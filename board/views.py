from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import Group

class NewsList(ListView):
	model = New
	template_name = 'news.html'
	context_object_name = 'news'
	ordering = ['-date']

class NewDetail(DetailView):
	model = New
	template_name = 'new.html'
	context_object_name = 'new'

class NewCreate(CreateView):
	template_name = 'create.html'
	form_class = PostForm

class NewUpdate(UpdateView):
	template_name = 'create.html'
	form_class = PostForm
	def get_object(self, **kwargs):
		id = self.kwargs.get('pk')
		return New.objects.get(pk=id)

class NewDelete(DeleteView):
	template_name = 'delete.html'
	queryset = New.objects.all()
	success_url = '/board/'

class UserView(LoginRequiredMixin, TemplateView):
	template_name = 'user.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		my_user = User.objects.get(id=self.request.user.id)
		context['my_news'] = my_user.new_set.all()
		return context

@login_required
def Comment_save(request):
	if request.POST['u_name']:
		newid = int(request.POST['new_id'])
		uname = int(request.POST['u_name'])
		mess = request.POST['message']
		sub = New.objects.get(id=newid)
		sub2 = User.objects.get(id=uname)
		rec_comment = Comment(text_comment=mess, one_to_many_new=sub, one_to_many_user=sub2)
		rec_comment.save()
	return redirect('/board/comment_save')

def CommentDel(request):
	if request.method == 'POST':
		del_com = request.POST['del_com']
		my_comment = Comment.objects.get(id=del_com)
		my_comment.delete()
	return redirect('/board/comment_save')
def CommentSend(request):
	if request.method == 'POST':
		send_com = request.POST['send_com']
		my_comment2 = Comment.objects.get(id=send_com)
		my_comment2.switch = True
		my_comment2.save()
	return redirect('/board/comment_save')

class Com(LoginRequiredMixin, TemplateView):
	template_name = 'comment_save.html'

def Navigat(request):
	if request.method == 'GET':
		cate = str(request.GET.get('T'))
		sub = New.objects.filter(category=cate)
		print('ok', sub)
	return render(request, 'news.html', {'news': sub})

def AddGroup(request):
	if request.method == 'POST':
		id_user = request.POST['ok']
		my_user = User.objects.get(id=id_user)
		basic_group = Group.objects.get(name='basic')
		basic_group.user_set.add(my_user)
	return redirect('/board/comment_save')