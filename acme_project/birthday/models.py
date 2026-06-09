# birthday/models.py
from django.db import models
# Импортируется функция-валидатор.
from .validators import real_age
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse

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
    # Т.к. мы уходим от view-функций и переходим на классы, то нам нужно будет 
    # реализовать метод get_absolute_url(), который будет возвращать 
    # URL объекта. Этот метод используется Django для автоматического 
    # перенаправления после успешного создания или редактирования объекта через
    # CreateView/UpdateView (если не указан success_url)..
    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})
    