import simpy
import random
import csv
from datetime import datetime

# Parámetros de configuración
RAM_CAPACITY = 100
CPU_SPEED = 1
NUM_PROCESSES = 25
INTERVAL = 10
INSTRUCTIONS_PER_CYCLE = 3

def process(env, name, cpu, ram, memory_needed, instructions, process_times):
    start_time = env.now
    print(f'{start_time}: {name} creado, necesita {memory_needed} de memoria, instrucciones {instructions}')
    
    # New -> Ready (solicitar RAM)
    with ram.get(memory_needed) as request:
        yield request
        print(f'{env.now}: {name} ha obtenido la memoria necesaria y está en READY')

        while instructions > 0:
            # Ready -> Running (solicitar CPU)
            with cpu.request() as req:
                yield req
                print(f'{env.now}: {name} está RUNNING')
                
                # Ejecutar instrucciones
                yield env.timeout(1)  # Representa un ciclo de CPU
                instructions -= min(INSTRUCTIONS_PER_CYCLE, instructions)
                print(f'{env.now}: {name} ha ejecutado instrucciones, restantes {instructions}')

                # Decisiones post ejecución
                if instructions <= 0:
                    print(f'{env.now}: {name} ha TERMINATED')
                    break
                else:
                    next_step = random.randint(1, 21)
                    if next_step == 1:
                        print(f'{env.now}: {name} entra a WAITING por I/O')
                        yield env.timeout(1)  # Simulación de tiempo de espera por I/O
                        print(f'{env.now}: {name} vuelve a READY después de I/O')
                    elif next_step == 2:
                        print(f'{env.now}: {name} se dirige nuevamente a READY sin I/O')
                    # Si next_step es diferente de 1 o 2, el proceso simplemente intentará volver a ready en el próximo ciclo sin una acción explícita aquí


    # Liberar RAM y registrar tiempo de finalización
    yield ram.put(memory_needed)
    finish_time = env.now  # Registrar tiempo de finalización
    process_times.append([name, start_time, finish_time])  # Añadir tiempos al registro
    print(f'{env.now}: {name} ha liberado su memoria')

def generate_processes(env, cpu, ram, process_times):
    for i in range(NUM_PROCESSES):
        memory_needed = random.randint(1, 10)
        instructions = random.randint(1, 10)
        env.process(process(env, f'Proceso {i}', cpu, ram, memory_needed, instructions, process_times))
        yield env.timeout(random.randint(1, INTERVAL))

# Función para guardar los tiempos en un CSV
def save_times_to_csv(times, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Proceso', 'Tiempo de Inicio', 'Tiempo de Finalización'])
        for time in times:
            writer.writerow(time)

# Lista para registrar los tiempos de cada proceso
process_times = []

env = simpy.Environment()
cpu = simpy.Resource(env, capacity=CPU_SPEED)
ram = simpy.Container(env, init=RAM_CAPACITY, capacity=RAM_CAPACITY)
env.process(generate_processes(env, cpu, ram, process_times))
env.run()

# Nombre del archivo CSV con marca de tiempo para evitar sobreescrituras
filename = f'times_{NUM_PROCESSES}_processes_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
save_times_to_csv(process_times, filename)


