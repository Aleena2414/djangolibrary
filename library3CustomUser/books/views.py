from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from books.models import Book



# Create your views here.
def home(request):
    context={'name':'Aleena','Age':'21'}
    return render(request,'home.html',context)
@login_required
def add(request):
    if(request.method=='POST'):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pr=request.POST['pr']
        l=request.POST['l']

        c=request.FILES['i']
        f=request.FILES.get('f')

        b=Book.objects.create(title=t,author=a,page=p,price=pr,language=l,cover=c,pdf=f) #create an new record
        b.save()   #save the record inside table
        return view(request)
    return render(request,'add.html')
@login_required
def view(request):
    # k=con.execute('select * from Book')
    k=Book.objects.all() #read all records from table Book and assigns it to k
    return render(request,'view.html',{'book':k})
@login_required
def detail(request,p):
    k=Book.objects.get(id=p)
    return render(request,'detail.html',{'book':k})
@login_required
def edit(request,p):
    k = Book.objects.get(id=p)
    if (request.method =="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['pr']
        k.page=request.POST['p']
        k.language=request.POST['l']

        if(request.FILES.get('c')==None):
            k.save()
        else:
            k.cover=request.FILES.get('c')

        if (request.FILES.get('f') == None):
            k.save()
        else:
            k.pdf = request.FILES.get('f')
        k.save()
        return view(request)


    return render(request,'edit.html',{'book':k})
@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return view(request)
def search(request):
    k=None
    if(request.method=="POST"):
        query=request.POST['q']
        print(query)
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)) #it check the key in title and author field in every records.#filter function retruns only the matching records.
            print(k)
    return render(request,'search.html',{'book':k})