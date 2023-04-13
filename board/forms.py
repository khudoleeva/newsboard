from django.forms import ModelForm
from django import forms
from .models import *

class PostForm(ModelForm):
	class Meta:
		model = New
		fields = ['name', 'text', 'category', 'author']
		labels = {
			'name': 'Заголовок',
			'text': 'Текст',
			'category': 'Категория',
			'author': 'Автор'
		}
