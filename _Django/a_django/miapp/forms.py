from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label="Titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ingresa titulo',
                'class': 'titulo_form_article'
            }
        ), validators=[
            validators.MinLengthValidator(4,'El titulo es demaciado corto !!'),
            validators.RegexValidator('^[A-Za-z0-9]*$', 'esta mal el titulo','invalid_title')
        ]
    ) 

    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,
        validators=[
            validators.MaxLengthValidator(20,'Excedistes numero de caracteres')
        ]
        
    )
    content.widget.attrs.update({
        'placeholder': 'ingresa contenido',
        'class': 'titulo_form_article',
        'id': 'contenido_id'
    })

    public_options = [
        (1,'si'),
        (0,'no')
    ]

    public = forms.TypedChoiceField(
        label = 'Publicado?',
        choices = public_options
    )
