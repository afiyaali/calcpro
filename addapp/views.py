from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showAddForm(request):
    return render(request,'addapp/addform.html')

def doAddForm(request):
    n1 = int(request.GET['n1'])
    n2 = int(request.GET['n2'])

    sum = n1+n2

    return render(request,'addapp/result.html',{'ans':sum})

def doMulForm(request):
    if request.method == 'POST':
        n1 = int(request.POST['n1'])
        n2 = int(request.POST['n2'])
        mul = n1*n2
        return render(request,'addapp/result1.html',{'ans':mul})

    else:
        return render(request,'addapp/multi.html')
   
