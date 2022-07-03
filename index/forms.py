from .models import Articles
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'full_name', 'course', 'description', 'tel', 'url_vk', 'gmail']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control fc',
                'type': 'text',
                'name': 'name',
                'placeholder': 'Имя',
                'aria-label': 'Имя',
            }),
            "full_name": TextInput(attrs={
                'class': 'form-control fc',
                'type': 'text',
                'name': 'subname',
                'placeholder': 'Фамилия',
                'aria-label': 'Фамилия',
            }),
            "course": TextInput(attrs={
                'class': 'form-control fc',
                'type': 'text',
                'name': 'name',
                'placeholder': 'Курс',
                'aria-label': 'Курс',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'skill',
                'placeholder': 'Опишите свои навыки',
                'aria-label': 'Опишите свои навыки',
                'rows': '3',
                'id': 'exampleFormControlTextarea1'
            }),
            "tel": TextInput(attrs={
                'class': 'form-control fc1',
                'name': 'phone',
                'placeholder': 'Введите номер телефона',

            }),
            "url_vk": TextInput(attrs={
                'class': 'form-control fc1',
                'name': 'vkontakte',
                'placeholder': 'Ссылка на VK или Telegram',
                'aria-label': 'Ссылка на Вконтакте',
            }),
            "gmail": TextInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'name': 'email',
                'id': 'inputEmail3',
                'placeholder': 'email@email.ru',
                'aria-label': 'email@email.ru',
            }),
        }


class BooleanFieldFrom(forms.Form):
    CheckboxInput = forms.BooleanField(label='', required=True)
