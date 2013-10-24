from django.http import HttpResponse

class LoginView(FormView):
    form_class = LoginForm
    template = "front.html"

