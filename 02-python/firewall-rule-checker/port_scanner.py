import os 
import sys  
import ipaddress
from scapy.all import ICMP , IP , sr1


class IPNetwork:
    """Small concrete IPv4/IPv6 network implementation used by the scanner."""

    def __init__(self, address):
        self._network = ipaddress.ip_network(address, strict=False)

    def __str__(self):
        return str(self._network)

    def __contains__(self, address):
        return ipaddress.ip_address(address) in self._network

    def __iter__(self):
        return iter(self._network)

    def __len__(self):
        return self._network.num_addresses

    def iter_hosts(self):
        """Yield usable host addresses, excluding network andgbroadcast addresses."""
        return self._network.hosts()

def ping_sweep(network, netmask):
    live_hosts = []
    total_hosts = 0
    scanned_hosts = 0

    ip_network = IPNetwork(network + '/' + netmask)
    total_hosts = len(list(ip_network.iter_hosts()))

    for host in ip_network. iter_hosts():
        scanned_hosts += 1
        print(f"Scanning: {scanned_hosts}/{total_hosts}", end="\r")
        response = sr1(IP(dst=str(host)) / ICMP(), Timeout=1, verbose=0)
        if response is not None:
            live_hosts.append(str(host))
            print(f"Host {host} is online")

    return live_hosts


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(f"Usage: {sys.argv[0]} <network> <netmask>")
    ping_sweep(sys.argv[1], sys.argv[2])

