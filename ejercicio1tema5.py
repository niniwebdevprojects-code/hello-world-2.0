#Esta lista es la que funcionará como base de datos ya que tendrá toda la información de todos los usuarios que se registren durante la ejecución de este programa.
usuarios = []
#Estas variables se utilizarán como un objetos que guardan la información temporalmente 
usuario = ''
cancion = ''
#Esta variable se utilizará como objeto que nos va a ayudar a guardar la información que contienen los dos objetos anteriores(usuario y cancion)
#en la base de datos(usuarios)
actualObjeto = ''
class Usuario:
    def __init__(self, nombreCompleto, dni, poblacion, pais):
        self.nombreCompleto = nombreCompleto
        self.dni = dni
        self.poblacion = poblacion
        self.pais = pais
   
class Cancion:
    def __init__(self, nombre, artista, estiloMusical):
        self.nombre = nombre
        self.artista = artista
        self.estiloMusical = estiloMusical

class BaseDeDatos(Usuario, Cancion): 
    def __init__(self, usuario, cancion):
        self.usuario = usuario
        self.cancion = cancion
    
    def validarDatos(self):
        if self.usuario.nombreCompleto and self.usuario.dni and self.usuario.poblacion and self.usuario.pais and self.cancion.nombre and self.cancion.artista and self.cancion.estiloMusical:
            return True
        return False
    
    def guardarUsuario(self):
        global usuarios
        dicUsuario = {
                'Nombre Completo': '',
                'DNI': '',
                'Población': '',
                'País': '',
                'Nombre': '',
                'Artista': '',
                'Estilo Musical': ''
            }
        if (self.validarDatos() == True):
            dicUsuario['Nombre Completo'] = self.usuario.nombreCompleto
            dicUsuario['DNI'] = self.usuario.dni
            dicUsuario['Población'] = self.usuario.poblacion
            dicUsuario['País'] = self.usuario.pais
            dicUsuario['Nombre'] = self.cancion.nombre
            dicUsuario['Artista'] = self.cancion.artista
            dicUsuario['Estilo Musical'] = self.cancion.estiloMusical
            usuarios.append(dicUsuario)
            print('Usuario guardado!')

    def mostrarPorPantalla(self):
        global usuarios
        if self.validarDatos():
            contrasena = input('Escribe tu DNI: ').upper()
            for k in usuarios:
                dicUsuario = k
                if (contrasena == dicUsuario['DNI']):
                    print(f"""Información del usuario:
                        Nombre Completo: {dicUsuario['Nombre Completo']}
                        DNI: {dicUsuario['DNI']}
                        Población: {dicUsuario['Población']}
                        País: {dicUsuario['País']}
                        Canción favorita del usuario:
                        Nombre: {dicUsuario['Nombre']}
                        Artista: {dicUsuario['Artista']}
                        Estilo Musical: {dicUsuario['Estilo Musical']}""")
                    return True
            else: 
                print('DNI incorrecto.')

def agregarDatos():
    global usuario
    global cancion
    global actualObjeto
    print('Para poder guardar sus datos necesitamos que rellene su información personal en los siguientes campos:')
    nombreCompleto = input('Nombre Completo: ').title()
    dni = input('DNI: ').upper()
    if (len(dni) != 9 or dni.isalnum() == False):
        print('DNI inválido. Recuerda que tiene que tener 9 carácteres y ser alfanúmerico.')
        agregarDatos()
    poblacion = input('Población: ').title()
    pais = input('País: ').capitalize()
    print('Ahora necesitamos un poco de información sobre tu canción favorita.')
    nombre = input('¿Cuál es tú canción favorita? ')
    artista = input('¿De qué grupo/artista es la canción? ')
    estiloMusical = input('¿De qué estilo musical es la canción? ').upper()
    usuario = Usuario(nombreCompleto, dni, poblacion, pais)
    cancion = Cancion(nombre, artista, estiloMusical)
    actualObjeto = BaseDeDatos(usuario, cancion)
    actualObjeto.validarDatos()
    actualObjeto.guardarUsuario()
    return True
    
def salir():
    global usuarios
    print(usuarios)
    return False
 
def switch(opcionElegida):
    global actualObjeto
    opciones = {
        '1': 'agregarDatos()', 
        '2': 'actualObjeto.mostrarPorPantalla()', 
        '3': 'salir()', 
    }
    return eval(opciones.get(opcionElegida))

while (True):
    print("""Elija lo que quiere hacer: 
      1. Agregar datos personales del usuario y datos de la canción
      2. Ver datos de usuario
      3. Salir
     """)
    opcionElegida = input()
    try: 
        continuar = switch(opcionElegida)
    except Exception as a:
        print('Seleccione una opción válida.')
    if (continuar == False):
        print('Ha salido del programa.')
        break











            
