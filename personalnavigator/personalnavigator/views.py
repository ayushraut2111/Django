from django.http import HttpResponse

def nav1(request):
    return HttpResponse('<h1>Ayush</h1><a href="https://github.com">Github</a>')
def nav2(request):
    return HttpResponse('<h1>Ayush</h1><a href="https://youtube.com">youtube</a>')
def nav3(request):
    return HttpResponse("<h1>From here write the url above at the url bar to redirect to another pages</h1>")