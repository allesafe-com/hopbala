import ipaddress
import socket

# IP aralığı belirleme
start_ip = ipaddress.IPv4Address('0.0.0.0')
end_ip = ipaddress.IPv4Address('255.255.255.255')

# Portları kontrol eden bir fonksiyon
def is_port_open(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((str(ip), port))
        sock.close()
        return result == 0
    except Exception as e:
        return False

# Hangi portları kontrol edeceğinizi buraya ekleyin
ports_to_check = [80, 443, 5060, 8088]  # Örneğin HTTP ve HTTPS portları

active_ips = []

# IP aralığını genişlet ve portları kontrol et
for ip_int in range(int(start_ip), int(end_ip) + 1):
    ip = ipaddress.IPv4Address(ip_int)
    if any(is_port_open(ip, port) for port in ports_to_check):
        active_ips.append(str(ip))

# Aktif IP adreslerini dosyaya yaz
output_file_path = 'active_ips.txt'
with open(output_file_path, 'w') as file:
    for ip in active_ips:
        file.write(f"{ip}\n")

print(f"Active IP addresses written to {output_file_path}")
