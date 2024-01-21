from .models import Category

def menu_links(request):  #Menu Category
   links = Category.objects.all()
   return dict(links=links) 