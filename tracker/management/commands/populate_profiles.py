from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tracker.models import Profile

class Command(BaseCommand):
    help = 'Create Profile instances for users without one.'

    def handle(self, *args, **options):
        users = User.objects.all()
        created_profiles = 0
        for user in users:
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                created_profiles += 1
                self.stdout.write(self.style.SUCCESS(f'Created profile for user: {user.username}'))
        self.stdout.write(self.style.SUCCESS(f'Total profiles created: {created_profiles}'))
