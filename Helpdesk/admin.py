from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Categorie)
admin.site.register(Elements)
admin.site.register(Entite)
admin.site.register(Etat)
admin.site.register(Message)
admin.site.register(Priorite)
admin.site.register(Ticket)
admin.site.register(Typecategorie)
admin.site.register(Typeelement)
admin.site.register(Typeentite)
admin.site.register(User)
