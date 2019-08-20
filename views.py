from django.http import HttpResponse
from fakestagram import views
from datetime import datetime

def hello_world(request):
    now = datetime.now()
    return HttpResponse('La hora actual en el servidor es: {now}'.format(now=str(now)))


def hi(request):
    import pdb; pdb.set_trace()
    return HttpResponse('Hi!')