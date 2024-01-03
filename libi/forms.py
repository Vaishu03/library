# Import necessary modules
from django import forms 
from .models import Book

# Define a form class for the Book model
class BookForm(forms.ModelForm):

    # Meta class provides additional information about the form
    class Meta:
        model = Book # Specifying the model for which the form is created
        fields = '__all__' # Include all fields from the Book model in the form