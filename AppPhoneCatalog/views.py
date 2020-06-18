from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, render, redirect
from .models import Catalog, Message
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from datetime import datetime
from django.http import JsonResponse
import json
from django import forms
from django.utils.translation import gettext, gettext_lazy as _





def index(request):

    return render(
        request,
        "index.html",
        {
            "Catalog": Catalog.objects.order_by('RegDate')[:10],
            "latest_messages": Message.objects.order_by('-pub_date')[:5]

        }
    )


app_url ='/AppPhoneCatalog/'

def post(request):
    msg = Message()
    msg.author = request.user
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url)


def msg_list(request):
    res = list(
            Message.objects
                .order_by('-pub_date')[:5]
                .values('author__username',
                        'pub_date',
                        'message'
                )
            )
    for r in res:
        r['pub_date'] = \
            r['pub_date'].strftime(
                '%d.%m.%Y %H:%M:%S'
            )
    return JsonResponse(json.dumps(res), safe=False)



def admin(request):

    return render(
        request,
        "admin.html",
        {
            "Catalog": Catalog.objects.order_by('RegDate')[:10],
        }
    )



def postInform(request):
    newRecord=Catalog()
    newRecord.Name=request.POST['NameCompany']
    newRecord.RegDate=datetime.now()
    newRecord.Adress=request.POST['Adress']
    newRecord.Phone=request.POST['Phone']
    newRecord.save()
    for i in User.objects.all():
        if i.email != '':
            send_mail(
                'New Information',
                'New Company added' +
                'http://localhost:8000/AppPhoneCatalog.',
                'pythonmakavchik@gmail.com',
                [i.email],
                False
            )

    return HttpResponseRedirect(app_url)



class SubscribeForm(forms.Form):
    email = forms.EmailField(
        label=_("E-mail"),
        required=True,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.user.email = self.cleaned_data["email"]
        if commit:
            self.user.save()
        return self.user


class SubscribeView(FormView):
    form_class = SubscribeForm
    template_name = 'subscribe.html'
    success_url = app_url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def unsubscribe(request):
    request.user.email = ''
    request.user.save()
    return HttpResponseRedirect(app_url)



class Register(FormView):
    form_class = UserCreationForm
    success_url = app_url + "logIn/"
    template_name = "reg/RegisterPage.html"
    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)


class LogIn(FormView):
    form_class = AuthenticationForm
    template_name = "reg/logInPage.html"
    success_url = app_url
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LogIn, self).form_valid(form)

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)


class PasswordChange(FormView):
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
    success_url = app_url + 'logIn/'
    def get_form_kwargs(self):
        kwargs = super(PasswordChange, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs
    def form_valid(self, form):
        form.save()
        return super(PasswordChange, self).form_valid(form)