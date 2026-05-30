from clases.entidades import Entidad, Jugador, Objeto, Inventario, Enemigo, Mapa, Ventana
from clases.lista_enlazada import LinkedList
import random

prueba = "entidad"

#pruebas de Entidad
if "entidad" in prueba:
    ente = Entidad(salud = -800, saludMax = -800, velocidad = -800, posicion = (1.435, -4.3456))
    ante = Entidad(velocidad = 80)
    print(ente)
    ente.add_estado("sangrado", 70)
    ente2 = ente.__repr__()
    print(ente2)

    for i in range(50):
        ente.actualizar()
    print(f"""\
saludMax: {ente.get_saludMax()}\n\
salud: {ente.get_salud()}\n\
estados: {ente.get_estados()}\n\
posoción: {ente.get_posicion()}\n\
velocidad: {ente.get_velocidad()}\
""")
    
#pruebas de Objeto
if "objeto" in prueba:
    espada = Objeto(nombre = "Espada Magna Magnífica", efectos = {"sangrado": 32, "pija": -84}, peso = -80)
    espada.set_peso(-32432)
    print(f"""\
nombre: {espada.get_nombre()}\n\
efectos: {espada.get_efectos()}\n\
peso: {espada.get_peso()}\
""")
    
#pruebas de Inventario
if "inventario" in prueba:
    inventario = Inventario()
    inventario.add(Objeto())
    inventario.add(Objeto("objeto2"))
    print(inventario)
    #nota: el inventario sólo debería recibir objetos, actualmente recibe cualquier tipo
    #de datos, pero también se puede implementar esta restricción en el main

#pruebas de Jugador
if "jugador" in prueba:
    espada = Objeto("Espada Magna Magnífica", {"saludMax": -3342, "pija": 84})
    jugador = Jugador(nombre = "Pablo", saludMax = 0, salud = 2345)
    jugador.set_nombre("Jazmín")
    jugador.add_letra("p", -2)
    jugador.dar(espada)
    jugador.usar_objeto(espada)
    print(f"""\
nombre: {jugador.get_nombre()}
inventario: {jugador.get_inventario()}
letras: {jugador.get_letras()}
""")
    print(jugador.atacar(""))
    print(jugador.__repr__())

if "enemigo" in prueba:
    malo = Enemigo(nombre = "Voldemort",\
                   blindaje = "asd12324l",\
                   inmunidades = ("sangrado", "vergeada"),\
                   botin = {Objeto("poción de salud", {""}): 100, Objeto(nombre = "Espada Magna Magnífica",\
                                   efectos = {"sangrado": 32, "pija": -84},\
                                   peso = -80): 50})
    malo.recibir_danio(80, {"chingada tu madre weeeeeeeeeey": 932045467, "sangrado": 9})
    print(f"""\
nombre: {malo.get_nombre()}
blindaje: {malo.get_blindaje()}
botín: {malo.get_botin()}
inmunidades: {malo.get_inmunidades()}
          """)
    print(malo)
    malo.actualizar()
    print(malo)

if "mapa" in prueba:
    mapa = Mapa(100, 100)
    print(mapa.get_coordenada(49,49))
    mapa.set_coordenada(49, 49, "pijadura")
    print(mapa)

if "ventana" in prueba:
    mapa = Mapa(11, 11)
    jugador = Jugador()
    mapa.set_coordenada(0, 0, jugador)
    mapa.mover_entidad(jugador, "sssss")
    ventana = Ventana(mapa)
    print(ventana.generar_vista(0, 0))

if "linkedlist" in prueba:
    lista = LinkedList()
    for i in range(134):
        lista.add(i)
    print(lista.get_index("pijadura"))