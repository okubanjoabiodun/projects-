firewall_rules = [{"ip": "192.168.1.1", "port": 80, "action": "allow"},
                  {"ip": "192.168.1.2", "port": 443, "action": "deny"},
                    {"ip": "192.168.1.3", "port": 22, "action": "allow"},
                    {"ip": "192.168.1.4", "port": 23, "action": "deny"},
                    {"ip": "192.168.1.5", "port": 8080, "action": "allow"},
                    {"ip": "192.168.1.6", "port": 3389, "action": "deny"}]


def check_firewall(ip, port):
    for rule in firewall_rules:
        if rule["ip"] == ip and  rule["port"] == port:
            return rule["action"]

ip = input("Enter the IP address: ")
port = int(input("Enter the port number: "))
action = check_firewall(ip, port)
if action == "allow":
    nam = f"Reply from {ip}: bytes=32 time<1ms TTL=128."
    for i in range(4):
        print(nam)
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),")
    print(f"Approximate round trip times in milli-seconds:")
    print(f"    Minimum = 0ms, Maximum = 0ms, Average = 0ms")
    print(f"Access granted for IP {ip} on port {port}.")
else:
    fi = f"Reply from {ip}: Destination host unreachable."
    for i in range(4):
        print(fi)
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),")
    print(f"Approximate round trip times in milli-seconds:")
    print(f"    Minimum = 0ms, Maximum = 0ms, Average = 0ms")
    print(f"Access denied for IP {ip} on port {port}.")
