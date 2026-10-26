from django.shortcuts import render,redirect
from .models import TodoModel,CompleteModel,TrashModel

# Create your views here.

def home(request):
    data = TodoModel.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        TodoModel.objects.create(
            title = title,
            desc = desc
        )
        return redirect('home')
    return render(request,'add.html')

def complete(request):
    data = CompleteModel.objects.all()

    return render(request,'complete.html',{'data':data})

def trash(request):
    data = TrashModel.objects.all()
    return render(request,'trash.html',{'data':data})

def about(request):
    return render(request,'about.html')


def update(request,pk):
    data = TodoModel.objects.get(id=pk)
    
    if request.method == 'POST':
            title = request.POST['title']
            desc = request.POST['desc']

            

            data.title = title
            data.desc = desc
            data.save()
            return redirect('home')

    

    return render(request,'update.html',{'data':data})



def hcomplete(request,pk):
    data = TodoModel.objects.get(id=pk)
    CompleteModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('complete')

def hdelete_all(request):
    data = TodoModel.objects.all()

    for i in data:
        TrashModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()

    return redirect('home')

def hcomplete_all(request):
    data = TodoModel.objects.all()
    for i in data:
        CompleteModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('home')

def hdelete_all(request):
    data = TodoModel.objects.all()
    for i in data:
        TrashModel.objects.create(
            title  = i.title,
            desc = i.desc
        )
        i.delete()
        return redirect('home')


def crestore(request,pk):
    data = CompleteModel.objects.get(id=pk)
    TodoModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('complete')


def cdelete(request,pk):
    data = CompleteModel.objects.get(id=pk)
    TrashModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('complete')

def crestore_all(request):
    data = CompleteModel.objects.all()
    for i in data:
        TodoModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('complete')

def cdelete_all(request):
    data = CompleteModel.objects.all()
    for i in data:
        TrashModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('complete')

def trestore(request,pk):
    data = TrashModel.objects.get(id = pk)
    TodoModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('trash')


def tdelete(request, pk):
    data = TrashModel.objects.get(id=pk)
    data.delete()
    return redirect('trash')



def trestore_all(request):
    data = TrashModel.objects.all()
    for i in data :
        TodoModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('trash')

def tdelete_all(request):
    data = TrashModel.objects.all().delete()
    return redirect('trash')
