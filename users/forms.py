from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=Profile.USER_TYPES, required=True)
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.user_type = self.cleaned_data.get('user_type')
            if self.cleaned_data.get('image'):
                profile.image = self.cleaned_data.get('image')
            profile.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
