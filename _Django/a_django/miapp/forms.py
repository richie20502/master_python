from django import forms

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
        )
    ) 

    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea(
            attrs={
                'placeholder': 'ingresa contenido',
                'class': 'titulo_form_article'
            }
        )
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
