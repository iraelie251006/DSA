def read_system_cpu_times():
    with open("/proc/stat") as f:
        line = f.readline()

    fields = line.split()
    times = list(map(int, fields[1:]))
    total = sum(times)
    idle = times[3] + times[4]

    return total, idle
