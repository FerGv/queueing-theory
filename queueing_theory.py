from math import log
from random import random

customers = int(input("\n\n¿Para cuántos clientes se realizará la simulación? "))
values_x = list(map(lambda r: -3 * log(r), [random() for i in range(customers)]))
values_y = list(map(lambda r: 2 * r + 3, [random() for i in range(customers)]))
total_waiting_time = 0.0
total_system_time = 0.0
arrival_time = 0.0
initial_time_service = 0.0
departure_time = 0.0

print("\n\nCliente | T LLegada | H Llegada | T Inicio | T Servicio | T Salida | T Espera | T Sistema")
print("-" * 90)

for i in range(customers):
    waiting_time = 0.0
    arrival_time += values_x[i]

    if arrival_time < departure_time:
        waiting_time = departure_time - arrival_time
        total_waiting_time += waiting_time
        initial_time_service = departure_time
    else:
        initial_time_service += values_x[i]

    departure_time = initial_time_service + values_y[i]
    system_time = departure_time - arrival_time
    total_system_time += system_time

    print("{:^8}| {:^10.2f}| {:^10.2f}|{:^10.2f}|{:^12.2f}|{:^10.2f}|{:^10.2f}|{:^10.2f}".format(i+1, values_x[i], arrival_time, initial_time_service, values_y[i], departure_time, waiting_time, system_time))

print("\n\nTiempo medio de Espera: {total_waiting_time:.2f}".format(total_waiting_time=total_waiting_time/customers))
print("Tiempo medio en el Sistema: {total_system_time:.2f} \n\n".format(total_system_time=total_system_time/customers))
