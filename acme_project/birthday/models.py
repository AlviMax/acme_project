# birthday/models.py
from django.db import models
# Импортируется функция-валидатор.
from .validators import real_age

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    # здесь мы подключили наш кастомный валидатор real_age
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    # Подключаем поле с изображением, указываем куда загружать фото и делаем 
    # поле не обязательным (если пользователь не захочет загружать фото, то он 
    # может оставить это поле пустым).
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
