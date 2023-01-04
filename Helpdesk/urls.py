from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Categories', views.Categories)
router.register(r'TypeCategories', views.TypeCategories)
router.register(r'Priorites', views.Priorites)
router.register(r'Etats', views.Etats)
router.register(r'Tickets', views.Tickets)
router.register(r'Entites', views.Entites)







urlpatterns = [
    path('',include(router.urls)),
    path('GetCategorie/<int:pk>',views.GetCategorie),
    path('datahome/',views.GetDataHome),
    path('GetPiechartPriorite/',views.GetPiechartPriorite),
    path('GetStatistiquesPerYear/<int:year>',views.GetStatistiquesPerYear),
    path('getTicket/<pk>',views.getTicket.as_view()),
    path('getEntity/<pk>',views.getEntity.as_view()),
    path('Register/',views.Register.as_view()),


]