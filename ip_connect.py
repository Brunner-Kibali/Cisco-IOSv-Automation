import subprocess
import platform


def ping_ip(current_ip_address):
    try:
        ping_reply = subprocess.check_output("ping -{} 2 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
        if 'unreachable' in ping_reply:
            return False
        else:
            return True
    except Exception:
        return False
