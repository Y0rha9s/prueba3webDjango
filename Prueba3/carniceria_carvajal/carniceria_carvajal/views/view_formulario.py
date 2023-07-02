from django.shortcuts import render
from carniceria_carvajal.models.models import Contact

def formulario(request):
    return render(request, 'formulario.html', {})

def save(request):
    print('request: ',request)
    print('request.method: ', request.method)
    if request.method == "POST":
        print('invcado por post')
        #lectura de los parametros provenientes del formulario
        nombre = request.POST['nombres']
        apellido = request.POST['apellidos']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        sugerencia = request.POST['sugerencia']
        # creando un objeto de tipo model (crud)
        datos = Contact();
        # asignando valores a los atributos del objeto de tipo model
        datos.nombres = nombre;
        datos.apellidos = apellido;
        datos.correo = correo;
        datos.telefono = int(telefono);
        datos.sugerencia = sugerencia;
        message = None
        message_error = None
        try:
            datos.save()
            message = "registro almacenado"
        except Exception as e:
            message_error = "error intente mas tarde"
        return render(request,'formulario-guardar.html', {'datos' : datos, 'message': message,'message_error': message_error })
    else:
        return render(request, 'error.html',{})