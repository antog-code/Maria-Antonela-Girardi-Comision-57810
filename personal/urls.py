from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('', home, name="home"),
  path('index/', index, name="index"),
  #path('experiencia/', experiencia, name="experiencia"),
  
  
  

  path('acerca/', acerca, name="acerca"),

  #----Formularios

  #--- Buscar / encontrarcontacto

  path('buscar/', buscarContacto, name="buscar"),
  path('contactoEncontrar/', contactoEncontrar, name="contactoEncontrar"),

  #---- Formacion
  path('formacion/', FormacionList.as_view(), name="formacion"),
  path('formacionAgregar/', FormacionAgregar.as_view(), name="formacionAgregar"),
  path('formacionUpdate/<int:pk>/', FormacionUpdate.as_view(), name="formacionUpdate"), 
  path('formacionDelete/<int:pk>/', FormacionDelete.as_view(), name="formacionDelete"),

    #---- Experiencia
  path('experiencia/', ExperienciaList.as_view(), name="experiencia"),
  path('experienciaAgregar/', ExperienciaAgregar.as_view(), name="experienciaAgregar"),


  # --- Proyectos
  path('proyectos/', ProyectosList.as_view(), name="proyectos"),
  path('proyectosAgregar/', ProyectosAgregar.as_view(), name="proyectosAgregar"),
  path('proyectosUpdate/<int:pk>/', ProyectosUpdate.as_view(), name="proyectosUpdate"),
  path('proyectosDelete/<int:pk>/', ProyectosDelete.as_view(), name="proyectosDelete"),


#--- Contacto
  path('contacto/', contacto, name="contacto"),
  path('contacto_list/', contacto_list, name="contacto_list"),
  path('contactoAgregar/', ContactoAgregar.as_view(), name="contactoAgregar"),
  path('contactoUpdate/<int:pk>/', ContactoUpdate.as_view(), name="contactoUpdate"),
  path('contactoDelete/<int:pk>/', ContactoDelete.as_view(), name="contactoDelete"),



#--- Login / Logout / Registration
  path('login/', loginRequest, name="login"),
  path ('logout', LogoutView.as_view(template_name="personal/logout.html"), name="logout" ),
  path('registro/', register, name="registro"),

  
#--- Edicion de perfil  / Avatar 
  path('perfil/', editProfile, name="perfil"),
  path('None/password/', CambiarClave.as_view(), name="cambiarClave"),
  path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]
