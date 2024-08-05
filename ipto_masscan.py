# Gerekli kütüphaneleri import et
import os

# Girdi dosya yolu
input_file_path = '/opt/hopbala/output/Hetzner Online GmbH_ipv4.txt'

# IP bloklarını oku ve virgülle ayrılmış bir liste oluştur
with open(input_file_path, 'r') as file:
    ip_blocks = file.read().splitlines()

# IP bloklarını virgülle ayrılmış bir string haline getir
target_ip = ','.join(ip_blocks)

# Tarama ayarları
ports = "80,443,5060,8088,8089"
rate = 20000
output_file_path = '/opt/hopbala/masscan_output.json'

# Masscan komutunu oluştur
masscan_command = f"masscan -p{ports} {target_ip} --rate={rate} -oJ {output_file_path}"

# Komutu yazdır
print(f"Generated Masscan command:\n{masscan_command}")
