from math import log
from random import random

def queueing_theory(*functions, **kwargs):
    """ 
        Queueing Theory Parameters:
        *functions ('name_function', values)
            - Poisson => ('p', mean_value)
            - Exponential => ('e', mean_value)
            - Uniform => ('u', mean_value, variation)
        **kwargs -> simulation = number_of_simulations

        Function returns mean waiting time and mean system time.

        Note: Functions order -> arrival_time_function, n-servers-functions
    """
    total_waiting_time = 0.0
    total_system_time = 0.0
    arrival_time = 0.0
    departure_time_list = []
    simulations = kwargs['simulations']
    servers_functions = len(functions[1:])
    counter = 0
    values = []

    for function in functions:
        if function[0] == 'p' or function[0] == 'e':
            value = tuple(map(lambda r: -function[1] * log(r), [random() for i in range(simulations)]))
        else:
            min_value = function[1] - function[2]
            max_value = function[1] + function[2]
            value = tuple(map(lambda r: (max_value - min_value)*r + min_value, [random() for i in range(simulations)]))
        
        values.append(value)

    for simulation in range(simulations):
        waiting_time = 0.0
        arrival_time += values[0][simulation]
        initial_time = arrival_time

        for function in range(servers_functions):
            counter += 1
            if counter == 1:
                pass
            else:
                if initial_time < departure_time_list[counter - (servers_functions+1)]:
                    waiting_time += departure_time_list[counter - (servers_functions+1)] - initial_time
                    initial_time = departure_time_list[counter - (servers_functions+1)]

            departure_time = initial_time + values[function+1][simulation]
            initial_time = departure_time
            departure_time_list.append(departure_time)

        total_waiting_time += waiting_time
        system_time = departure_time - arrival_time
        total_system_time += system_time

    mean_waiting_time = total_waiting_time / simulations
    mean_system_time = total_system_time / simulations

    return mean_waiting_time, mean_system_time


def main():
    """ Example """
    functions = []
    while True:
        print("\n\nEscoge una distribución \n1. Poisson \n2. Exponencial \n3. Uniforme \n4. Salir ")
        option = int(input("\n\tOpción: "))
        if option == 1 or option == 2:
            mean_service = float(input("\t¿Cuál es la media? "))
            functions.append(('p', mean_service)) if option == 1 else functions.append(('e', mean_service))
        elif option == 3:
            mean_service = float(input("\t¿Cuál es la media? "))
            variation_service = float(input("\t¿Cuál es la variación? "))
            functions.append(('u', mean_service, variation_service))
        else:
            break

    simulations = int(input("\t¿Cuántas simulaciones se realizarán? "))

    wt, st = queueing_theory(*functions, simulations=simulations)

    print("\n\nTiempo medio de Espera: {mean_waiting_time:.2f}".format(mean_waiting_time=wt))
    print("Tiempo medio en el Sistema: {mean_system_time:.2f} \n\n".format(mean_system_time=st))


if __name__ == '__main__':
    main()
