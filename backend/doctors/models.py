from django.db import models
from users.models import User

class Hospital (models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


    def __str__(self):
        return self.name




class Medecin (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=50)
    Second_name = models.CharField(max_length=50)
    CIN = models.CharField(max_length=50, unique = True)
    hospital = models.ForeignKey(Hospital, verbose_name="hospital", on_delete=models.CASCADE)
    id_prof = models.CharField(unique = True, max_length=50)
    phone = models.CharField(max_length=50, unique = True)
    add_date = models.DateTimeField(auto_now_add=True)
    
    


    def __str__(self):
        return self.CIN

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
