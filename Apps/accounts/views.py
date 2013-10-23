
from django.views.generic import FormView
from forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User


class LoginView(FormView):

    form_class = LoginForm
    template_name = "index.html"

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('')
        context = {'form':self.form_class()}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        data = request.POST.copy()
        form = self.form_class(data)
        context = {}
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username=email,password=password)

                if user is not None:
                    login(request,user)
                    next = request.GET.get('next', None)
                    if next:
                        return HttpResponseRedirect(next)
                    return  HttpResponseRedirect('""')
                else:
                    context['message'] = 'Invalid Username or Password'
                    context['form']= form
                    return self.render_to_response(context)
            except User.DoesNotExist:
                context['message']='Invalid Username or Password'
                context['form']= form
                return self.render_to_response(context)
        context['form']= form
        return self.render_to_response(context)

