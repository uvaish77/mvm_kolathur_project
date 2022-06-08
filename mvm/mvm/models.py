from django.db import models

class sendmail(models.Model):
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=50)
    email_id = models.CharField(max_length=150)
    comment = models.CharField(max_length=150)

    class meta:
        db_table = 'send_email'

class matric(models.Model):
    applicant_name = models.CharField(max_length=150)
    dob = models.CharField(max_length=150)
    mobile_matric = models.CharField(max_length=50)
    gender = models.CharField(max_length=150)
    religion = models.CharField(max_length=150)
    std = models.CharField(max_length=150)
    nationality = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    father_occupation = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    mother_occupation = models.CharField(max_length=150)
    annual_income = models.CharField(max_length=150)
    community = models.CharField(max_length=150)
    last_school = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    present_address = models.CharField(max_length=150)
    permanent_address = models.CharField(max_length=150)


    class meta:
        db_table = 'enquiry_matric'