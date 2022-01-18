from django.shortcuts import render
from bmstu_lab4.models import Film
from django.http import HttpResponse
# Create your views here.


def Hello(req):
    return render(req, 'sorts.html', {
        'data': {
            'title_page': 'bmstu lab4',
        },
        'films': Film.objects.all()



    })


def ice(req, id):
    img = req.GET.get("img", "")
    return render(req, 'ice.html', {
        'data': {
            'film': Film.objects.filter(id=id)[0],
            'img': 'img/'+img
        }
    })