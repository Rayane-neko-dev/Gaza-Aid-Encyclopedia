import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GAZA.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "ray.nacib@gmail.com"
password = "Rayane112001#"

user, created = User.objects.get_or_create(username=username, defaults={
    'email': email,
})
user.is_staff = True
user.is_superuser = True
user.set_password(password)
user.save()

if created:
    print("✅ Superuser created.")
else:
    print("⚠️ Superuser already existed. Flags updated.")
