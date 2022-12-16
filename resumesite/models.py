from django.db import models

# Create your models here.
class std(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    address = models.CharField(max_length=122, blank=True, null=True)
    description = models.CharField(max_length=122)
    skill_1 = models.CharField(max_length=122)
    skill_2 = models.CharField(max_length=122)
    skill_3 = models.CharField(max_length=122)
    skill_4 = models.CharField(max_length=122)
    skill_5 = models.CharField(max_length=122, blank=True, null=True)
    skill_6 = models.CharField(max_length=122, blank=True, null=True)
    exp_1_title = models.CharField(max_length=122)
    exp_1_duration = models.CharField(max_length=122)
    exp_1_description = models.CharField(max_length=122)
    exp_2_title = models.CharField(max_length=122, blank=True, null=True)
    exp_2_duration = models.CharField(max_length=122, blank=True, null=True)
    exp_2_description = models.CharField(max_length=122, blank=True, null=True)
    education_10th_year = models.CharField(max_length=122)
    education_10th_uni = models.CharField(max_length=122)
    education_10th_score = models.CharField(max_length=122)
    education_12th_year = models.CharField(max_length=122)
    education_12th_uni = models.CharField(max_length=122)
    education_12th_score = models.CharField(max_length=122)
    education_btech_year = models.CharField(max_length=122)
    education_btech_uni = models.CharField(max_length=122)
    education_btech_score = models.CharField(max_length=122)
    education_mtech_year = models.CharField(max_length=122, blank=True, null=True)
    education_mtech_uni = models.CharField(max_length=122, blank=True, null=True)
    education_mtech_score = models.CharField(max_length=122, blank=True, null=True)

    def __int__(self):
        return self.id


class resume(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.FileField()