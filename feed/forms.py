from django import forms

from . import models

class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    title = forms.CharField(
        label='Titre',
        label_suffix='',
        max_length=128,
        widget=forms.TextInput(attrs={'size': '70'})
    )
    description = forms.CharField(
        label_suffix='',
        label='Description', max_length=2048, required=False,
        widget=forms.Textarea(attrs={'rows': '10', 'cols': '70'})
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'value': 'Télécharger fichier'}),
        error_messages={
            'missing' : 'Aucune image choisie',
            'required' : 'Aucune image choisie',
            'empty' : 'Aucune image choisie',
            'invalid' : 'Le fichier choisi est invalide',
            'invalid_image' : 'Le fichier choisi est invalide',
        },
        label_suffix='',
        label='Image',
        required=True
    )

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']

class ReviewForm(forms.ModelForm):
    RATINGS = [('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    headline = forms.CharField(
        label='Titre',
        label_suffix='',
        max_length=128,
        widget=forms.TextInput(attrs={'size': '70'})
    )
    rating = forms.ChoiceField(
        label='Note',
        label_suffix='',
        widget=forms.RadioSelect, choices=RATINGS
    )
    body = forms.CharField(
        label='Commentaire',
        label_suffix='',
        max_length=8192,
        required=False,
        widget=forms.Textarea(attrs={'rows': '10', 'cols': '70'})
    )

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']