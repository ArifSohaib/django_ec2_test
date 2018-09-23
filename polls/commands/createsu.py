from django.contrib.auth.models import User

def makeuser():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@admin.com", "admin")
makeuser()
