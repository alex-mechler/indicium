# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Symptoms(models.Model):
    id = models.TextField(primary_key=True, db_column='ID', blank=True, null=False)  # Field name made lowercase.
    user_id = models.TextField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    control_id = models.TextField(db_column='CONTROL_ID', blank=True, null=True)  # Field name made lowercase.
    symptom = models.TextField(db_column='SYMPTOM', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    intensity = models.IntegerField(db_column='INTENSITY', blank=True, null=True)  # Field name made lowercase.
    start = models.IntegerField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    end = models.IntegerField(db_column='END', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', blank=True, null=True)  # Field name made lowercase.
    img_url = models.TextField(db_column='IMG_URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SYMPTOMS'


class User(models.Model):
    id = models.TextField(primary_key=True, db_column='ID', blank=True, null=False)  # Field name made lowercase.
    control_id = models.TextField(db_column='CONTROL_ID', blank=True, null=True)  # Field name made lowercase.
    first_name = models.TextField(db_column='FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    last_name = models.TextField(db_column='LAST_NAME', blank=True, null=True)  # Field name made lowercase.
    dob = models.TextField(db_column='DOB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    doctor_email = models.TextField(db_column='DOCTOR_EMAIL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER'


