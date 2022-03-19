from .models import Category

def Linkes_categories(request):
    Linkes = Category.objects.all()
    return dict(Linkes_of_categories=Linkes)
