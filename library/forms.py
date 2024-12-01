from django import forms
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator, MinLengthValidator
from django.forms.utils import ErrorList


class BookForm(forms.Form):
    book_id = forms.CharField(max_length=255, label='Id książki')
    isbn = forms.CharField(max_length=255, label='Numer ISBN')
    authors = forms.CharField(max_length=255, label='Podaj autorów')
    original_publication_year = forms.DateField(label='Pierwsza data publikacji')
    original_title = forms.CharField(max_length=255, label='Tytuł oryginalny')
    small_image_url = forms.URLField(max_length=255, label='Link do okładki')
    genres = forms.CharField(label='Gatunek', max_length=55,
                                     validators=[MinLengthValidator(3)])
    short_description = forms.CharField(label='Krótki opis książki', validators=[MinLengthValidator(10)],
                               widget=forms.Textarea(attrs={'rows': 3}))


    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'uk-input uk-margin-small-bottom'
