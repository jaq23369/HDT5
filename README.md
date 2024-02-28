Autor: Joel Antonio Jaquez López
Carné: 23369
Fecha de inicio: 26/02/2024
Fecha de Finalización: 27/02/2024

Explicación del programa:
Objetivos:
a. Simulación DES (Discrete Event Simulation) usando el módulo SimPy.
b. Utilización de colas con la clase Resources y Container de SimPy.
Simulación:
Simulación de corrida de programas en un sistema operativo de tiempo compartido (el procesador se comparte por una
porción de tiempo entre cada programa que se desea correr). En la terminología de sistemas operativos se llama “proceso” a
un programa que se ejecuta.

new: el proceso llega al sistema operativo pero debe esperar que se le asigne memoria RAM. En nuestra simulación el
proceso solicitará una cantidad de memoria (número entero al azar entre 1 y 10). Si hay memoria disponible puede pasar al
estado de ready. En caso contrario permanece haciendo cola, esperando por memoria. NOTA: la cantidad de memoria
disponible se disminuye con la cantidad de memoria que empleará el proceso que logró obtenerla.

ready: el proceso está listo para correr pero debe esperar que lo atienda el CPU. El proceso tiene un contador con la cantidad
de instrucciones totales a realizar (número entero al azar entre 1 y 10). Cuando se desocupa el CPU puede pasar a utilizarlo.

running: el CPU atiende al proceso por un tiempo limitado, suficiente para realizar solamente 3 instrucciones (esto será
configurado, ya que podrá crecer o reducirse). Al completarse el tiempo de atención el proceso es retirado del CPU. Se debe
actualizar el contador de instrucciones a realizar, disminuyendo las 3 instrucciones que ejecutó en esta oportunidad. Si el
proceso tiene menos de tres instrucciones que le hace falta procesar, libera el CPU anticipadamente.

Al finalizar la atención del CPU puede ocurrir:
a)Terminated: Si el proceso ya no tiene instrucciones por realizar entonces pasa al estado “terminated” y sale del sistema.
b)Waiting: al dejar el CPU se genera un número entero al azar entre 1 y 21. Si es 1 entonces pasa a la cola de Waiting par a
hacer operaciones de I/O (entrada/salida). Al dejar esa cola regresa a “ready”.
c)Ready: al dejar el CPU y el número generado al azar es 2 entonces se dirige nuevamente a la cola de “ready”.

Tareas a cumplir:
A. Hacer el programa de simulación y usarlo con 25 procesos, luego con 50 procesos, con 100, 150 y 200 procesos. Su
programa debe mostrar el promedio de tiempo que está el proceso en la computadora en cada caso y la desviación
standard. Haga gráfica con número de procesos y tiempo promedio.

B. Vuelva a correr su simulación, pero ahora los procesos llegar más rápido, es decir en intervalos de 5. Calcule los tiempo
promedio para las mismas cantidades de procesos: 25,50,100,150 y 200. Repita lo mismo para intervalos de 1 ( mucha
carga de trabajo). Haga gráfica con número de procesos y tiempo promedio.

C. Revise las gráficas y trate de reducir el tiempo promedio. Pruebe con:
    i. incrementar la memoria a 200,
    ii. luego con poner la memoria nuevamente a 100, pero tener un procesador más rápido (es decir que ejecuta 6  
    instrucciones por unidad de tiempo),
    iii. luego regrese a la velocidad normal procesador pero emplee 2 procesadores.
Haga gráficas para cada cambio con las cantidades de 25,50,100,150 y 200 procesos (e intervalos de 10, 5, 1) . D ecida
cuál es la mejor estrategia para reducir el tiempo promedio de ejecución de los procesos, justifique su respuesta.

"OJO, INFORMACIÓN A TOMAR EN CUENTA"
Como indicación final cabe mencionar que al cambiar el numero de procesos saldrá todo en la terminal y pues las gráficas se generan con Matplotlib de manera automática, pero si al cambiar de número de procesos no sale nada en la terminal darle en el "Basurero"
osea terminal la terminal, guardar y ahora si volver a correrlo para ver los tiempos y gráfica de la nueva cantidad de procesos. La desviación estándar y promedio de tiempos que se adjuntan en el PDF se muestran en la terminal.
