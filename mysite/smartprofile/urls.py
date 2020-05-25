from django.urls import path
from . import views
from django.urls import include, path
app_name ='smartprofile'
urlpatterns = [
    path('', views.index, name='index'),
    #path('add/', views.add_Household, name='add_Household'),
    path('add/', views.add_Household.as_view(), name='add_Household'),
    path('personal/', views.personalList, name='personalList'),
    path('hhdetail/<pk>/', views.HHDetailView, name='hhdetail'),
    path('householdupdate/<pk>/', views.householdupdate.as_view(), name='householdupdate'),
    path('householddelete/<pk>/', views.householddelete.as_view(), name='householddelete'),
    path('personaldetail/<pk>', views.personaldetail, name='personaldetail'),
    path('add_Personal/<pk>', views.add_Personal.as_view(), name='add_Personal'),
    path('personalupdate/<pk>', views.personalupdate.as_view(), name='personalupdate'),
    path('personaldelete/<pk>', views.personaldelete.as_view(), name='personaldelete'),
    path('export/', views.export, name='export'),
    path('import/', views.importData, name='importData'),
    path('map/', views.map, name='map'),
    path('excel/', views.ParseExcel.as_view(), name='ParseExcel'),
    path('housedata/', views.housedata, name='housedata'),
    path('HouseholdListJson/', views.HouseholdListJson.as_view(), name='HouseholdListJson'),



]
