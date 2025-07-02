from django.contrib import admin
from .models.dogs import Dog

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'adoption_status', 'vaccinated', 'created_at')
    list_filter = ('adoption_status', 'size', 'gender', 'vaccinated', 'age')
    search_fields = ('name', 'breed')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    actions = ['make_adopted', 'make_reserved', 'make_available']

    @admin.action(description='Marcar como Adoptado')
    def make_adopted(self, request, queryset):
        queryset.update(adoption_status='adopted')

    @admin.action(description='Marcar como Reservado')
    def make_reserved(self, request, queryset):
        queryset.update(adoption_status='reserved')

    @admin.action(description='Marcar como Disponible')
    def make_available(self, request, queryset):
        queryset.update(adoption_status='available')
