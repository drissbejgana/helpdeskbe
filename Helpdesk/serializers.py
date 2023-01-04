

from lib2to3.pytree import Base
from rest_framework import serializers
from .models import *
from django.utils.timezone import now



class TypeCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Typecategorie
        fields='__all__'


class CategorieSerializer(serializers.ModelSerializer):
    typecategorie=TypeCategorieSerializer()
    class Meta:
        model=Categorie
        fields=['id','namefr','typecategorie']
        



class PrioriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Priorite
        fields='__all__'


class EtatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Etat
        fields='__all__'

class EntiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Entite
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'


class ListTicketSerializer(serializers.ModelSerializer):
    categorie=CategorieSerializer()
    priorite=PrioriteSerializer()
    etat=EtatSerializer()
    user=UserSerializer()
    ticketimage = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    
    class Meta:
        model=Ticket
        fields='__all__'




class TicketSerializer(serializers.ModelSerializer):
     
    ticketimage = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model=Ticket
        fields='__all__'
    
    # def validate(self, data):
    #     if data.get('objet')!="aaa":
    #         raise serializers.ValidationError("Errror")
    #     else :
    #      return data

 


class ChartTicketSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=55)
    total=serializers.IntegerField()
    objetclass=serializers.CharField(max_length=55,allow_blank=True,allow_null=True)



class HomeDataSerializer(serializers.Serializer):
    ListAllTicket=ListTicketSerializer(read_only=True, many=True)
    ListEtatPieChartTicket=ChartTicketSerializer(read_only=True,many=True)
    ListTicketEnregistree=ListTicketSerializer(read_only=True, many=True)
    ListPriorite=PrioriteSerializer(read_only=True, many=True)
    EtatClass=EtatSerializer(read_only=True, many=True)


class StatistiquesSerializer(serializers.Serializer):
    listPriorite=ChartTicketSerializer(read_only=True, many=True)
    listEtat=ChartTicketSerializer(read_only=True, many=True)
    listCategorie=ChartTicketSerializer(read_only=True, many=True)
    listTypeCategorie=ChartTicketSerializer(read_only=True, many=True)
    listTicket=ChartTicketSerializer(read_only=True,many=True)
    listTicketPerMonth=ChartTicketSerializer(read_only=True,many=True)
    Top5User=ChartTicketSerializer(read_only=True,many=True)
    listTicketEntite=ChartTicketSerializer(read_only=True,many=True)
    Top5Entite=ChartTicketSerializer(read_only=True,many=True)