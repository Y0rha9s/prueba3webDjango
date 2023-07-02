from django.shortcuts import render
from carniceria_carvajal.models.models import Usuario

def registro(request):
    return render(request, 'registro.html', {})

def save(request):
    print('request: ',request)
    print('request.method: ', request.method)
    if request.method == "POST":
        print('invcado por post')
        #lectura de los parametros provenientes del registro
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        # creando un objeto de tipo model (crud)
        datos = Usuario();
        # asignando valores a los atributos del objeto de tipo model
        datos.usuario = usuario;
        datos.contrasena = contrasena;
        datos.correo = correo;
        datos.telefono = int(telefono);
        datos.direccion = direccion;
        message = None
        message_error = None
        try:
            datos.save()
            message = "registro almacenado"
        except Exception as e:
            message_error = "error intente mas tarde"
        return render(request,'registro-guardar.html', {'datos' : datos, 'message': message,'message_error': message_error })
    else:
        return render(request, 'error.html',{})