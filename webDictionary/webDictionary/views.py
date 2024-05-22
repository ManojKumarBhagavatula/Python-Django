from django.shortcuts import render
from django.http import JsonResponse
from .models import Word

def home(request):
    return render(request, 'homeSearch.html')


def search_word(request):
    search_query = request.GET.get('q', '').lower()
    try:
        word = Word.objects.get(word=search_query)
        result = word.meaning
    except Word.DoesNotExist:
        result = "Word not found."

    return JsonResponse({'result': result})

