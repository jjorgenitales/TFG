from django.shortcuts import render
from django.utils import timezone
from .models import Usuario


# Create your views here.
def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        clave = request.POST.get('clave')
        try:
            usuario = Usuario.objects.get(correo=correo, clave=clave)
            # Guardamos datos en sesión
            request.session['nombre'] = usuario.nombre
            request.session['correo'] = usuario.correo
            request.session['id_usuario'] = usuario.idUsuario
            request.session['tipo'] = usuario.tipo  

            return redirect('categorias')
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': True})
    return render(request, 'login.html', {
            'nombre': request.session.get('nombre'),
            'tipo': request.session.get('tipo')
        })

def inicio(request):
    categorias = Categoria.objects.annotate(total=Count('producto'))
    correo = request.session.get('correo')
    return render(request, 'categorias.html', {'categorias': categorias, 'correo': correo})