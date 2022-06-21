from django import forms

from . import models

class UserFollowsForm(forms.ModelForm):
    # followed_user = forms.CharField(
    #     label='',
    #     label_suffix='',
    #     max_length=128,
    #     widget=forms.TextInput(attrs={'size': '70', 'placeholder': 'Nom d\'utilisateur'})
    # )
    class Meta:
        model = models.UserFollows
        fields = ['followed_user']