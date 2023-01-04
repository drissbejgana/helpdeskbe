from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from django.db.models import Count
from django.db.models import F
from django.contrib.auth import authenticate

# Create your views here.
# from .forms import Ticketform


## is_superuser == is admin
## ListTicketSerializer gives Ticket with specifie data 
## Tickets gives Ticket without specifie data 


class Tickets(viewsets.ModelViewSet):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    def list(self,request):
        user=request.user
        if request.method == 'GET':
            if user.is_superuser: 
             Tickets=Ticket.objects.all()
            else:
             Tickets=Ticket.objects.filter(user=user.id)
            serializer=ListTicketSerializer(Tickets,many=True)
        return Response(serializer.data)


class getTicket(generics.RetrieveAPIView):
   
    queryset = Ticket.objects.all()
    serializer_class = ListTicketSerializer


## CRUD Categories
class Categories(viewsets.ModelViewSet):
    
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
 
@api_view(['GET'])
def GetCategorie(request,pk):
    if request.method=='GET':
        cat=Typecategorie.objects.get(id=pk)
        p=cat.Typecat_cat.all()
        serializer=CategorieSerializer(p,many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)   

## CRUD TypeCategories
class TypeCategories(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = Typecategorie.objects.all()
    serializer_class = TypeCategorieSerializer

## CRUD Priorites
class Priorites(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Priorite.objects.all()
    serializer_class=PrioriteSerializer

## CRUD Etats
class Etats(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Etat.objects.all()
    serializer_class=EtatSerializer


   


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetDataHome(request):
     if request.method=='GET':
        datahome={}
        if request.user.is_superuser:
              datahome['ListAllTicket']=Ticket.objects.all()
              datahome['ListTicketEnregistree']=Ticket.objects.filter(etat=1)
              datahome['ListEtatPieChartTicket']=Ticket.objects.values('etat__namefr','etat__etatclass').annotate(name=F('etat__namefr'),objetclass=F('etat__etatclass'),total=Count('etat')).values('name','objetclass','total')
        else :
              print(request.user.id)
              datahome['ListAllTicket']=Ticket.objects.filter(user=request.user.id)
              datahome['ListTicketEnregistree']=Ticket.objects.filter(etat=1,user=request.user.id)
              datahome['ListEtatPieChartTicket']=Ticket.objects.filter(user=request.user.id).values('etat__namefr','etat__etatclass').annotate(name=F('etat__namefr'),objetclass=F('etat__etatclass'),total=Count('etat')).values('name','objetclass','total')


        datahome['ListPriorite']=Priorite.objects.all()
        datahome['EtatClass']=Etat.objects.all()
        
        serializer=HomeDataSerializer(datahome)
       
        return Response(serializer.data)

     return Response(status=status.HTTP_404_NOT_FOUND) 




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetPiechartPriorite(request):
    if request.method=='GET':
        data={}
        if request.user.is_superuser:
            data['listPriorite']=Ticket.objects.values('priorite__namefr','priorite__prioriteclass').annotate(name=F('priorite__namefr'),objetclass=F('priorite__prioriteclass'),total=Count('priorite')).values('name','objetclass', 'total')
        else :
            data['listPriorite']=Ticket.objects.filter(user=request.user.id).values('priorite__namefr','priorite__prioriteclass').annotate(name=F('priorite__namefr'),objetclass=F('priorite__prioriteclass'),total=Count('priorite')).values('name','objetclass', 'total')
           
        serializer=StatistiquesSerializer(data)
        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND) 



@api_view(['GET'])
@permission_classes([IsAdminUser])
def GetStatistiquesPerYear(request,year):
    if request.method=='GET':
        data={}
        data['listPriorite']=Ticket.objects.filter(datecreation__year=year).values('priorite__namefr','priorite__prioriteclass').annotate(name=F('priorite__namefr'),objetclass=F('priorite__prioriteclass'),total=Count('priorite')).values('name','objetclass', 'total')
        data['listEtat']=Ticket.objects.filter(datecreation__year=year).values('etat__namefr','etat__etatclass').annotate(name=F('etat__namefr'),objetclass=F('etat__etatclass'),total=Count('etat')).values('name','objetclass', 'total')
        data['listCategorie']=Ticket.objects.filter(datecreation__year=year).values('categorie__namefr').annotate(name=F('categorie__namefr'),total=Count('categorie')).values('name', 'total')
        data['listTypeCategorie']=Ticket.objects.filter(datecreation__year=year).values('typecategorie__namefr').annotate(name=F('typecategorie__namefr'),total=Count('typecategorie')).values('name','total')
        data['listTicket']=Ticket.objects.values('datecreation__year').annotate(name=F('datecreation__year'),total=Count('id')).values('name','total')
        data['listTicketPerMonth']=Ticket.objects.filter(datecreation__year=year).values('datecreation__month').annotate(name=F('datecreation__month'),total=Count('id')).values('name','total')
        data['listTicketEntite']=Ticket.objects.filter(datecreation__year=year).values('user__entite__namefr').annotate(name=F('user__entite__namefr'),total=Count('id')).values('name','total')
        data['Top5User']=Ticket.objects.filter(datecreation__year=year).values('user__username').annotate(name=F('user__username'),total=Count('id')).values('name','total').order_by('-total')[:5]
        data['Top5Entite']=Ticket.objects.filter(datecreation__year=year).values('user__entite__namefr').annotate(name=F('user__entite__namefr'),total=Count('id')).values('name','total').order_by('-total')[:5]
       
        serializer=StatistiquesSerializer(data)
        return Response(serializer.data)
       
    return Response(status=status.HTTP_404_NOT_FOUND) 


class Entites(viewsets.ModelViewSet):
    serializer_class=EntiteSerializer
    queryset=Entite.objects.all()

class getEntity(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Entite.objects.all()
    serializer_class=EntiteSerializer

class Register(generics.CreateAPIView):
     queryset=User.objects.all()
     serializer_class=UserSerializer