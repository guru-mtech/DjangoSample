"""tweetme2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tweet.views import home_page,tweet_detial_view,tweet_list,tweet_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet-create/', tweet_create_view),
    path('',home_page),
    path('global/',tweet_list),  
    path('tweet/<int:tweet_id>',tweet_detial_view),
]

