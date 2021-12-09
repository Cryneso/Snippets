from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput, ValidationError
from django.forms.widgets import CheckboxInput, Select
from MainApp.models import Comment, Snippet

LANGS = (
    ('python', 'Python'),
    ('java', 'Java'),
    ('php', 'PHP'),
    ('cs', 'C#'),
)

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'public']
        
        widgets = {
            'name': TextInput(attrs={"class": "form-control form-control-lg", 'placeholder': 'Название сниппета'}),
            'lang': Select(attrs={"class": "form-control form-control-lg"}, choices=LANGS),
            'code': Textarea(attrs={"class": "form-control form-control-lg"}),
            'puplic': CheckboxInput(attrs={"class": "form-control"}),
        }
        
        labels = {
            'name': 'Название',
            'lang': 'Язык',
            'code': 'Код',
            'public': 'Публичный сниппет',
        }
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
       
    widgets = {
            'text': Textarea(attrs={"class": "form-control form-control-lg"}),
        }  
    
    labels = {
            'text': '',
        } 
       

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    password1 = CharField(label="password", widget=PasswordInput)
    password2 = CharField(label="password confirm", widget=PasswordInput)

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise ValidationError("Пароли не совпадают или пустые")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user