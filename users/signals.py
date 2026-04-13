from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from members.models import Teacher, Student

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=Profile)
def create_member_profile(sender, instance, created, **kwargs):
    if instance.user_type == 'teacher':
        Teacher.objects.get_or_create(
            user=instance.user,
            defaults={'name': instance.user.username, 'email': instance.user.email}
        )
    elif instance.user_type == 'student':
        import uuid
        Student.objects.get_or_create(
            user=instance.user,
            defaults={'enrollment_number': str(uuid.uuid4())[:8].upper()}
        )
