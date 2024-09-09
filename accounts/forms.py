from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (AuthenticationForm,  UserCreationForm)

from accounts.models import RelationShip, RelativeModel

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username or Email', 'id': 'id_username'}), label="Username or Email*")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'id_password'}))

class RegistrationForm(UserCreationForm):
    confirm_email = forms.EmailField(help_text="Confirm your email address", required=True, widget=forms.EmailInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}),
            'email': forms.EmailInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}),
            'confirm_email': forms.EmailInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}),
            'first_name': forms.TextInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}),
            'last_name': forms.TextInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}),
            #'hobbies': forms.TextInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}),
            'password1': forms.PasswordInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}),
            'password2': forms.PasswordInput(attrs={"class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"}),
            
        }

    def clean_email(self):
        email = self.cleaned_data["email"]

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(f'This email: {email} is already in use.')
        
        return email
    
    def clean(self):
        clean = super().clean()
        second_email = clean.get("confirm_email", None)
        mail = clean.get("email", None)

        if second_email and mail and mail != second_email:
            raise forms.ValidationError(f'This email: {mail} does not match with confirmation email.')
        
        

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()

        return user

class AccountUpdateForm(forms.ModelForm):
    
    class Meta:
        model = get_user_model()
        fields = ["title", "gender", "identity_number", "profile_image", "first_name", "last_name", 'maiden_name', "biography", "identity_number"]

        widgets = {
            'username': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            'title': forms.Select(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150"}),
            'first_name': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            'maiden_name': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            'last_name': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            #'hobbies': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            
        }

    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field_value in self.initial.items():
            if field_value is None:
                self.initial[field_name] = ''
     
class GeneralEditForm(forms.ModelForm):
    """
        Form to edit only username and email
    """
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "phone", "address_one", "address_two", "city", "country", "province", "zipcode"]

        widgets = {
            'address_one': forms.TextInput(attrs={"class": "block p-2 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            'address_two': forms.TextInput(attrs={"class": "block p-2 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            'city': forms.TextInput(attrs={"class": "block p-2 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            'country': forms.TextInput(attrs={"value": "South Africa", "class": "block p-2 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            'province': forms.TextInput(attrs={"class": "block p-2 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"}),
            'zipcode': forms.NumberInput(attrs={"class": "block p-2 md:text-base w-full text-sm text-gray-900 outline-none bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary placeholder:text-gray-400 focus:border-custom-primary ease-linear transition-all duration-150"})
        }

    def __init__(self, *args, **kwargs):
        super(GeneralEditForm, self).__init__(*args, **kwargs)
        for field_name, field_value in self.initial.items():
            if field_value is None:
                self.initial[field_name] = ''

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get("email")
        if get_user_model().objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(f'This username: {username} is already in use.')
        
        if get_user_model().objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(f'This email: {email} is already in use.')
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super(GeneralEditForm, self).save(commit=False)
        email = self.cleaned_data['email']
        if commit:
            user.save()
            
        return user

class RelativeForm(forms.ModelForm):
    class Meta:
        model = RelativeModel
        fields = ['title', 'surname', 'full_name', 'relationship', 'phone', 'email', 'maiden_name']

        widgets = {
            'title': forms.Select(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150"}),
            'full_name': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150"}),
            'surname': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150"}),
            'maiden_name': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150"}),
            'relationship': forms.Select(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150"}),
            }
    
    def __init__(self, *args, **kwargs):
        super(RelativeForm, self).__init__(*args, **kwargs)
        for field_name, field_value in self.initial.items():
            if field_value is None:
                self.initial[field_name] = ''

    # def clean(self):
    #     clean = super().clean()
    #     name = clean.get("full_name", None)
    #     last_name = clean.get("surname", None)
    #     other_surname = clean.get("maiden_name", None)
    #     relation = clean.get("relationship", None)
    #     gender = clean.get("gender", None)
    #     relative = RelativeModel.objects.filter(full_name = name, surname = last_name, maiden_name = other_surname, gender=gender, relationship = relation).exists()

    #     if relative:
    #         raise forms.ValidationError(f"Relative with following details already exists")

    #     return clean

        