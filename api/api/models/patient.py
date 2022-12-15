from django.db import models

class Patient(models.Model):
    GENDERS = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )

    INCOME_OPTIONS = (
        ('A', 'Ate 1.5 salarios minimos'),
        ('B', '1.5 ate 3 salarios minimos'),
        ('C', '3 a 5 salarios minimos'),
        ('D', 'Mais de 5 salarios minimos'),
    )

    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    nationality = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    fathers_age = models.IntegerField()
    fathers_profession = models.CharField(max_length=50)
    fathers_schooling = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    mothers_age = models.IntegerField()
    mothers_profession = models.CharField(max_length=50)
    mothers_schooling = models.CharField(max_length=50)
    family_income = models.FloatField(max_length=1, choices=INCOME_OPTIONS)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    cns = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    rg = models.CharField(max_length=50)
    encaminhado = models.CharField(max_length=50)
    review_date = models.DateField()
    clinical_diagnosis = models.CharField(max_length=50)
    physiotherapist_in_charge = models.CharField(max_length=50)
    academic_in_charge = models.CharField(max_length=50)
