from django import forms
from rooms.models import RoomType, RoomContent, RoomApplication
from tinymce.widgets import TinyMCE

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ("cover_image", "title", "description", "number_of_rooms", "room_size")

        widgets = {
            'title': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'number_of_rooms': forms.NumberInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'room_size': forms.NumberInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'cover_image': forms.FileInput(attrs={"class": "w-[0.1px] h-[0.1px] opacity-0 overflow-hidden absolute -z-[1]"}),
            'description': TinyMCE(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text", "rows": 8}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = RoomApplication
        fields = (
            "applicant_first_name", "applicant_last_name", 
            "applicant_phone", "applicant_email", "applicant_identity_number", "applicant_gender",
            "relative_first_name", "relative_last_name", "relationship", 
            "relative_phone", "relative_email", "address_one", "city", 
            "country", "zipcode", "zipcode", "province")
        
        widgets = {
            'applicant_first_name': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'applicant_last_name': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'relative_first_name': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'applicant_identity_number': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'applicant_email': forms.EmailInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'relative_email': forms.EmailInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'relative_last_name': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'relationship': forms.Select(attrs={"class": "hidden"}),
            'relative_phone': forms.NumberInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text", "type": "tel"}),
            
            'applicant_gender': forms.Select(attrs={"class": "hidden"}),
            'province': forms.Select(attrs={"class": "hidden"}),
            'address_one': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'city': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'country': forms.TextInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            'zipcode': forms.NumberInput(attrs={"class": "bg-transparent px-[15px] w-full h-[50px] rounded-[15px] outline-0 border border-solid border-custom-bg text-sm text-custom-text"}),
            
            
        }