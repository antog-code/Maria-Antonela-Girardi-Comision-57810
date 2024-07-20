from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy

from .forms import*

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin #trabajan sobre las clases
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, "personal/index.html")

def index(request):
    return render(request, "personal/index.html")

def formacion(request):
    contexto = {"formacion": Estudios.objects.all(),}
    return render(request, "personal/formacion.html", contexto)

def experiencia(request):
    contexto = {"experiencia": Experiencia.objects.all()}
    return render(request, "personal/experiencia.html", contexto)



def coworking(request):
    contexto = {"coworking": ContactoCoworking.objects.all()}
    return render(request, "personal/coworking.html", contexto)



def acerca(request):
    return render(request, "personal/acerca.html")


#___ Formularios


#--- Proyectos

class ProyectosList(ListView):
    model = Proyectos

class ProyectosAgregar(LoginRequiredMixin, CreateView):
    model = Proyectos
    fields = ["nombre","fecha","descripcion","imagen"]
    success_url = reverse_lazy("proyectos")

class ProyectosUpdate(LoginRequiredMixin, UpdateView):
    model = Proyectos
    fields = ["nombre","fecha","descripcion","imagen"]
    success_url = reverse_lazy("proyectos")
    def form_valid(self, form):
        return super().form_valid(form)

class ProyectosDelete(LoginRequiredMixin, DeleteView):
    model = Proyectos
    success_url = reverse_lazy("proyectos")


#--- Contacto

@login_required
def contacto_list(request):
    contexto = {"contacto_list": Contacto.objects.all()}
    return render(request, "personal/contacto_list.html", contexto)

class ContactoAgregar(CreateView):
    model = Contacto
    fields = ["nombre","email","telefono","mensaje"]
    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse_lazy("index")) 

class ContactoUpdate(LoginRequiredMixin, UpdateView):
    model = Contacto
    fields = ["nombre","email","telefono","mensaje"]
    success_url = reverse_lazy("contacto_list")
    def form_valid(self, form):
        return super().form_valid(form)

class ContactoDelete(LoginRequiredMixin, DeleteView):
    model = Contacto
    success_url = reverse_lazy("contacto_list")

def contacto(request):
    if request.method == "POST":
        miForm = ContactoForm(request.POST)
        if miForm.is_valid():
            contacto_nombre = miForm.cleaned_data.get("nombre")
            contacto_email = miForm.cleaned_data.get("email")
            contacto_telefono = miForm.cleaned_data.get("telefono")
            contacto_mensaje = miForm.cleaned_data.get("mensaje")
            contacto = Contacto(nombre=contacto_nombre, email=contacto_email, telefono=contacto_telefono, mensaje=contacto_mensaje)
            contacto.save()
            contexto = {"contacto_list": Contacto.objects.all() }
            return render(request, "personal/index.html", contexto)
    else:
        miForm = ContactoForm()

    return render(request, "personal/contacto.html", {"form": miForm})

#--- Contacto Buscar
@login_required
def buscarContacto(request):
    return render(request, "personal/buscar.html")

@login_required
def contactoEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        contacto = Contacto.objects.filter(nombre__icontains=patron)
        contexto = {'contacto': contacto}    
    else:
        contexto = {'contacto': Contacto.objects.all()}

    return render(request, "personal/contacto_list.html", contexto)




#--- Formacion

class FormacionList(ListView):
    model = Estudios

class FormacionAgregar(LoginRequiredMixin, CreateView):
    model = Estudios
    fields = ["titulo","institucion","fecha","degree"]
    success_url = reverse_lazy("formacion")

class FormacionUpdate(LoginRequiredMixin, UpdateView):
    model = Estudios
    fields = ["titulo","institucion","fecha","degree"]
    success_url = reverse_lazy("formacion")
    def form_valid(self, form):
        return super().form_valid(form)

class FormacionDelete(LoginRequiredMixin, DeleteView):
    model = Estudios
    success_url = reverse_lazy("formacion")


#--- Experiencia

class ExperienciaList(ListView):
    model = Experiencia

class ExperienciaAgregar(LoginRequiredMixin, CreateView):
    model = Experiencia
    fields = ["nombre","inicio","fin","empresa","descripcion"]
    success_url = reverse_lazy("experiencia")




#--- Login / Logout / Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            # Leer / buscar avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar= "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar


            return render (request, "personal/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "personal/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistrationForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('index'))
        else:
            return redirect(reverse_lazy('registro'))
    else:
        miForm = RegistrationForm()

    return render(request, "personal/registro.html", {"form": miForm})


#--- Edicion de perfil / Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method =="POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.username = miForm.cleaned_data.get("username")
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("index"))
    else:
        miform = UserEditForm(instance=usuario)
    return render(request, "personal/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "personal/cambiar_clave.html"
    success_url= reverse_lazy = ("index")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("index"))
    else:
        miForm = AvatarForm()
    return render(request, "personal/agregarAvatar.html", {"form": miForm}) 

