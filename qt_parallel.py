from math import log

random_x = (0.09,0.56,0.66,0.57,0.64,0.84,0.24,0.92,0.22,0.49)
random_y = (0.08,0.45,0.20,0.89,0.25,0.53,0.21,0.13,0.24,0.48)
random_z = (0.60,0.25,0.53,0.21,0.64,0.81,0.86,0.32,0.39,0.42)

def montecarlo(r):
    if r < 0.2:
        return 1
    elif r < 0.6:
        return 2
    else:
        return 3

values_x = list(map(lambda r: 2*r + 2, random_x))
values_y = list(map(lambda r: -4 * log(r), random_y))
values_z = list(map(montecarlo, random_z))

arrival_time = 0
departure_time_y = [0]
departure_time_z = [0]
total_waiting_time = 0
total_system_time = 0

print("{:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5}".format("C", "T/L", "HL", "TIS", "TSe", "TSa", "TE", "TS"))
print("-" * 60)

for i in range(10):
    arrival_time += values_x[i]
    initial_time = arrival_time
    waiting_time = 0
    server = None
    server_time = 0

    if values_y[i] < values_z[i]:
        server = 'A'
        server_time = values_y[i]

        if departure_time_y[-1] <= arrival_time:
            departure_time = arrival_time + values_y[i]
            departure_time_y.append(departure_time)
        elif departure_time_z[-1] <= arrival_time:
            departure_time = arrival_time + values_z[i]
            departure_time_z.append(departure_time)
            initial_time = departure_time_z[-1]
            server = 'B'
            server_time = values_z[i]
        else:
            waiting_time = departure_time_y[-1] - arrival_time
            departure_time = departure_time_y[-1] + values_y[i]
            departure_time_y.append(departure_time)
            initial_time = departure_time_y[-1]
    else:
        server = 'B'
        server_time = values_z[i]

        if departure_time_z[-1] <= arrival_time:
            departure_time = arrival_time + values_z[i]
            departure_time_z.append(departure_time)
        elif departure_time_y[-1] <= arrival_time:
            departure_time = arrival_time + values_y[i]
            departure_time_y.append(departure_time)
            initial_time = departure_time_y[-1]
            server = 'A'
        else:
            waiting_time = departure_time_z[-1] - arrival_time
            departure_time = departure_time_z[-1] + values_z[i]
            departure_time_z.append(departure_time)
            initial_time = departure_time_z[-1]

    total_waiting_time += waiting_time
    total_system_time += departure_time - arrival_time

    print("{:^5} | {:^5.1f} | {:^5.1f} | {}{:<4.1f} | {:^5.1f} | {:^5.1f} | {:^5.1f} | {:^5.1f}".format(i+1, values_x[i], arrival_time, 
                            server, initial_time, server_time, departure_time, waiting_time, departure_time-arrival_time))

mean_waiting_time = total_waiting_time / 10
mean_system_time = total_system_time / 10

print("\n\n -> TME: ", mean_waiting_time)
print(" -> TMS: ", mean_system_time)


