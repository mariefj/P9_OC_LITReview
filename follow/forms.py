from django import forms

from . import models

class UserFollowsForm(forms.ModelForm):
    # followed_user = forms.ModelMultipleChoiceField(
    #     queryset=None,
    #     label='',
    #     label_suffix=''
    # )
    class Meta:
        model = models.UserFollows
        fields = ['followed_user']

    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['followed_user'].queryset = models.UserFollows.objects.exclude(user=user)
    #     print('QUERY ', self.fields['followed_user'].queryset)