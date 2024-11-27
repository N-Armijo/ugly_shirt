"""
URL configuration for tienda_poleras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from productos.views import listar_poleras, crear_polera, registro_usuario, editar_usuario, editar_polera, eliminar_polera

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='registro_usuario'), name='logout'), #especifica la pagina a la que redirige
    path('', listar_poleras, name='listar_poleras'),
    path('crear_polera/', crear_polera, name='crear_polera'),
    path('registro/',registro_usuario, name='registro_usuario'),
    path('editar_perfil/',editar_usuario, name='editar_usuario'),
    path('editar_polera/<int:pk>/', editar_polera, name='editar_polera'),
    path('eliminar_polera/<int:pk>/',eliminar_polera, name='eliminar_polera'),
]
