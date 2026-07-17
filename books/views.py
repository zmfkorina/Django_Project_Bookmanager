from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm
from .models import Book


# Create your views here.

# functions that manage our web pages

def home(request: HttpRequest):
    return HttpResponse("Hello from our books app!")

#function-based view:
# CRUD - Create Read Update Delete -> patru actiuni de baza pt orice resursa web

def list_books(request):
    # Trebuie sa listam cartile din baza de date.
    # accesare de carti:
    books = Book.objects.all()

    return render(request, "books/home.html", context={"books": books})

def create_book(request: HttpRequest):
    if request.method == "POST":
        #detaliile cartii care au fost trimise de form folosing HTTP POST request se afla in request.POST, care e un dictionar
        book_instance = BookForm(request.POST)
        if book_instance.is_valid():
            #aici se creeaza o carte in baza de date
            book_instance.save()
            return redirect("create_book")
    else:
        #in cazul asta requestul poate fi GET, PUT, PATCH, DELETE, ETC
        form = BookForm()
        list1 = [10, 20, 30, 40]
        return render(request, "books/book_form.html", context={"form": form, "list1": list1})

def delete_book(request: HttpRequest, pk: int):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("home")
    else:
        return render(request, "books/book_confirm_delete.html", context={"book": book})
        


    # book.delete()
    # return redirect("home")