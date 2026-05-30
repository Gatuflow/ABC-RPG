#Terminar la reconstrucción del jugador al cargar una partida guardada y asegurarse de que esté correcta
import clases.entidades as ent
import random
import json
import sys
from pathlib import Path
import math

def intro():
    print("""
_____________________________________________________________

¡Bienvenido a ABC-RPG!
      
Crear una nueva partida: 1 o "N"
Cargar una partida previa: 2 o "P"
Ver partidas existentes: 3 o "V"
Borrar partida: 4 o "B"
_____________________________________________________________
      """)
    input_partida = input("Acción: ").lower().strip()
    if input_partida == "1" or input_partida == "n":
        return partida_nueva()
    elif input_partida == "2" or input_partida == "p":
        return cargar_partida()
    elif input_partida == "3" or input_partida == "v":
        return ver_partidas()
    elif input_partida == "4" or input_partida == "b":
        borrar_partida()
    else: return None

def partida_nueva():
    partida = {}
    nombre = input("Introduzca su nombre: ")
    partida["jugador"] = ent.Jugador(nombre=nombre)
    partida["mapa"] = ent.Mapa()
    partida["mapa"].set_coordenada(partida["jugador"].get_posicion()[0], partida["jugador"].get_posicion()[1], partida["jugador"])
    return partida

def moverse(partida, inputs):
    jugador = partida["jugador"]
    mapa = partida["mapa"]
    baldosa = mapa.mover_entidad(jugador, inputs)
    if isinstance(baldosa, ent.Enemigo):
        enemigo = baldosa
        return combate(jugador, enemigo, mapa)

def inventario(jugador):
    while True:
        print(f"""\
_____________________________________________________________
                
{jugador.get_inventario()}
_____________________________________________________________

Volver: 0 o "V" | Empuñar: 1 o "E" | Tirar: 2 o "T"\
    """)
        accion = input("Acción: ").strip().lower()
        if accion == "0" or accion == "v": return
        elif accion == "1" or accion == "e":
            indice = input("Empuñar: ")
            try:
                int(indice)
                empuniar(jugador, int(indice))
            except ValueError:
                print("\nÍndice inválido")
            
        elif accion == "2" or accion == "t":
            objeto = input("Tirar: ")
            tirar(jugador, objeto)

def personaje(jugador):
    print(jugador)
    input("presione ENTER para volver ")

def estados(jugador):
    print(f"""\
_____________________________________________________________
              
{jugador.estados_lindo()}
_____________________________________________________________
""")
    input("presione ENTER para volver ")

def letras(jugador):
    print(f"""\
_____________________________________________________________
              
{jugador.letras_bonito()}
_____________________________________________________________
""")
    input("presione ENTER para volver ")

def empuniar(jugador, indice):
    objeto = jugador.get_inventario().get_index(indice - 1)
    if objeto is None:
        print("\nEL OBJETO NO EXISTE")
        return
    nombre = objeto.get_nombre()
    jugador.set_mano(nombre)
    print(jugador.get_mano())
    nombre = jugador.get_mano().get_nombre()
    print(f"""
{nombre} en mano
""")
    

def tirar(jugador, objeto):
    jugador.quitar(objeto)

def generar_coordenada(min: int, max: int):
    coordenada = random.randint(min, max)
    return coordenada

def atributo_aleatorio(lista: list):
    return random.choice(lista)

def game_over():
    print("""
_____________________________________________________________

HAS MUERTO
          
Salir: 1 o "Q" | Volver al menú: 2 o "M" | Guardar partida como recuerdo: 3 o "R"
_____________________________________________________________
""")
    accion = input("Acción: ").strip().lower()
    if accion == "1" or accion == "q": sys.exit()
    elif accion == "2" or accion == "m": return "menu"
    elif accion == "3" or accion == "r": return "guardar"
    else: return game_over()

    
def combate(jugador, enemigo, mapa):
    velocidad_jugador_restaurar = jugador.get_velocidad()
    velocidad_enemigo_restaurar = enemigo.get_velocidad()
    velocidad_jugador = velocidad_jugador_restaurar
    velocidad_enemigo = velocidad_enemigo_restaurar
    print("""\
_____________________________________________________________
          
Enemigo localizado\
          """)
    while True:
        jugador.actualizar()
        if jugador.get_salud() == 0: return game_over()
        if enemigo.get_salud() == 0:
            matar_enemigo(enemigo, jugador, mapa)
            soltar_botin(enemigo, jugador)
            return

        enemigo.actualizar()
        if velocidad_jugador == 0 and velocidad_enemigo == 0:
            velocidad_enemigo = velocidad_enemigo_restaurar
            velocidad_jugador = velocidad_jugador_restaurar
        elif velocidad_jugador >= velocidad_enemigo:
            print(f"""        
¡Tienes la iniciativa!
{enemigo}
Retirada | Inventario | Personaje | Estados | Letras
""")
            ataque = input("¡Ataque de letras!: ").lower().strip()
            if "retirada" in ataque:
                return
            elif "inventario" in ataque:
                inventario(jugador)
                continue
            elif "personaje" in ataque:
                personaje(jugador)
                continue
            elif "estados" in ataque:
                estados(jugador)
                continue
            elif "letras" in ataque:
                letras(jugador)
                continue
            fuerza_del_ataque = jugador.atacar(ataque, enemigo.get_blindaje())
            enemigo.recibir_danio(fuerza_del_ataque, jugador.get_mano().get_efectos() if jugador.get_mano() else {})
            print(enemigo)
            velocidad_jugador -= 1
        elif velocidad_enemigo > velocidad_jugador:
            ataque = enemigo.atacar("abcdefghijklmnñopqrstuvwxyz")
            print(f"""
¡{enemigo.get_nombre()} tiene la iniciativa!
""")
            jugador.recibir_danio(ataque, enemigo.get_efectos())
            velocidad_enemigo -= 1

