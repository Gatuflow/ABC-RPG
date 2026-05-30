import clases.entidades as ent
import clases.motor as mot

def jugar():
    while True:
        nombres_de_esqueletos = ["Huesos", "Femurio", "Coxímedes", "Cuencas", "Cratos"]
        botines_de_esqueletos = [{ent.Objeto("Espada fémur", efectos = {"sangrado": 32}, peso = 5): 100, ent.Objeto(nombre = "Calavera de la vida", efectos={"salud": 50}, peso = 10): 100}]
        cantidad_de_esqueletos = 2000

        partida = mot.intro()
        if partida is None:
            continue
        jugador = partida["jugador"]
        mapa = partida["mapa"]

        for i in range(cantidad_de_esqueletos):
            x = mot.generar_coordenada(-40, 40)
            y = mot.generar_coordenada(-40, 40)
            nombre_actual = mot.atributo_aleatorio(nombres_de_esqueletos)
            botin_actual = mot.atributo_aleatorio(botines_de_esqueletos)
            esqueleto_actual = ent.Enemigo(nombre=nombre_actual, botin=botin_actual)
            mapa.set_coordenada(x, y, esqueleto_actual)
            esqueleto_actual.set_posicion((x, y))

        ventana = ent.Ventana(mapa)

        jugador.add_letra("a", 900)

        espada = ent.Objeto("Espada Magna Magnífica", {"sangrado": 32, "frío": 80}, 1)
        pocion = ent.Objeto("Poción de Salud", {"salud": 20}, 2)
        jugador.get_inventario().add(espada)
        jugador.get_inventario().add(pocion)

        jugando = True
        while jugando == True:
            jugador.actualizar()
            if jugador.get_salud() == 0:
                mot.game_over()
                jugando = False
                continue
            print(f"""\
{ventana.generar_vista(jugador.get_posicion()[0], jugador.get_posicion()[1])}
Guardar: 9 o "G" | Retirarse: 8 o "R"
Inventario: 1 o "I" | Personaje: 2 o "P" | Estados: 3 o "E" | Letras: 4 o "L"\
        """)
            accion = input("Acción: ").strip().lower()

            if accion == "1" or accion == "i":
                mot.inventario(jugador)
            elif accion == "2" or accion == "p":
                mot.personaje(jugador)
            elif accion == "3" or accion == "e":
                mot.estados(jugador)
            elif accion == "4" or accion == "l":
                mot.letras(jugador)
            elif accion == "9" or accion == "g":
                mot.guardar_partida(partida["jugador"])
            elif accion == "8" or accion == "r":
                break
            else:
                movimiento = mot.moverse(partida, accion)
                if movimiento == "menu":
                    jugando = False
                    continue
                elif movimiento == "guardar":
                    mot.guardar_partida(partida["jugador"])
                    jugando = False
                    continue    
jugar()