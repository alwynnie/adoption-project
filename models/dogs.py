class Dog(object):
    def __init__(self, id, name, breed, age, gender, size, weight, health_status, vaccinated, adoption_status, temper):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.size = size #pequeno, mediano, intermedio, grande
        self.weight = weight
        self.health_status = health_status
        self.vaccinated = vaccinated
        self.adoption_status = adoption_status
        self.temper = temper
        

    def change_status(self, new_status):
        if new_status == 'disponible' or 'reservado' or 'adoptado':
            self.adoption_status = new_status

    def show_information(self):
        print(f'ID: {self.id} \nNombre: {self.name}  \nRaza: {self.breed} \nEdad: {self.age} \nGenero: {self.gender} \nTamano: {self.size} \nPeso: {self.weight} \nEstado de salud: {self.health_status} \nVacunas: {self.vaccinated} \nEstado: {self.adoption_status} \nTemperamento: {self.temper}')

Chita = Dog(1, 'Chita', 'golden retriever', 12, 'hembra', 'mediano', 65, 'saludable', 'vacunas completas', 'disponible', 'leal')

Chita.show_information()
Chita.change_status('reservado')
Chita.show_information()