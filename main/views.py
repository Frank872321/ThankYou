from django.http import HttpResponse
from django.template import loader
from submit.models import Post

def Main(request):
    queryset = Post.objects.all()
    some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    template = loader.get_template("index.html")
    return HttpResponse(template.render({'queryset': queryset}, {'some_list': some_list}))
 