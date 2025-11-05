from django.shortcuts import get_object_or_404, render
from categories.models import Categories

# Create your views here.

def categories_view(request):

    context = {'categories': Categories.objects.all()}
    return render(request, 'categories.html', context)

def category_detail_view(request, category_id):
    category = get_object_or_404(Categories, pk=category_id)
    products = category.products.all()
    context = {
        'category': category,
        'products': products,
    }
    return render (request, 'products.html', context)
