import psutil

def check_system_threshold():

    cpu_threshold = int(input("Please enter the CPU usage threshold: "))
    disk_threshold = int(input("Please enter the disk usage threshold: "))
    memory_threshold = int(input("Please enter the memory usage threshold: "))

    current_cpu_usage = psutil.cpu_percent(interval = 1)
    current_disk_usage = psutil.disk_usage('C://').percent
    current_memory_usage = psutil.virtual_memory().percent

    if current_cpu_usage > cpu_threshold:
        print("CPU usage exceed threshold, Alert email sent")
    elif current_disk_usage > disk_threshold:
        print("Disk usage exceed threshold, Alert email sent")
    elif current_memory_usage > memory_threshold:
        print("Memory usage exceed threshold, Alert email sent")
    else:
        print("All the metrics are good")
    print(f"Curret CPU usage: {current_cpu_usage}, Current disk usage: {current_disk_usage}, current memory usage: {current_memory_usage}")

check_system_threshold()
    