from math import log

random_numbers_x = [0.262, 0.95, 0.67, 0.97, 0.73, 0.75, 0.64, 0.265, 0.45, 0.01]
random_numbers_y = [0.47, 0.79, 0.54, 0.08, 0.89, 0.33, 0.88, 0.09, 0.26, 0.82]
values_x = list(map(lambda r: -3 * log(r), random_numbers_x))
values_y = list(map(lambda r: 2 * r + 3, random_numbers_y))

total_waiting_time = 0.0
total_system_time = 0.0
arrival_time = 0.0
initial_time_service = 0.0
departure_time = 0.0

print("\n\nCliente | T LLegada | H Llegada | T Inicio | T Servicio | T Salida | T Espera | T Sistema")
print("-" * 90)

for i in range(10):
    waiting_time = 0.0
    arrival_time += values_x[i]

    if initial_time_service < departure_time:
        waiting_time = departure_time - arrival_time
        total_waiting_time += waiting_time
        initial_time_service = departure_time
    else:
        initial_time_service += values_x[i]

    departure_time = initial_time_service + values_y[i]
    system_time = departure_time - arrival_time
    total_system_time += system_time

    print("{:^8}|{:^11.2f}|{:^11.1f}|{:^10.2f}|{:^12.2f}|{:^10.2f}|{:^10.2f}|{:^10.2f}".format(i+1, values_x[i], arrival_time, initial_time_service, values_y[i], departure_time, waiting_time, system_time))

print("\n\nTiempo medio de Espera: {total_waiting_time:.2f}".format(total_waiting_time=total_waiting_time/10))
print("Tiempo medio en el Sistema: {total_system_time:.2f} \n\n".format(total_system_time=total_system_time/10))
