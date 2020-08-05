from django import forms


class Formulario(forms.Form):
    name = forms.CharField(
        label='Nombre',
        required=True,
        min_length=4,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Introduce tu nombre', 'size':10})
        )

    subject = forms.CharField(
        label='Asunto',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Motivo de consulta', 'size':50, 'value':''})
        )    

    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'sergio@correo.es',})
    )
    
    message = forms.CharField(
        label="Mensaje",
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Describe aquí tu consulta', 'title':'Comentario', 'rows':5}), 
        )