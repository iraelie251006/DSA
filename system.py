def read_system_cpu_times():
    with open("/proc/stat") as f:
        line = f.readline()

    fields = line.split()
    times = list(map(int, fields[1:]))
    total = sum(times)
    idle = times[3] + times[4]

    return total, idle

def read_pid_cpu_time(pid):
    # open /proc/{pid}/stat
    # extract: process name, utime + stime
    # return (name, total_ticks) or None if process is gone
    with open(f"/proc/{pid}/stat") as f:
        pass
