from abc import ABC
from multiprocessing.dummy import Manager
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

from project.settings import AUTH_USER_MODEL



class User(AbstractUser):  
    email=models.EmailField(verbose_name='email',max_length=255,unique=True)
    entite=models.ForeignKey('Entite',related_name='user_entite',on_delete=models.CASCADE,null=True,blank=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username','first_name','last_name','entite','is_staff','is_superuser']   
    USERNAME_FIELD = 'email'
   

    def get_username(self):
        return self.username

        




class Categorie(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namefr = models.CharField(db_column='NameFr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='NameAr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    typecategorie = models.ForeignKey('Typecategorie', models.DO_NOTHING,related_name='Typecat_cat',db_column='TypeCategorie_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta: 
        db_table = 'Categorie'

    def __str__(self):
        return self.namefr

class Elements(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namefr = models.CharField(db_column='NameFr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='NameAr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    typeelement = models.ForeignKey('Typeelement', models.DO_NOTHING,related_name='Elem_tyelem', db_column='IdTypeElement', blank=True, null=True)  # Field name made lowercase.
    descriptionfr = models.TextField(db_column='DescriptionFr',  blank=True, null=True)  # Field name made lowercase.
    descriptionar = models.TextField(db_column='DescriptionAr',  blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Elements'

    def __str__(self) -> str:
        return self.namefr   

class Entite(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namefr = models.CharField(db_column='NameFr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='NameAr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    shortename = models.CharField(db_column='ShorteName', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    entiteparrent = models.IntegerField(db_column='IdEntiteParrent', blank=True, null=True)  # Field name made lowercase.
    typeentite = models.ForeignKey('Typeentite', models.DO_NOTHING, db_column='IdTypeEntite', blank=True, null=True)  # Field name made lowercase.
    entiteparrent = models.ForeignKey('self', models.DO_NOTHING, db_column='EntiteParrent_Id', blank=True, null=True)  # Field name made lowercase.
    user=models.ForeignKey(AUTH_USER_MODEL,related_name='entite_user',on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'Entite'

    def __str__(self) -> str:
        return self.namefr   

class Etat(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namefr = models.CharField(db_column='NameFr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='NameAr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.
    etatcolor = models.CharField(db_column='EtatColor', max_length=20,  blank=True, null=True)  # Field name made lowercase.
    etatclass = models.CharField(db_column='EtatClass', max_length=20,  blank=True, null=True)  # Field name made lowercase.
    etatorder = models.IntegerField(db_column='EtatOrder')  # Field name made lowercase.


    class Meta:
        db_table = 'Etat'

    def __str__(self) -> str:
        return self.namefr   

class Message(models.Model):
    idmessage = models.IntegerField(db_column='IdMessage', primary_key=True)  # Field name made lowercase.
    messagetext = models.TextField(db_column='MessageText', )  # Field name made lowercase.
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING,related_name='Tickets_msg', db_column='IdTicket')  # Field name made lowercase.
    user=models.ForeignKey(AUTH_USER_MODEL,related_name='message_user',on_delete=models.CASCADE)

    class Meta:
        db_table = 'Message'

    def __str__(self) -> str:
        return self.idmessage   

class Priorite(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namefr = models.CharField(db_column='NameFr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='NameAr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.
    prioritecolor = models.CharField(db_column='PrioriteColor', max_length=20,  blank=True, null=True)  # Field name made lowercase.
    prioriteclass = models.CharField(db_column='PrioriteClass', max_length=20,  blank=True, null=True)  # Field name made lowercase.
    prioriteorder = models.IntegerField(db_column='PrioriteOrder')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Priorite'

    def __str__(self) -> str:
        return self.namefr   

class Ticket(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    objet = models.CharField(db_column='Objet', max_length=150, )  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=400, )  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=400,  blank=True, null=True)  # Field name made lowercase.
    mesureaprendre = models.CharField(db_column='MesureAprendre', max_length=400,  blank=True, null=True)  # Field name made lowercase.
    supplementaire = models.CharField(db_column='Supplementaire', max_length=400,  blank=True, null=True)  # Field name made lowercase.
    ticketimage = models.ImageField(upload_to="media/images/%y/%m/%d",db_column='TicketImage', max_length=400, blank=True, null=True)  # Field name made lowercase.
    dateouverture = models.DateTimeField(db_column='DateOuverture', blank=True, null=True)  # Field name made lowercase.
    datemodifier = models.DateTimeField(db_column='DateModifier', blank=True, null=True,auto_now=True)  # Field name made lowercase.
    datecreation = models.DateTimeField(db_column='DateCreation', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    categorie = models.ForeignKey(Categorie, models.DO_NOTHING,related_name='Tickets_cat',db_column='IdCategorie', blank=True, null=True)  # Field name made lowercase.
    typecategorie = models.IntegerField(db_column='IdTypeCategorie', blank=True, null=True)  # Field name made lowercase.
    etat = models.ForeignKey(Etat, models.DO_NOTHING,related_name='etat',db_column='IdEtat', blank=True, null=True)  # Field name made lowercase.
    priorite = models.ForeignKey(Priorite, models.DO_NOTHING,related_name='Tickets_pri', db_column='IdPriorite', blank=True, null=True)  # Field name made lowercase.
    element = models.ForeignKey(Elements, models.DO_NOTHING,related_name='Tickets_ele',db_column='IdElement', blank=True, null=True)  # Field name made lowercase.
    typecategorie = models.ForeignKey('Typecategorie',models.DO_NOTHING,related_name='Tickets_tycat', db_column='TypeCategorie_Id', blank=True, null=True)  # Field name made lowercase.
    user=models.ForeignKey(AUTH_USER_MODEL,related_name='ticket_user',on_delete=models.CASCADE)
   
    class Meta:
       
        db_table = 'Ticket'

    def __str__(self) -> str:
        return self.objet     


class Typecategorie(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namefr = models.CharField(db_column='NameFr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='NameAr', max_length=100,  blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'TypeCategorie'

    def __str__(self) -> str:
        return self.namefr   

class Typeelement(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namefr = models.CharField(db_column='NameFr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='NameAr', max_length=100,  blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'TypeElement'

    def __str__(self) -> str:
        return self.namefr   

class Typeentite(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namefr = models.CharField(db_column='NameFr', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    namear = models.CharField(db_column='NameAr', max_length=100,  blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'TypeEntite'

    def __str__(self) -> str:
        return self.namefr           


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, )
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)

    def __str__(self) -> str:
        return self.name   