def matar_enemigo(enemigo, jugador, mapa):
    posicion_enemigo = enemigo.get_posicion()
    posicion_jugador = jugador.get_posicion()
    mapa.set_coordenada(posicion_enemigo[0], posicion_enemigo[1], jugador)
    mapa.set_coordenada(posicion_jugador[0], posicion_jugador[1], "·")
    jugador.set_posicion((posicion_enemigo[0], posicion_enemigo[1]))
    print(f"""
_____________________________________________________________
          
{enemigo.get_nombre()} ha muerto
_____________________________________________________________\
""")

def soltar_botin(enemigo, jugador):
    print("Botín enemigo:")
    for objeto in enemigo.get_botin():
        print(f"""
{objeto}
Quedárselo: 1 o "Q" | Tirarlo: 2 o "T" | Salir: 3 o "S"
""")
        accion = input("Acción: ").lower().strip()
        if accion == "1" or accion == "q":
            jugador.get_inventario().add(objeto)
            continue
        elif accion == "2" or accion == "t":
            continue 
        elif accion == "3" or accion == "q":
            break

def guardar_partida(jugador):
    carpeta_actual = Path(__file__).parent
    raiz = carpeta_actual.parent
    carpeta_destino = raiz / "partidas"
    
    nombre = input("Nombre de la partida: ").strip()
    
    ruta_final = (carpeta_destino / f"{nombre}.txt").resolve()
    carpeta_destino.mkdir(exist_ok=True)
    with open(f"{ruta_final}", "w", encoding="utf-8") as archivo:
        json.dump(jugador.to_dict(), archivo, indent=4)

def cargar_partida():
    print("""
Volver: 1 o "V"
""")
    nombre = input("Nombre de la partida: ").strip()
    if nombre.lower().strip() == "1" or nombre == "v": return None
    ruta_actual = Path(__file__).parent
    raiz = Path(ruta_actual).parent
    ruta_objetivo = raiz / "partidas" / f"{nombre}.txt"
    try:
        with open(ruta_objetivo, "r", encoding="utf-8") as partida_guardada:
            partida = json.load(partida_guardada)
                
    except FileNotFoundError:
        print("""
Esta partida no existe
""")
        return cargar_partida()
    jugador = to_Jugador(partida)    
    mapa = ent.Mapa()
    mapa.set_coordenada(jugador.get_posicion()[0], jugador.get_posicion()[1], jugador)
    return {"jugador": jugador, "mapa": mapa}

def armar_estados(jugador, diccionarioDesarmado):
    for elemento in diccionarioDesarmado.strip().split("|"):
        partido = elemento.split(":")
        jugador.add_estado(partido[0].strip(), int(partido[1]))

def armar_posicion(jugador, tuplaDesarmada):
    lista = tuplaDesarmada.split("|")
    x = int(lista[0].strip())
    y = int(lista[1].strip())
    jugador.set_posicion((x, y))

def ver_partidas():
    ruta_carpeta = Path(__file__).parent.parent / "partidas"
    ruta_carpeta.mkdir(exist_ok=True)
    nombres = [file.name.split(".")[0] for file in ruta_carpeta.iterdir() if file.is_file() and file.suffix == ".txt"]
    print(f"""
{"\n".join(nombres)}
          """)
    input("presione ENTER para volver ")
    return None

def borrar_partida():
    print("""
Volver: 1 o "V"
          """)
    nombre_archivo = input("Nombre de la partida: ").strip()
    if nombre_archivo.lower() == "v" or nombre_archivo == "1": return intro()
    ruta_archivo = Path(__file__).parent.parent / "partidas" / f"{nombre_archivo}.txt"
    if ruta_archivo.exists():
        ruta_archivo.unlink()
        print("\nPartida borrada")
        return
    print("\nel archivo no existe")
    return borrar_partida()

def to_Jugador(dicti):
    jugador = ent.Jugador(
        nombre=dicti["nombre"],
        saludMax=dicti["saludMax"],
        salud=dicti["salud"],
        posicion=dicti["posicion"],
        velocidad=dicti["velocidad"],
        inventario= to_Inventario(dicti["inventario"]))
    for clave, valor in dicti["estados"].items():
        jugador.add_estado(clave, valor)
    for clave, valor in dicti["letras"].items():
        jugador.add_letra(clave, valor - 1)
    jugador.set_mano(dicti["mano"])
    return jugador
    
def to_Inventario(lista):
    inventario = ent.Inventario()
    for elemento in lista:
        inventario.add(to_Objeto(elemento))
    return inventario

def to_Objeto(dicti):
    return ent.Objeto(
        nombre=dicti["nombre"],
        efectos=dicti["efectos"],
        peso=dicti["peso"]
    )

def calcular_distancia(coordenada1: tuple[int, int], coordenada2: tuple[int, int]):
    x1 = coordenada1[0]
    x2 = coordenada2[0]
    y1 = coordenada1[1]
    y2 = coordenada2[1]
    distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distancia