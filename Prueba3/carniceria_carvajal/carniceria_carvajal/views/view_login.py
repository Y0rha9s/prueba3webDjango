from django.shortcuts import render
import traceback
from carniceria_carvajal.models.models import Usuario

def login(request):
    print('login')
    if request.method == 'GET':
        return render(request, 'index.html', {'message_error' : None}) 
    elif request.method == 'POST':
        try:
            print('request_post:', request.POST)
            user = request.POST['username']
            password = request.POST['password'] 
            usuario = Usuario.objects.get(usuario=user)
            print('contrasena', usuario.contrasena)
            print('password', password)
            if usuario.contrasena == password: 
                return render(request, 'login.html')
            else:
                return render(request, 'index.html', {'message_error' : 'USUARIO O CONTRASEÑA INVALIDA'}) 
        except Exception as e:
            traceback.print_exc()
            return render(request, 'index.html', {'message_error' : 'ERROR INESPERADO INTENTE MAS TARDE'})        