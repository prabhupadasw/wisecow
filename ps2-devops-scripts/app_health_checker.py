import requests
import time

URLS_TO_CHECK = [
    "https://wisecow.local",
    "https://google.com",
    "https://github.com"
]

def check_app_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is UP (status: 200)")
            log_result(f"{url} is UP (status: 200)")
        else:
            print(f"{url} is DOWN (status: {response.status_code})")
            log_result(f"{url} is DOWN (status: {response.status_code})")
    except Exception as e:
        print(f"{url} is DOWN (error: {str(e)})")
        log_result(f"{url} is DOWN (error: {str(e)})")

def log_result(message):
    with open("app_health.log", "a") as log_file:
        log_file.write(f"{time.ctime()}: {message}\n")

if __name__ == "__main__":
    for url in URLS_TO_CHECK:
        check_app_health(url)
