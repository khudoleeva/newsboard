from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class New(models.Model):
	list_category = [("Танки", "Танки"), ("Хилы", "Хилы"),("ДД", "ДД") ,("Торговцы", "Торговцы") , ("Гилдмастеры", "Гилдмастеры"),("Квестгиверы", "Квестгиверы") ,("Кузнецы", "Кузнецы") ,("Кожевники", "Кожевники") , ("Зельевары", "Зельевары"), ("Мастера заклинаний", "Мастера заклинаний")]
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=255)
	text = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.CharField(max_length=20, choices=list_category)
	def __str__(self):
		return f'{self.name}  {self.text[:20]}'
	def get_absolute_url(self):
		return f'/board/{self.id}'


class Comment(models.Model):
	text_comment = models.TextField()
	date_comment = models.DateTimeField(auto_now_add=True)
	one_to_many_new = models.ForeignKey(New, on_delete=models.CASCADE)
	one_to_many_user = models.ForeignKey(User, on_delete=models.CASCADE)
	switch = models.BooleanField(default=False)
