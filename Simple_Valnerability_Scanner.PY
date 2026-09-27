import socket
from datetime import datetime

print("========================================")
print("       SIMPLE VULNERABILITY SCANNER")
print("========================================")

target = "127.0.0.1"

print("\nTarget:", target)
print("Scanning your own computer...")
print("Started at:", datetime.now())

# Common ports for the demonstration
ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

open_ports = []

print("\n----------------------------------------")
print("PORT SCAN RESULTS")
print("----------------------------------------")

for port, service in ports.items():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} ({service}) : OPEN")
        open_ports.append((port, service))
    else:
        print(f"Port {port} ({service}) : CLOSED")

    sock.close()


print("\n========================================")
print("          SCAN SUMMARY")
print("========================================")

print("Target:", target)
print("Open ports found:", len(open_ports))

if len(open_ports) == 0:
    print("No open ports were found in the selected ports.")

else:
    print("\nOpen ports:")

    for port, service in open_ports:
        print(f"- {port} ({service})")

print("\nSecurity Recommendations:")

if 23 in ports and any(port == 23 for port, service in open_ports):
    print("- Telnet is open. Consider disabling it and using SSH instead.")

if any(port == 445 for port, service in open_ports):
    print("- SMB is open. Make sure file sharing is properly secured.")

if any(port == 3389 for port, service in open_ports):
    print("- RDP is open. Make sure remote access is properly secured.")

if len(open_ports) == 0:
    print("- No selected ports are currently open.")

print("\nScan completed at:", datetime.now())

print("\n========================================")
print("             SCAN COMPLETETED")
print("========================================")
