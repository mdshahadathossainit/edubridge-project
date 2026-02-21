from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=Profile.USER_TYPES,  
        required=True,
        label="User type",
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()


        user_profile = Profile.objects.create(user=user)
        user_profile.user_type = self.cleaned_data.get('user_type')
        if commit:
            user_profile.save()

        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
