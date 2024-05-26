import subprocess

def check_adb_devices():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    if "device" not in result.stdout:
        raise RuntimeError("No devices/emulators found. Please connect your device and ensure USB debugging is enabled.")