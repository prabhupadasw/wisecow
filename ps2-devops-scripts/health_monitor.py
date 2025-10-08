import psutil
import time

# Thresholds
CPU_THRESHOLD = 80     # percent
MEM_THRESHOLD = 80     # percent
DISK_THRESHOLD = 90    # percent

def log_alert(message):
    with open("health_alerts.log", "a") as log_file:
        log_file.write(f"{time.ctime()}: {message}\n")

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    process_count = len(psutil.pids())

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {mem}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {process_count}")

    if cpu > CPU_THRESHOLD:
        print("ALERT: CPU usage high!")
        log_alert("CPU usage high!")
    if mem > MEM_THRESHOLD:
        print("ALERT: Memory usage high!")
        log_alert("Memory usage high!")
    if disk > DISK_THRESHOLD:
        print("ALERT: Disk space usage high!")
        log_alert("Disk space usage high!")

if __name__ == "__main__":
    try:
        while True:
            check_system_health()
            print("-" * 40)
            time.sleep(10)  # Wait 10 seconds before next check
    except KeyboardInterrupt:
        print("System health monitor stopped.")
