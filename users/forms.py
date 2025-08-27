from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile  # Profile মডেলটি ইমপোর্ট করা হয়েছে


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class RegistrationForm(UserCreationForm):
    # RegistrationForm-এ নতুন user_type ফিল্ডটি যোগ করা হয়েছে
    user_type = forms.ChoiceField(
        choices=Profile.USER_TYPES,  # এখানে Profile.USER_TYPES ব্যবহার করা হয়েছে
        required=True,
        label="ইউজারের ধরণ",
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        # UserCreationForm এর ডিফল্ট save() মেথডটি override করা হয়েছে
        # প্রথমে User মডেলটি সেভ করা হয়
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()

        # User সেভ করার পর Profile মডেলটি তৈরি বা আপডেট করা হয়
        user_profile = Profile.objects.create(user=user)
        user_profile.user_type = self.cleaned_data.get('user_type')
        if commit:
            user_profile.save()

        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
