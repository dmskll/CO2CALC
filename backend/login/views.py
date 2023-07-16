from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from sesame.utils import get_query_string

from .forms import EmailLoginForm

class EmailLoginView(FormView):
    template_name = "email_login.html"
    form_class = EmailLoginForm

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        
        User = get_user_model()
        user = User.objects.get(email=email)

        link = reverse("login")
        link = self.request.build_absolute_uri(link)
        link += get_query_string(user)
        user.email_user(
                        subject="[django-sesame] Log in to our app",
                        message=f"""\
            Hello,

            You requested that we send you a link to log in to our app:

                {link}

            Thank you for using django-sesame!
            """)

        return render(self.request, "email_login_ok.html")