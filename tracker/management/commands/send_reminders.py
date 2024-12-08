from django.core.management.base import BaseCommand
from django.utils import timezone
from tracker.models import Task
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Send email reminders for upcoming tasks due today.'

    def handle(self, *args, **options):
        today = timezone.now().date()
        due_today = Task.objects.filter(due_date=today, completed=False)
        for task in due_today:
            user = task.goal.user
            subject = f"Reminder: {task.title} due today"
            message = f"Hello {user.username},\n\nYour task '{task.title}' for goal '{task.goal.title}' is due today."
            send_mail(subject, message, 'admin@goaltracker.com', [user.email], fail_silently=True)
            self.stdout.write(self.style.SUCCESS(f"Reminder sent to {user.email} for {task.title}."))
