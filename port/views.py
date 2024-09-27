from django.shortcuts import render
from .models import Contact,Post

# Create your views here.
def home(request):
    return render(request,'port/home.html')


def about(request):
    return render(request,'port/about.html')

def contact(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        phone=request.POST['phone']
        message=request.POST['message']
        print(email,name,phone,message)
        content=Contact(email=email,name=name,phone=phone,message=message)
        content.save()

    return render(request,'port/contact.html')

def service(request):
    allposts=Post.objects.all().order_by('-timestamp')
    context={"allposts":allposts}
    
    return render(request,'port/service.html',context)



def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}

    return render(request,'port/blogpost.html',context)