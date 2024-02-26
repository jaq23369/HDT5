import simpy
import random

# Parámetros iniciales
RAM_CAPACITY = 100  # Capacidad de la RAM en unidades
CPU_SPEED = 1       # Número de slots en el CPU
NUM_PROCESSES = 25  # Número total de procesos a simular
INTERVAL = 10       # Intervalo para la generación de nuevos procesos

def process(env, name, cpu, ram, memory_needed, execution_time):
    # Registro del tiempo de llegada del proceso
    arrive_time = env.now
    print(f'{env.now}: {name} creado; necesita {memory_needed} unidades de memoria')

    # Solicitar memoria RAM
    yield ram.get(memory_needed)
    print(f'{env.now}: {name} ha obtenido la memoria necesaria; entra en READY')

    # Solicitar tiempo de CPU y ejecutar
    with cpu.request() as req:
        yield req
        print(f'{env.now}: {name} está en RUNNING')
        yield env.timeout(execution_time)  # Simular el tiempo de procesamiento
        print(f'{env.now}: {name} ha terminado; entra en TERMINATED')

    # Devolver la memoria RAM
    yield ram.put(memory_needed)
    print(f'{env.now}: {name} ha devuelto la memoria')

    # Registro del tiempo de finalización y cálculo de estadísticas
    total_time = env.now - arrive_time
    print(f'{name} completado en {total_time} unidades de tiempo')

def generate_processes(env, cpu, ram):
    for i in range(NUM_PROCESSES):
        execution_time = random.randint(1, 10)  # Tiempo de ejecución aleatorio
        memory_needed = random.randint(1, 10)   # Memoria necesaria aleatoria
        env.process(process(env, f'Proceso {i}', cpu, ram, memory_needed, execution_time))
        yield env.timeout(random.randint(1, INTERVAL))  # Generar un nuevo proceso en un intervalo aleatorio

# Crear el entorno de simulación y recursos
env = simpy.Environment()
cpu = simpy.Resource(env, capacity=CPU_SPEED)
ram = simpy.Container(env, init=RAM_CAPACITY, capacity=RAM_CAPACITY)

# Iniciar la generación de procesos y correr la simulación
env.process(generate_processes(env, cpu, ram))
env.run()
