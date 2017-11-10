# queueing-theory
Program to calculate the mean waiting time and mean system time using the queueing theory.

### Queueing Theory Parameters `queueing_theory(*functions, **kwargs)`:
  * __*functions -> n-tuples with format ('name_function', values)__
      - Poisson => ('p', mean_value)
      - Exponential => ('e', mean_value)
      - Uniform => ('u', mean_value, variation)
  * __**kwargs__ -> simulation = number_of_simulations
  
  Function returns mean waiting time and mean system time.
  
  **Note: Functions order -> arrival_time_function, n-servers-functions**
