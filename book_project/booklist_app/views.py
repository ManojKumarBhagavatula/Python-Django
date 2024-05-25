from django.shortcuts import get_object_or_404, render,redirect
from booklist_app.models import Books
from .models import Books
from .forms import BookForm


# Create your views here.

def book_list(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'books': books} )

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Books.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'add_book.html')

def edit_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})  

def delete_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})