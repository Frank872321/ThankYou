from django.http import HttpResponse
from django.template import loader
from submit.models import Post

def Main(request):
    queryset = Post.objects.all()
    template = loader.get_template("index.html")
    return HttpResponse(template.render({'queryset': queryset}))
 