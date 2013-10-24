from django.views.generic.detail import TemplateResponseMixin
from django.http import HttpResponse
from django.views.generic import FormView
from forms import LoginForm,SignupForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from models import LogUser
from django.conf import settings


class SignupView(FormView):
    form_class = SignupForm
    template_name = "signup.html"
    model = LogUser

    def get(self,request, *args, **kwargs):
            context = {'form':self.form_class()}
            return self.render_to_response(context)


    def post(self,request, *args, **kwargs):
        data = request.POST.copy()
        form = self.form_class(data)
        if form.is_valid():
            usr_account = self.register_user(form)
            message="success"
            return HttpResponseRedirect("/home")
        else:
            message = "error"
            context = {'form':form,'message': message}
        return self.render_to_response(context)


    def register_user(self,form):
        reg_data = self.model()
        reg_data.firstname = form.cleaned_data['email']
        reg_data.lastname = form.cleaned_data['lastname']
        reg_data.role = form.cleaned_data['role']
        reg_data.email = form.cleaned_data['email']
        reg_data.password = form.cleaned_data['password']
        reg_data.save()
        return reg_data



