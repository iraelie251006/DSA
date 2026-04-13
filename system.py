import os

def read_system_cpu_times():
    with open("/proc/stat") as f:
        line = f.readline()

    fields = line.split()
    times = list(map(int, fields[1:]))
    total = sum(times)
    idle = times[3] + times[4]

    return total, idle

def read_pid_cpu_time(pid):
    try:
        with open(f"/proc/{pid}/stat") as f:
            data = f.readline()

        rparen = data.rfind(")")
        name = data[data.find("(") + 1:rparen]

        rest = list(map(int, data[rparen + 4:].split()))

        total_ticks = rest[10] + rest[11]

        return name, total_ticks
    except (FileNotFoundError, PermissionError, ValueError):
        return None

def get_all_pids():
    pids = [name for name in os.listdir("/proc") if name.isdigit()]
    return pids

