from django.shortcuts import render, redirect, get_object_or_404
from .models import Item,Form


def home(request):
    item1 = Item.objects.all()
    if request.method == 'POST':
        slno = request.POST.get('sl', '')
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        item = Item(slno=slno, name=name, desc=desc)
        item.save()
    return render(request, 'home.html', {'item': item1})

def delete(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request,id):
    item1 = Item.objects.get(id=id)
    if request.method == 'POST':
        slno = request.POST.get('sl', '')
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        Item.objects.filter(id=id).update(slno=slno, name=name, desc=desc)
        return redirect('/')

    return render(request, 'update.html', {'item': item1})

