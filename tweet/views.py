from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
import random
from .forms import TweetForm

from .models import Tweet

# to render HomePage
def home_page(request , *args , **kwargs):
    return render(request,"pages/index.html",context={},status=200)

def tweet_create_view(request, *args , **kwargs):

    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()

        if next_url != None:
            return HttpResponseRedirect(next_url)
        form = TweetForm()
        
    return render(request,"components/form.html",context={"form" : form},status=200)


def tweet_detial_view(request , tweet_id ,*args , **kwards): 
    status = 200
    data = {
        "status" : status,
        "id" : tweet_id,
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.contant
    except:
        data["message"] = "Notfound"
        status = 404
    return JsonResponse(data)   


def tweet_list(request,*args,**kwargs): 
    querySet = Tweet.objects.all().reverse()
    allTweets = [{"id" : item.id,"content" : item.contant,"likes" : random.randint(0,1000)} for item in querySet]

    data = {
        "response" : allTweets,
        "status": 200,
    }

    return JsonResponse(data)