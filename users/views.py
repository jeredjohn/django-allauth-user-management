from allauth.account.views import SignupView, LoginView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, TemplateView
from .models import CustomUser
from django.urls import reverse_lazy
from .forms import AccountSignUpForm, AccountUpdateForm, AccountLoginForm


class AccountLoginView(LoginView):
    form_class = AccountLoginForm
    model = CustomUser
    template_name = 'account/login.html'
      
account_login_view = AccountLoginView.as_view()


class AccountSignupView(SignupView):
    form_class = AccountSignUpForm
    model = CustomUser
    template_name = "users/users_custom_signup.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    
    #     ...

account_signup_view = AccountSignupView.as_view()


class UserAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_account.html'

user_account = UserAccountView.as_view()


class AccountUpdateView(UpdateView):
    model = CustomUser
    form_class = AccountUpdateForm
    template_name = 'users/account_update_form.html'
    success_message = "Account updated!"
    success_url = reverse_lazy('user_account')

account_update = AccountUpdateView.as_view()
