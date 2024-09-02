from django.shortcuts import render
from .models import Post


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('class') and request.POST.get('content'):
                post=Post()
                post.name = request.POST.get('name')
                post.yourclass = request.POST.get('class')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'main.html')  

        else:
                return render(request,'main.html')
