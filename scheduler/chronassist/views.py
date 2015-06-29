from django.shortcuts import render
from chronassist.models import Item
from chronassist.forms import ItemForm

# Create your views here.
def index(request):
    new_item_text = None
    if(request.method == 'POST'):
        new_item_text = request.POST.get('item_text','')
        return render(request,
                      'chronassist/base.html',
                      {'new_item_text': new_item_text})
    return render(request, 'chronassist/base.html', {'new_item_text': new_item_text})