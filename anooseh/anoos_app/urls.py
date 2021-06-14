"""anooseh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from anoos_app import views, viewcounty

urlpatterns = {
    path('postfiends', views.addfreiendview),
    path('update/<int:pk>', views.viewupdateFriend),
    path('delete/<int:pk>', views.deleteFriendView),
    path('getone/<int:pk>', views.FriendsgetByIdview),
    path('getAll', views.FriendsgetAllView),
    path('updateparam/<int:pk>', views.updateparamfriendview),

    #####country######
    path('postcountry', viewcounty.addcountryview),
    path('deletecountry/<int:pk>', viewcounty.countrydeleteview),



    # new test name
    path('addname', views.addnameview),
    path('getnameandlast/<int:pk>', views.getview)
}