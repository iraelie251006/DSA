import os
import time

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

def take_snapshot():
    system_cpu_time = read_system_cpu_times()
    pids = get_all_pids()
    pids_cpu_time_dict = {}
    for pid in pids:
        pid_cpu_time = read_pid_cpu_time(pid)

        if pid_cpu_time is not None:
            pids_cpu_time_dict[pid] = pid_cpu_time

    (sys_total, sys_idle) = system_cpu_time

    return sys_total, sys_idle, pids_cpu_time_dict

def compute_cpu_percent(snap1, snap2):
    result = []

    for pid in snap1[2].keys():
            if pid in snap2[2]:
                pid_ticks_snap1, pid_ticks_snap2 = snap1[2].get(pid)[1], snap2[2].get(pid)[1]
                sys_total_snap1, sys_total_snap2 = snap1[0], snap2[0]
                cpu_pct = (pid_ticks_snap2 - pid_ticks_snap1) / (sys_total_snap2 - sys_total_snap1) * 100

                pid_cpu_pct = (pid, snap1[2].get(pid)[0], cpu_pct)

                result.append(pid_cpu_pct)
    result.sort(key=lambda x: x[2], reverse=True)
    return result

def format_bar(pct, width=20, num_cpus=1):
    filled = int(min(pct / num_cpus, 100) / 100 * width)
    bar = "█" * filled + "░" * (width - filled)
    return bar

def get_num_cpus():
    count = 0
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("processor"):
                    count += 1
    except FileNotFoundError:
        count = 1
    return max(count, 1)
 
 
def clear_screen():
    print("\033[H\033[J", end="")
