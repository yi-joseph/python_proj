# _*_coding: utf-8 _*_
import platform
import psutil
import csv

# Funktion für System-Info
def get_system_info():
    system_info = {
    	"Windows_Version": platform.platform(),
	"RAM_GB": round(psutil.virtual_memory().total / (1024 ** 3), 2),
	"CPU_Cores": psutil.cpu_count(logical=False)
    }
    return system_info

# Funktion für Harddick-Info
def get_disk_info():
    disk_info = []
    partitions = psutil.disk_partitions(all=False)
    for part in partitions:
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disk_info.append({
                "Device": part.device,
                "Mountpoint": part.mountpoint,
                "Filesystem": part.fstype,
                "Total_GB": round(usage.total / (1024 ** 3), 2),
                "Used_GB": round(usage.used / (1024 ** 3), 2),
                "Free_GB": round(usage.free / (1024 ** 3), 2),
                "Percent_Used": usage.percent
	    })
        except PermissionError:
            continue
        
    return disk_info

# Funktion CSV-Datei zu erstellen
def write_to_csv(system_info, disk_info, filename="system_info_v2.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        #System-Info
        writer.writerow(["Systeminformationen "])
        for key, value in system_info.items():
            writer.writerow([key, value])
        writer.writerow([])     # eine leere Zeile zwischen System-Info und Disk-Info
            
        # Disk-Info
        writer.writerow(["Festplatteninformationen "])
        writer.writerow(["Device", "Mountpoint", "Filesystem", "Total_GB", "Used_GB", "Percent_Used"])
        for disk in disk_info:
            writer.writerow([
                disk["Device"],
                disk["Mountpoint"],
                disk["Filesystem"],
                disk["Total_GB"],
                disk["Used_GB"],
                disk["Free_GB"],
                disk["Percent_Used"]
            ])
            # Hauptprogramm
if __name__ == "__main__":
    sys_info = get_system_info()
    disks = get_disk_info()
    write_to_csv(sys_info, disks)
    print("System- und Festplatteninformationen wurden in system_info_v2.csv gespeichert. ")
