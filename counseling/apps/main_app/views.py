from django.shortcuts import render
from django.views import View
from django.conf import settings

def media_admin(request):
    return {'media_url':settings.MEDIA_URL,}


class MainView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"main_app/index.html")
    
