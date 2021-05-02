from django.db import models
from doctors.models import Medecin, Hospital



class Patient(models.Model):
    First_name = models.CharField(max_length=50)
    Second_name = models.CharField(max_length=50)
    cin = models.CharField(max_length=50,unique = True)
    phone = models.CharField(unique=True,max_length=50)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    hopital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    onset_state = models.TextField()
    chronic = models.TextField()
    vacc = models.BooleanField(default = False)
    reinfect = models.BooleanField(default = False)
    add_date = models.DateTimeField(auto_now_add=True)

    

    # class Meta:
    #     verbose_name = _("Patient")
    #     verbose_name_plural = _("Patients")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Patient_detail", kwargs={"pk": self.pk})

class Virus(models.Model):
    patient = models.ForeignKey(Patient, verbose_name='patient', on_delete=models.CASCADE)
    file = models.FileField(upload_to=f'virus/{patient}', max_length=50000)


    

    # class Meta:
    #     verbose_name = _("Virus")
    #     verbose_name_plural = _("Viruss")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Virus_detail", kwargs={"pk": self.pk})
class ACE(models.Model):
    patient = models.ForeignKey(Patient, verbose_name='patient', on_delete=models.CASCADE)
    file = models.FileField(upload_to=f'ace2/{patient}', max_length=50000000)

    

    # class Meta:
    #     verbose_name = _("ACE")
    #     verbose_name_plural = _("ACEs")

    # def __str__(self):
    #     return f'{self.pos}{self.ref}>{self.alt}'

    # def get_absolute_url(self):
    #     return reverse("ACE_detail", kwargs={"pk": self.pk})
class Virus_var(models.Model):
    ref = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)
    pos = models.IntegerField()
    impact = models.CharField(max_length=50)
    gene = models.CharField(max_length=50)
    protein_var = models.CharField(max_length=50)
    

    # class Meta:
    #     verbose_name = _("Virus_var")
    #     verbose_name_plural = _("Virus_vars")

    def __str__(self):
        return f'{self.pos}{self.ref}>{self.alt}'

    # def get_absolute_url(self):
    #     return reverse("Virus_var_detail", kwargs={"pk": self.pk})
class ACE_Var(models.Model):
    ref = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)
    pos = models.IntegerField()
    impact = models.CharField(max_length=50)
    protein_var = models.CharField(max_length=50)
    

    # class Meta:
    #     verbose_name = _("ACE_Var")
    #     verbose_name_plural = _("ACE_Vars")

    def __str__(self):
        return f'{self.pos}{self.ref}>{self.alt}'

    # def get_absolute_url(self):
    #     return reverse("ACE_Var_detail", kwargs={"pk": self.pk})



class Status(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    more_infos = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    predicted = models.BooleanField(default = False)


    

    # class Meta:
    #     verbose_name = _("Status")
    #     verbose_name_plural = _("Statuss")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Status_detail", kwargs={"pk": self.pk})


