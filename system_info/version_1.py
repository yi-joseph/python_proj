# _*_ coding: utf-8 -*-
import platform
import psutil
import csv
from datetime import datetime

def get_system_info():
    info = {
        "Zeitpunkt": datetime.now().strftime("%Y-%M-%D %H:%M:%S"),
        "Windows_Version": platform.platform(),
        "RAM_GB": round(psutil.virtual_memory().total/(1024 ** 3), 2),
        "CPU_Kerne": psutil.cpu_count(logical=False)
    }
    return info

def write_to_csv(info, filename="system_info_v1.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Feld", "Wert"])
        for key, value in info.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    system_info = get_system_info()
    write_to_csv(system_info)
    print("Systeminformation wurden in 'system_info_v1.csv' gespeichert.")
    
