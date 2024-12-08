from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Goal(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    is_recurring = models.BooleanField(default=False)
    recurrence_period = models.CharField(max_length=50, blank=True, help_text="e.g. weekly, monthly")

    def __str__(self):
        return self.title

    def progress(self):
        tasks = self.tasks.all()
        if not tasks:
            return 0
        completed_tasks = tasks.filter(completed=True).count()
        return (completed_tasks / tasks.count()) * 100

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
