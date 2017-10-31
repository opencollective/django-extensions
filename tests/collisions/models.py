# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Note(models.Model):
    # name conflict with testapp.Note
    text = models.CharField(max_length=42)
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        app_label = 'collisions'


class UniqueModel(models.Model):
    # no conflicts
    global_hash_id = models.CharField(max_length=32)

    class Meta:
        app_label = 'collisions'


class Group(models.Model):
    # conflict with django.contrib.auth
    name = models.CharField(max_length=10)
    priority = models.IntegerField()


class Name(models.Model):
    # name conflict with testapp.Name
    real_name = models.CharField(max_length=50)
    number_of_users_having_this_name = models.IntegerField()

    class Meta:
        app_label = 'collisions'


class SystemUser(models.Model):
    # no conflicts but FK to conflicting models.
    name = models.ForeignKey(Name)
    group = models.ForeignKey(Group)
    global_id = models.CharField(unique=True, max_length=32)