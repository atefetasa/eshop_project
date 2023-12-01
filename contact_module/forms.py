from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی', max_length=50, error_messages={
        'required': 'لطفا نام و نام خانوادگی خود را وارد کنید.',
        'max_length': 'نام و نام خانوادگی نمیتواند بیش تر از ۵۰ کاراکتر باشد.'
    }, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}))

    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ایمیل'
    }))

    title = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'عنوان'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'پیغام شما',
        'id': 'message'
    }), label='متن پیام')


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'message', 'email', 'full_name']

        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما'
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری میباشد. لطفا وارد کنید.'
            }
        }


class ProfileForm(forms.Form):
    user_image = forms.FileField()