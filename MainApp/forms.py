from django.forms import ModelForm
from django.forms.widgets import Select, TextInput, Textarea
from MainApp.models import Snippet

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
        fields = ['name', 'lang', 'code']
        
        widgets = {
            'name': TextInput(attrs={"class": "form-control form-control-lg", 'placeholder': 'Название сниппета'}),
            'lang': Select(attrs={"class": "form-control form-control-lg"}, choices=LANGS),
            'code': Textarea(attrs={"class": "form-control form-control-lg"}),
        }
        
        labels = {
            'name': 'Название',
            'lang': 'Язык',
            'code': 'Код',
        }
