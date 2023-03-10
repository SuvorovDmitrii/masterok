from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserPageForm
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, ListView
from django import forms
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def getpage(request):
    return render(request, "index.html")

class ShowUserPageView(DetailView):
    model = Person
    template_name = 'registration/user_page.html'

    def get_object(self):
        # users = User.objects.filter(id__exact = self.request.user.id)
        # patronomyc = users.get(Person.patronomyc)
        try:
            person = Person.objects.get(user=self.request.user.id)
        except:
            person = None
        return person

        # if self.request.user.id in Person.user.id:
        #     person = Person.objects.get(user = self.request.user.id)
        #     return person#, render(request, 'registration/user_page.html',context={'patronomyc':patronomyc, 'img':img})
        # else:
        #     return get_object_or_404(User, self.request.user.id)

'''
    def get_context_data(self, *args, **kwargs):
        users = Person.objects.all()
        context = super(ShowUserPageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.request.user.id)
        context['page_user'] = page_user
        context['users'] = users
        return context, get_object_or_404(User, id=self.request.user.id)
'''


class UserUpdatePage(UpdateView):
    model = Person, User
    template_name = 'user_update_form.html'
    fields = ('patronomyc', )
    def get_object(self):
        return get_object_or_404(User, id = self.request.user.id)

def login(request):
    return render(request, 'login.html')

def main(request):
    model = Order
    count = model.objects.filter(status__exact = 3).count()
    orders = model.objects.filter(status__exact = 3)
    users = Person.objects.all()
    return render(request, 'base_generic.html', context={
        'count':count,
        'users':users,
        'orders': orders,
    })


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})
