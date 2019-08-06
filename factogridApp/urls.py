from django.urls import path
from factogridApp import views

urlpatterns = [
    path('', views.addequipment,name='index'),
    path('addEquip', views.addequipment,name='addequipment'),
    path('addEquipProp', views.addequipmentprop,name='addequipmentprop'),
    path('equipProp', views.equipPropData,name='equipPropData')
]
