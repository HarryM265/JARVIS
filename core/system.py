import platform
import psutil

def get_system_status():

    ram = psutil.virtual_memory()

    return (
        f"System operational, sir. "
        f"Memory usage is "
        f"{ram.percent} percent."
    )