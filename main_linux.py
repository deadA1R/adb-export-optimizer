import subprocess
import utils
import var


# A function to execute a script for each URI
def run_script_for_all_uris():
    for component, uris in var.components.items():
        for uri in uris:
            print(f"Executing for {component}: {uri}")
            try:
                subprocess.run([var.script_path, "-e", uri], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing for {uri}: {e}")
            except FileNotFoundError as e:
                print(f"File not found: {e}")
            except PermissionError as e:
                print(f"Permission denied: {e}")

# Starting the function
if __name__ == "__main__":
    try:
        utils.check_adb_devices()
        run_script_for_all_uris()
    except RuntimeError as e:
        print(e)
