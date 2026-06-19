from django.shortcuts import render,redirect
from .models import Blog

# Create your views here.
def home(request):
    blog=Blog.objects.all().order_by('-created_at')
    data={'blog':blog}
    return render(request,'home.html',data)




def view_blog(request,id):
   blog=Blog.objects.get(id=id)
   data={'blog':blog}
   return render(request,'view.html',data)

def create_blog(request):
    if request.method=='POST':
     title=request.POST.get('title')
     description=request.POST.get('description')
     Blog(title=title,description=description).save()
     return redirect('home')
    
    return render (request,'create.html')


def edit_blog(request,id):
    blog=Blog.objects.get(id=id)
    data={'blog':blog}
    if request.method == 'POST':
       blog.title=request.POST.get('title')
       blog.description=request.POST.get('description')
       blog.save()
       return redirect('home')
    
    return render(request,'edit.html',data)

def delete_blog(request,id):
    blog=Blog.objects.get(id=id)
    data={'blog':blog}
    if request.method=='POST':
       blog.delete()
       return redirect('home')
    return render(request,'delete.html',data)