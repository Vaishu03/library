# Import necessary modules and classes from Django
from django.shortcuts import render
from django.shortcuts import redirect

# Import the Book model and BookForm from the current app i.e libi
from .forms import BookForm
from .models import Book

# Define the index view function for adding new record to the database
def index(request):

    # Check if the request method is POST
    if request.method == "POST":
        # Create a BookForm instance with the POST data
        form = BookForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            try:
                # Save the form data to the database
                form.save()
                return redirect('/show') # Redirect to the 'show' page after successful form submission
            except:
                pass
    # If the request method is not POST, create an empty BookForm instance
    else:
        form = BookForm()
    # Render the 'index.html' template with the form
    return render(request,'index.html',{'form':form})

# Define the show view function for displaying all books
def show(request):
    books = Book.objects.all() # Retrieve all books from the database
    # Render the 'show.html' template with the list of books
    return render(request,"show.html",{"books":books})

# Define the edit view function for editing a specific book
def edit(request,ISBN):
    book=Book.objects.get(ISBN=ISBN) # Retrieve the book with the given ISBN from the database
    # Render the 'edit.html' template with the book details
    return render(request,'edit.html',{'book':book})

# Define the update view function for updating a specific book
def update(request,ISBN):
    book=Book.objects.get(ISBN=ISBN) # Retrieve the book with the given ISBN from the database
     # Create a BookForm instance with the data using post method and the book instance
    form = BookForm(request.POST,instance=book)

    if form.is_valid(): # Check if the form is valid
        form.save() # Save the updated form data to the database
        # Redirect to the 'show' page after successful form submission
        return redirect("/show")
    
    # Render the 'edit.html' template with the book details
    return render(request,'edit.html',{'book':book})

# Define the destroy view function for deleting a specific book
def destroy(request,ISBN):
    book=Book.objects.get(ISBN=ISBN) # Retrieve the book with the given ISBN from the database
    # Delete the book from the database
    book.delete()

    # Redirect to the 'show' page after successful deletion
    return redirect("/show")
        