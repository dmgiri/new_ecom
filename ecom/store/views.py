from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "category_slug": category_slug,
    }

    # products = Product.objects.all().filter(available=True)
    # product_count = products.count()
    # context = {
    #     "products": products,
    #     "product_count": product_count,
    # }
    return render(request, "stores/store.html", context)