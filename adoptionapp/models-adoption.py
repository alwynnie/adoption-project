from django.db import models
from models.dogs import Dog
from models.adopting_user import AdoptingUser

class AdoptionRequest(models.Model):
    adoption_id = models.AutoField(primary_key=True)
    dog_id = models.ForeignKey(Dog, on_delete=models.SET_NULL, null = True)
    dog_name = models.CharField(max_length=20)
    application_date = models.DateField()
    user_id = models.ForeignKey(AdoptingUser, on_delete=models.SET_NULL, null = True)
    user_name = models.CharField(max_length=60)

