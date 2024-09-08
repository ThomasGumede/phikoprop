from django import forms
# from accounts.custom_models.account import WalletModel
from prop_home.models import Blog, Comment, EmailModel, Member
from tinymce.widgets import TinyMCE

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", )

class SearchForm(forms.Form):
    SEARCH_CHOICES = (
        ("campaigns", "campaigns"),
        ("events", "events"),
        ("news", "news"),
        ("listings", "listings")
    )
    search_by = forms.ChoiceField(choices=SEARCH_CHOICES, required=False, widget=forms.Select(attrs={"class": "bg-gray-50 outline-none focus:outline-none border-none p-4 border rounded-md text-lg text-black focus:border-none h-full"}))
    query = forms.CharField(widget=forms.TextInput(attrs={"type": "search", "class": "bg-gray-50 outline-none focus:outline-none border-none p-2 py-2 rounded-md text-lg text-black focus:border-none h-full"}))

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = ('from_email', 'phone', 'name', 'message', 'subject')

        widgets = {
            "from_email": forms.EmailInput(attrs={"class": "text-body-color border-custom-h focus:border-custom-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none", "placeholder": "Your email"}),
            "subject": forms.TextInput(attrs={"class": "text-body-color border-custom-h focus:border-custom-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none", "placeholder": "Email subject"}),
            "name": forms.TextInput(attrs={"class": "text-body-color border-custom-h focus:border-custom-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none", "placeholder": "Your name"}),
            "phone": forms.TextInput(attrs={"class": "text-body-color border-custom-h focus:border-custom-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none", "type": "tel", "placeholder": "Your phone"}),
            "message": forms.Textarea(attrs={"class": "text-body-color border-custom-h focus:border-custom-primary w-full resize-none rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none", "placeholder": "Your message", "row": "6"}),
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('image', 'full_names', 'role', 'decription')

        widgets = {
            "image": forms.FileInput(attrs={"class": "w-[0.1px] h-[0.1px] opacity-0 overflow-hidden absolute -z-[1]"}),
            
            "full_names": forms.TextInput(attrs={"class": "text-body-color border-custom-h focus:border-custom-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none", "placeholder": "Full names"}),
            "role": forms.TextInput(attrs={"class": "text-body-color border-custom-h focus:border-custom-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none", "placeholder": "Role"}),
            "decription": TinyMCE(attrs={"class": "border-0 px-3 py-3 {% if form.content.errors %} h-44 border-2 border-red-500{% endif %} placeholder-gray-300 text-gray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150", "rows": 8}),
            }

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "image", "content", "category", "description")

        widgets = {
            'title': forms.TextInput(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150", "placeholder": "e.g John Snow's 30th Birthday"}),
            'category': forms.Select(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150"}),
            'image': forms.FileInput(attrs={"class": "w-[0.1px] h-[0.1px] opacity-0 overflow-hidden absolute -z-[1]"}),
            'content': TinyMCE(attrs={"class": "block p-3 md:text-base w-full text-sm text-custom-h outline-none placeholder:text-gray-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-custom-primary focus:border-custom-primary ease-linear transition-all duration-150", "rows": 8}),
        }