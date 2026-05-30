# El Exilio Solitario

¡Hola! Este es mi proyecto "El Exilio Solitario" Las siguientes secciones contienenen explicaciones detalladas sobre el propósito del proyecto y el proceso de desarrollo.

## Propósito del proyecto
El Exilio Solitario no empezó con el propósito de ejecutar una idea específica en un videojuego, ni con el objetivo de completar un proyecto, en realidad, el propósito original de este programa era reforzar mi aprendizaje personal. El proyecto era una práctica integradora que pondría en práctica los conocimientos que aprendí en los capítulos del 1 al 17 del libro "Aprende a pensar como un programador con Python" de Allen Downey y compañía. Por ese motivo, el proyecto no está pulido, y el escenario inicial planteado por el archivo **main.py** es básico y no explota el potencial del motor.
Aunque me hubiera gustado terminarlo, tomé la decisión de cerrarlo porque ya cumplió su objetivo pedagógico en mi aprendizaje. Actualmente, una refactorización del código consumiría mucho tiempo, y no aprendería al ritmo que lo hice durante las fases tempranas e intermedias del desarollo. Evité continuar al sentir que corregía código cuyos errores de lógica y arquitectura ya comprendía de sobra, pues el tedio, para este proyecto particular, no retorna la inversión de tiempo y energía.

## Registro del proceso

* **Tipo de dato personalizado**: El proceso de desarrollo de este proyecto inició con la creación de un tipo de dato propio, una clase de lista enlazada, ubicada en el archivo **lista_enlazada.py**, con sus métodos y lógica incluídos. Si bien no es perfecta, es quizás la parte más pulida de todo el proyecto, a pesar de ser la inicial, y quizás la rescate para proyectos posteriores. El motivo de haber pasado tanto tiempo perfeccionando este primer archivo, fue un sentimiento de importancia, sentía que si la lista enlazada estaba mal, los problemas a pagar serían demasiado grandes.
* **Lógica de POO, herencia, polimorfismo, etc:**: El siguiente archivo fue **entidades.py**, en el cuál desarrollé la lógica de una entidad base, de la cual heredan las clases **Jugador** y **Enemigo**. Agregué también la clase **Inventario**, que heredaría de **LinkedList**, y que tiene sus métodos específicos para el juego, incluyendo una función recursiva para calcular el peso total de todos los objetos, según la consigna del proyecto. los objetos son otra clase, junto con el mapa, una matriz con lógica de coordenadas cartesianas que se complementa con el atributo "posicion" de **Entidad**, **Enemigo** y **Jugador**.
* **Lógica de negocio y motor de juego**: El archivo **motor.py** contiene todas las funciones que el **main.py** necesita para llevar a cabo el juego, según cómo se escriba el archivo main, es posible crear escenarios personalizados varios, el escenario guardado en el proyecto actual es más bien mediocre, así que cualquiera que esté leyendo esto y sienta curiosidad, está formalmente invitado a explotar el potencial del motor de juego de formas interesantes con objetos, enemigos, y mapas varios.

## Post-Mortem
Mirando hacia atrás, si bien el proyecto me enseñó muchísimo y estoy orgulloso de mi progreso como desarrollador y diseñador de software, puedo notar carencias en el desarollo de la consigna inicial. Por ejemplo, si bien con este proyecto aprendí sobre la serialización y la deserialización, la consigna pedía explícitamente que utilizara el código **pickle**, al olvidar eso, investigué e implementé serialización con archivos de texto plano, que después convertí a archivos de **.json**, con los cuales se pueden guardar y cargar las partidas.
Otro error que puedo notar y no repetiré en proyectos futuros es la mezcla de lógica de negocio con la interfaz lógica, entre el **main.py** y el **motor.py** hay funcionalidades y lógica mezcladas que fallan en la encapsulación de las tareas de ejecución.

## Instrucciones de uso
Cualquier interesado en inicializar el juego, debe ejecutar en la consola el archivo **main.py** una vez que haya descargado la carpeta del proyecto. ya sea ejecutándolo en su editor de código preferido, o en la terminal con:
```bash
python3 main.py