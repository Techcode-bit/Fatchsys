import platform
import psutil
import speedtest
import wmi
import socket
from screeninfo import get_monitors
import uuid

def get_installed_software():
    software_list = []
    for app in psutil.process_iter(['pid', 'name']):
        software_list.append(app.info['name'])
    return software_list

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6
    return download_speed, upload_speed

def get_screen_resolution():
    monitors = get_monitors()
    resolutions = [(monitor.width,monitor.height) for monitor in monitors]
    return resolutions

def get_cpu_info():
    return platform.processor()

def get_cpu_cores_threads():
    return psutil.cpu_count(logical=True), psutil.cpu_count(logical=False)

def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu = w.Win32_VideoController()[0]
        return gpu.Caption
    except Exception as e:
        return "No GPU found"

def get_ram_size():
    return round(psutil.virtual_memory().total / (1024 ** 3), 2)

def get_screen_size():
    return "15 inch"

def get_mac_address():
    return (":".join(f"{b:02x}" for b in uuid.getnode().to_bytes(6)))


def get_public_ip():
    return socket.gethostbyname(socket.gethostname())

def get_windows_version():
    return platform.version()

print("1. Installed Software:", get_installed_software())
download_speed, upload_speed = get_internet_speed()
print("2. Internet Speed (Download Speed: {:.2f} Mbps, Upload Speed: {:.2f} Mbps)".format(download_speed, upload_speed))
print("3. Screen Resolution:", get_screen_resolution())
print("4. CPU Model:", get_cpu_info())
cores, threads = get_cpu_cores_threads()
print("5. No of Cores:", cores, "Threads:", threads)
print("6. GPU Model:", get_gpu_info())
print("7. RAM Size:", get_ram_size(), "GB")
print("8. Screen Size:", get_screen_size())
print("9. Mac Address:", get_mac_address())
print("10. Public IP Address:", get_public_ip())
print("11. Windows Version:", get_windows_version())
