from accounts.forms import AccountUpdateForm, GeneralEditForm, UserLoginForm, RegistrationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from accounts.utilities.custom_email import send_email_confirmation_email, send_verification_email
from django.shortcuts import redirect, render, get_object_or_404
from accounts.utilities.decorators import user_not_authenticated
from accounts.utilities.tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import logging, jwt

from prop_home.utilities.decorators import user_not_superuser_or_staff



logger = logging.getLogger("accounts")
User = get_user_model()

@login_required
@user_not_superuser_or_staff
def manage_accounts(request):
    accounts = User.objects.all()
    return render(request, "accounts/manage-accounts-dashboard.html", {"accounts": accounts})

@login_required
def user_details(request, username):
    model = get_object_or_404(get_user_model().objects.all(), username=username)
    template = "accounts/account.html"
    context = {
        "user": model
    }
   

    return render(request, template, context)

@user_not_authenticated
def custom_login(request):
    next_page = request.GET.get("next", None)
    template_name = "accounts/login.html"
    success_url = "prop_home:prop-home"
    if next_page:
        success_url = next_page

    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None and user.is_active:
                login(request, user)
                messages.success(
                    request, f"Hello <b>{user.username}</b>! You have been logged in"
                )
                return redirect(success_url)
        else:
            account = User.objects.filter(username=form.cleaned_data["username"]).first()
            if account != None and not account.is_active:
                messages.error(request, f"Sorry your account is not active. We have sent account activation email to your email {account.email}")
                sent = send_verification_email(account, request)
                if not sent:
                    pass
                return redirect("accounts:login")
            
            return render(
                request=request, template_name=template_name, context={"form": form}
            )

    form = UserLoginForm()
    return render(request=request, template_name=template_name, context={"form": form})

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("prop_home:prop-home")

@user_not_authenticated
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        payload = jwt.decode(uidb64, settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(pk=payload["user_id"], username=payload["username"])
    except User.DoesNotExist:
        user = None
    
    if user and account_activation_token.check_token(user, token):
        if user.is_active == True:
            messages.success(
                request,
                "Thank you for your email confirmation. Now you can login your account.",
            )
            return redirect("accounts:login")
        
        user.is_active = True
        user.is_email_activated = True
        user.save(update_fields=["is_active", "is_email_activated"])

        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login your account.",
        )
        return redirect("accounts:login")
    else:
        messages.error(request, f"Activation link is expired! New activation link was sent to {user.email}")
        sent = send_verification_email(user, request)
        if not sent:
            logger.error(f"Something went wrong trying to send email to {user.username}")

    return redirect("prop_home:prop-home")

def confirm_email(request, uidb64, token):
    logout(request)
    User = get_user_model()
    try:
        payload = jwt.decode(uidb64, settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(pk=payload["user_id"], username=payload["username"])
    except:
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_email_activated = True
        user.save(update_fields=["is_active", "is_email_activated"])

        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login to your account with your new email.",
        )

        return redirect("accounts:login")
    
    else:
        messages.error(request, f"Email confirmation link is expired! New email confirmation link was sent to {user.email}")
        sent = send_email_confirmation_email(user, user.email, request)

        if not sent:
            logger.error(f"Something went wrong trying to send email to {user.username}")

    return redirect("prop_home:prop-home")

@user_not_authenticated
def register(request):
    template_name = "accounts/register.html"
    success_url = "accounts:success"
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # send_verification_email(user, request)
            # messages.success(
            #     request,
            #     f"Dear {user}, please go to you email {user.email} inbox and click on \
            #         received activation link to confirm and complete the registration. Note: Check your spam folder.",
            # )
            # return redirect(success_url)
            messages.success(request, "You have successfully register with us")
            return redirect("accounts:login")
        else:
            messages.error(request, "Something went wrong while signing up")
            return render(
                request=request, template_name=template_name, context={"form": form}
            )
    
    form = RegistrationForm()
    return render(request=request, template_name=template_name, context={"form": form})

@user_not_authenticated
def activation_sent(request):
    return render(request, "accounts/activation_sent.html")

@login_required
def general(request):
    template = "accounts/manage/general.html"

    if request.method == 'POST':
        form = GeneralEditForm(instance=request.user, data=request.POST)
        old_email = request.user.email

        if form.is_valid():
            new_email = form.cleaned_data["email"]
            user = form.save(commit=False)
            if old_email != new_email:
                user.is_email_activated = False
                sent = send_email_confirmation_email(request.user, new_email, request)
                if not sent:
                    logger.error(f"Email error - failed to send email to  {form.cleaned_data['email']}")

                messages.success(request, "we have also sent email confirmation to your new email address")
            else:
                user.email = old_email

            user.save(update_fields=["username", "email", "phone", "address_one", "address_two", "city", "country", "province", "zipcode"])
            messages.success(request, "Your information was updated successfully")
            return redirect("accounts:contact-update")
        else:

            messages.error(request, "Your information was updated unsuccessfull, please fix errors below")
            return render(request, template, {"form": form})
        
    form = GeneralEditForm(instance=request.user)

    
    return render(request, template, {"form": form})

@login_required
def account_update(request):
    template = "accounts/manage/update.html"

    if request.method == 'POST':
        form = AccountUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid() and form.is_multipart():
            form.save()
            messages.success(request, "Your information was updated successfully")
            return redirect("accounts:profile-update")
        else:
            return render(request, template, {"form": form})
        
    form = AccountUpdateForm(instance=request.user)  
    return render(request, template, {"form": form})
