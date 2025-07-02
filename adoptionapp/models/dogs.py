from django.db import models

class Dog(models.Model):
    STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('reserved', 'Reservado'),
        ('adopted', 'Adoptado'),
    ]
    name = models.CharField(max_length=60)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Macho'),
        ('female', 'Hembra'),
    ])
    size = models.CharField(max_length=20, choices=[
        ('small', 'Pequeño'),
        ('medium', 'Mediano'),
        ('large', 'Grande'),
    ])
    weight = models.PositiveIntegerField(blank=True, null=True)
    health_status = models.CharField(max_length=50, choices=[
        ('healthy', 'Saludable'),
        ('needs healthcare attention', 'Necesita cuidados'),
    ])
    vaccinated = models.BooleanField(default=False)
    adoption_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    temper = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    # def change_status(self, new_status):
    #     if new_status == 'disponible' or 'reservado' or 'adoptado':
    #         self.adoption_status = new_status

    # def show_information(self):
    #     print(f'ID: {self.id} \nNombre: {self.name}  \nRaza: {self.breed} \nEdad: {self.age} \nGenero: {self.gender} \nTamano: {self.size} \nPeso: {self.weight} \nEstado de salud: {self.health_status} \nVacunas: {self.vaccinated} \nEstado: {self.adoption_status} \nTemperamento: {self.temper}')
