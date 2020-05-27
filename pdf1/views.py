from .models import Book
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import BookForm
from django.db.models import Q

class BookListView(ListView):
    model = Book
    template_name = 'index.html'
    paginate_by = 3

class AddBookView(CreateView):
    model = Book
    form_class = BookForm

    success_url = reverse_lazy('home')
    template_name = 'addbook.html'



class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(Title__icontains=query) | Q(Author__icontains=query)
        )
        return object_list
