from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Member


@receiver(post_delete, sender=Member)
def delete_user_on_member_delete(sender, instance, **kwargs):
    try:
        user = User.objects.get(id=instance.User_Id)
        user.delete()
    except User.DoesNotExist:
        pass