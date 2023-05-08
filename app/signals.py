from django.db.models.signals import post_save
from app.models import( 
    Student ,
    StudentProfile ,
)
from django.dispatch import receiver




@receiver(post_save, sender=Student)
def create_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(student=instance)


@receiver(post_save, sender=Student)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()