# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Unit Heads(models.Model):

    #__Unit Heads_FIELDS__
    service no = models.IntegerField(null=True, blank=True)
    year of enlistment = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Unit Heads_FIELDS__END

    class Meta:
        verbose_name        = _("Unit Heads")
        verbose_name_plural = _("Unit Heads")


class Members(models.Model):

    #__Members_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    office = models.CharField(max_length=255, null=True, blank=True)
    rank = models.CharField(max_length=255, null=True, blank=True)
    service no = models.CharField(max_length=255, null=True, blank=True)

    #__Members_FIELDS__END

    class Meta:
        verbose_name        = _("Members")
        verbose_name_plural = _("Members")



#__MODELS__END
