from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    pass


class OrganisationProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username


class Lead(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return f"Lead for: {self.first_name} {self.last_name}, ID: {self.id}"


class Agent(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(
        OrganisationProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Agent: {self.user.username} ; {self.user.email}'


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        OrganisationProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
