from django import forms

from authentication.models import User
from . import models

class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['followed_user']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        followed_users = models.UserFollows.objects.filter(user=user)
        users_id = [user.id]
        for user1 in followed_users:
            users_id += [user1.followed_user.id]
        self.fields['followed_user'].queryset = User.objects.exclude(id__in=users_id)