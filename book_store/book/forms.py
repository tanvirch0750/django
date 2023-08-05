from book.models import BookStoreModel

from django import forms


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        exclude = ['last_pub', 'first_pub']