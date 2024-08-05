import os
import time
import subprocess
from datetime import datetime, timedelta

# Masscan komutu
masscan_command = [
    'sudo', 'masscan', '0.0.0.0/0', '-p80,443,5060,8088,8089', '--rate=10000', 
    '-oX', 'masscan_output-80506080888089.xml', '--exclude', '255.255.255.255'
]

# Çalışma ve uyuma süreleri (saniye cinsinden)
run_time = 300  # 5 dakika çalıştır
sleep_time = 120  # 2 dakika uyut

def print_current_time(label):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{label} at: {current_time}")

while True:
    # Başlama zamanını göster
    print_current_time("Masscan started")
    print(f"Running Masscan for {run_time} seconds...")

    process = subprocess.Popen(masscan_command)

    # Belirli süre çalıştır
    time.sleep(run_time)

    # Masscan'ı durdur
    print(f"\nStopping Masscan...")
    process.terminate()
    process.wait()  # Process'in tamamen durdu
