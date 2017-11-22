from django import forms

class ContactForm(forms.Form):
    Nombre = forms.CharField(label='Tu nombre', max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    Correo = forms.EmailField(label='Tu email',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'}))
    Asunto = forms.CharField(label='Asunto', max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Asunto'}))
    Mensaje = forms.CharField(label='Mensaje', max_length=500,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Mensaje'}))
