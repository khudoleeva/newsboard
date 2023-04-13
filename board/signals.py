from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Comment, New, User
from django.contrib.auth.models import Group

@receiver(post_save, sender=Comment)
def my_comment(update_fields, instance, **kwargs):
	post_id = instance.one_to_many_new.id
	text_com = instance.text_comment
	if instance.switch:
		author = instance.one_to_many_user
		html_content = render_to_string('tomail.html', {'newtext': text_com, 'username':author,'post_id':post_id})
		msg = EmailMultiAlternatives(
			subject='Ваш комментарий принят!',
			body=f'Привет, {author}',
			from_email='ovechkinak@yandex.ru',
			to=[f'{author.email}'],
		)
		msg.attach_alternative(html_content, "text/html")
		msg.send()
	else:
		author_post = instance.one_to_many_new.author
		html_content = render_to_string('tomail2.html', {'newtext': text_com, 'username': author_post, 'post_id': post_id})
		msg = EmailMultiAlternatives(
			subject='Новый комментарий!',
			body=f'Привет, {author_post.username}',
			from_email='ovechkinak@yandex.ru',
			to=[f'{author_post.email}'],
		)
		msg.attach_alternative(html_content, "text/html")
		msg.send()

@receiver(post_save, sender=New)
def my_news(instance, **kwargs):
	post_name = instance.name
	post_text = instance.text
	id_post = instance.id
	print(post_name)
	group = Group.objects.get(name='basic')
	# premium_group.user_set
	users = group.user_set.all()
	list_email = []
	for user in users:
		user_s = user.username
		print(user.email)
		sub = user.email
		if sub not in list_email:
			list_email.append(sub)
			html_content = render_to_string(
				'tomail3.html', {'newtitle': post_name, 'newtext': post_text, 'username': user_s, 'id_post': id_post}
			)
			msg = EmailMultiAlternatives(
				subject='У нас для вас новости!',
				body=f'Привет, {user_s}',
				from_email='ovechkinak@yandex.ru',
				to=[f'{sub}'],
				)
			msg.attach_alternative(html_content, "text/html")
			msg.send()
