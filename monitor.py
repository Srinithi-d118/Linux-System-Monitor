
import platform
import os
from datetime import datetime

# Project Title
print("======================================")
print("         LINUX SYSTEM MONITOR")
print("======================================")

# 1. System Information
print("\n========== SYSTEM INFORMATION ==========")

print("Computer Name:", platform.node())
print("Operating System:", platform.system())
print("OS Version:", platform.release())
print("Processor Architecture:", platform.processor())
print("Current Directory:", os.getcwd())

# 2. Memory Information
print("\n========== MEMORY INFORMATION ==========")

with open("/proc/meminfo", "r") as file:
    memory_data = file.readlines()

total_memory = memory_data[0]
available_memory = memory_data[2]

print(total_memory.strip())
print(available_memory.strip())

# 3. RAM Usage
total_kb = int(total_memory.split()[1])
available_kb = int(available_memory.split()[1])

used_kb = total_kb - available_kb

total_mb = total_kb / 1024
used_mb = used_kb / 1024

usage_percentage = (used_kb / total_kb) * 100

print("\n========== RAM USAGE ==========")
print("Total RAM:", round(total_mb, 2), "MB")
print("Used RAM:", round(used_mb, 2), "MB")
print("RAM Usage:", round(usage_percentage, 2), "%")

# 4. CPU Information
print("\n========== CPU INFORMATION ==========")

with open("/proc/cpuinfo", "r") as file:
    cpu_data = file.readlines()

for line in cpu_data:
    if "model name" in line:
        print("CPU Model:", line.split(":")[1].strip())
        break

cpu_cores = os.cpu_count()
print("CPU Cores:", cpu_cores)

# 5. Disk Information
print("\n========== DISK INFORMATION ==========")

disk = os.statvfs("/")

total_disk = (disk.f_blocks * disk.f_frsize) / (1024 ** 3)
free_disk = (disk.f_bavail * disk.f_frsize) / (1024 ** 3)
used_disk = total_disk - free_disk

print("Total Disk Space:", round(total_disk, 2), "GB")
print("Used Disk Space:", round(used_disk, 2), "GB")
print("Free Disk Space:", round(free_disk, 2), "GB")

# 6. Date and Time
print("\n========== DATE AND TIME ==========")

current_time = datetime.now()

print("Date:", current_time.strftime("%d-%m-%Y"))
print("Time:", current_time.strftime("%I:%M:%S %p"))

# End
print("\n======================================")
print("   SYSTEM MONITORING COMPLETED!")
print("======================================")
