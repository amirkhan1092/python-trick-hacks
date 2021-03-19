"""
the module psutil(process and system utilities) is a cross-platform
library for retrieving information on running processes and system utilization
(CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring,
profiling and limiting process resources and management of running processes
"""

import psutil

# battery power display
power = psutil.sensors_battery()
x = power.percent
print(type(power))
print(x, type(x))

# cpu count
n_cpu = psutil.cpu_count()
print(n_cpu)


