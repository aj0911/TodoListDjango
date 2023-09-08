from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html',
        {
            'todos':{
                'django':'pending',
                'installation':'completed',
                'exercise':'done'
            },
            'username':'Abhinav Jha'
                
        }
    )