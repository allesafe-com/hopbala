import ipaddress
import socket

# Girdi ve çıktı dosya yolları
input_file_path = '/opt/hopbala/Hetzner Online GmbH_ipv4.txt'
output_file_path = '/opt/hopbala/active_ips.txt'

# Portları kontrol eden bir fonksiyon
def is_port_open(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception as e:
        return False

# Hangi portları kontrol edeceğinizi buraya ekleyin
ports_to_check = [80, 443]  # Örneğin HTTP ve HTTPS portları

active_ips = []

# IP bloklarını genişlet ve portları kontrol et
with open(input_file_path, 'r') as file:
    ip_blocks = file.read().splitlines()
    for block in ip_blocks:
        try:
            network = ipaddress.ip_network(block)
            for ip in network:
                if any(is_port_open(str(ip), port) for port in ports_to_check):
                    active_ips.append(str(ip))
        except ValueError as e:
            print(f"Invalid IP block {block}: {e}")

# Aktif IP adreslerini dosyaya yaz
with open(output_file_path, 'w') as file:
    for ip in active_ips:
        file.write(f"{ip}\n")

print(f"Active IP addresses written to {output_file_path}")
