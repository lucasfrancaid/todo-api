from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.is_superuser = True
            user.is_staff = True
            user.set_password('123')
            user.save()

        print('User admin was created!')