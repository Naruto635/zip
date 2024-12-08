from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Goal, Task, Profile
from .forms import GoalForm, TaskForm, RegistrationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from .utils import generate_ics

def home(request):
    return render(request, 'home.html')

@login_required
def profile_view(request):
    # Ensure the profile exists; get_or_create will handle missing profiles
    profile, created = Profile.objects.get_or_create(user=request.user)
    if created:
        messages.info(request, "A new profile has been created for you.")

    # Gather task statistics
    total_tasks = Task.objects.filter(goal__user=request.user).count()
    completed_tasks = Task.objects.filter(goal__user=request.user, completed=True).count()
    incomplete_tasks = total_tasks - completed_tasks

    # Prepare data for the chart
    chart_data = {
        'labels': ['Completed Tasks', 'Incomplete Tasks'],
        'data': [completed_tasks, incomplete_tasks],
    }

    return render(request, 'registration/profile.html', {
        'profile': profile,
        'chart_data': chart_data,
    })

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    # For chart.js data:
    data = []
    labels = []
    for goal in goals:
        labels.append(goal.title)
        completed = goal.tasks.filter(completed=True).count()
        total = goal.tasks.count()
        data.append((completed, total - completed))
    return render(request, 'goal_list.html', {'goals': goals, 'labels': labels, 'data': data})

@login_required
def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, "Goal created successfully!")
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'goal_form.html', {'form': form})

@login_required
def task_list(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    tasks = goal.tasks.all()
    return render(request, 'task_list.html', {'goal': goal, 'tasks': tasks})

@login_required
def task_create(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.goal = goal
            task.save()
            messages.success(request, "Task created successfully!")
            return redirect('task_list', goal_id=goal.id)
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'goal': goal})

@login_required
def complete_task(request, goal_id, task_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    task = get_object_or_404(Task, id=task_id, goal=goal)
    task.completed = True
    task.save()
    # Award points
    profile = Profile.objects.get(user=request.user)
    profile.points += 10
    profile.save()
    messages.success(request, "Task marked as completed! Points awarded.")
    return redirect('task_list', goal_id=goal.id)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically create Profile via signals
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def export_ics(request):
    # Export all tasks of the user as an ICS file
    goals = Goal.objects.filter(user=request.user)
    tasks = Task.objects.filter(goal__in=goals)
    ics_content = generate_ics(tasks)
    response = HttpResponse(ics_content, content_type='text/calendar')
    response['Content-Disposition'] = 'attachment; filename="tasks.ics"'
    return response
