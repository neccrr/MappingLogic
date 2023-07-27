import platform
import subprocess
import os


class SystemUtils:

    # tested on macOS
    @staticmethod
    def getProcessorName():
        raw_brand = None
        try:
            system = platform.system()
            if system == 'Windows':
                # Windows
                cmd = "wmic cpu get caption /value"
                output = subprocess.check_output(cmd, shell=True).strip().decode()
                raw_brand = output.split('=')[1].strip()
            elif system == 'Darwin':
                # macOS
                cmd = "sysctl -n machdep.cpu.brand_string"
                raw_brand = subprocess.check_output(cmd, shell=True).strip().decode()
            elif system == 'Linux':
                # Linux
                with open('/proc/cpuinfo', 'r') as f:
                    for line in f:
                        if 'model name' in line:
                            raw_brand = line.split(':', 1)[1].strip()
                            break
        except Exception as e:
            print("Error:", e)
        return raw_brand

    @staticmethod
    def getUsedMemory():
        if os.name == 'nt':  # Windows
            result = subprocess.check_output(['tasklist', '/FI', 'PID eq {}'.format(os.getpid()), '/FO', 'CSV']).decode()
            mem_info = result.strip().split(',')[-1].replace('"', '').replace(' K', '').replace(',', '')
            return int(mem_info) / 1024  # Convert kilobytes to megabytes
        elif os.name == 'posix':  # macOS and Linux
            result = subprocess.check_output(['ps', '-o', 'rss', '-p', str(os.getpid())]).decode().split('\n')[1].strip()
            return int(result) / 1024  # Convert kilobytes to megabytes
        else:
            raise NotImplementedError("Unsupported platform: {}".format(os.name))

    @staticmethod
    def printSystemInformation():
        print(f"Python version: {platform.python_version()}")
        print(f"Platform: {platform.platform()}")
        print(f"System: {platform.system()}")
        # cpuinfo.get_cpu_info()['brand_raw']
        print(f"Processor: {SystemUtils.getProcessorName()} ({platform.processor()})")
        print(f"Machine: {platform.machine()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Used Memory: {SystemUtils.getUsedMemory()} MB")