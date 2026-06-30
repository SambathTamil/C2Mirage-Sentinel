import subprocess
from notifications.telegram_notifier import send_alert

def scan_file(file_path):

    rule_file = "rules/malware_rules.yar"
    yara_path = "yara.exe"

    try:
        result = subprocess.check_output(
            [yara_path, rule_file, file_path],
            stderr=subprocess.STDOUT
        )

        output = result.decode()

        if output:
            print("YARA detection:", output)

            send_alert(f"🚨 YARA Detection Alert\n{output}")

            return True

        else:
            return False

    except subprocess.CalledProcessError:
        return False