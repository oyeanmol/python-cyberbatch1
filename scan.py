import socket
import time

# ---------------------------------
# PYTHON CYBER RECON SCANNER
# ---------------------------------

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Alt",
}


def banner():
    print("\n")
    print("╔══════════════════════════════════════════════╗")
    print("║       PYTHON CYBER RECON SCANNER             ║")
    print("╚══════════════════════════════════════════════╝")
    print()


def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.25)

    result = sock.connect_ex((target, port))

    sock.close()

    return result == 0


def main():

    banner()

    print("[!] Scan only systems you own or are")
    print("    explicitly authorized to test.")
    print()

    # -----------------------------
    # USER INPUT
    # -----------------------------

    target = input(
        "Enter target IP/hostname "
        "(press Enter for 127.0.0.1): "
    ).strip()

    if not target:
        target = "127.0.0.1"

    print()
    print(f"[*] Target selected : {target}")

    # Resolve hostname
    try:
        target_ip = socket.gethostbyname(target)

        print(f"[*] Resolved IP     : {target_ip}")

    except socket.gaierror:
        print("[!] Could not resolve target.")
        return

    print("[*] Scan started...")
    print()

    start_time = time.time()

    open_ports = []

    # -----------------------------
    # PORT SCANNING
    # -----------------------------

    for port, service in COMMON_PORTS.items():

        print(
            f"[*] Checking port {port:<5}",
            end="\r"
        )

        if scan_port(target_ip, port):

            open_ports.append(
                (port, service)
            )

            print(
                f"[+] PORT {port:<5} → OPEN   "
                f"({service})"
            )

    # -----------------------------
    # RESULTS
    # -----------------------------

    elapsed = time.time() - start_time

    print()
    print("-" * 50)

    if open_ports:

        print(
            f"[!] {len(open_ports)} "
            f"open port(s) discovered."
        )

        print("\n[+] Discovery Summary:")

        for port, service in open_ports:
            print(
                f"    PORT {port:<5} → {service}"
            )

    else:

        print(
            "[✓] No scanned ports are currently open."
        )

    print()
    print(
        f"[*] Scan completed in "
        f"{elapsed:.2f} seconds."
    )

    print()
    print("╔══════════════════════════════════════════════╗")
    print("║ Python → Network → Cybersecurity             ║")
    print("╚══════════════════════════════════════════════╝")
    print()


if __name__ == "__main__":
    main()

