from django.contrib import admin
from .models import Birthday


# Зарегистрируем модель Birthday в админке
@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birthday')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'last_name')


#Альтернативная простая запись (если не нужны настройки отображения):
#admin.site.register(Birthday)
