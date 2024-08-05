import csv
import json
import os

# CSV dosyasının tam yolu
csv_file_path = 'D:\Github\hopbala\geoip2_asn_list.csv.csv'
json_file_path = 'D:\Github\hopbala\geoip_database.json'

# Dosya yolunun doğruluğunu kontrol etme
if not os.path.exists(csv_file_path):
    print(f"Error: CSV file not found at {csv_file_path}")
    exit(1)

# JSON verilerini saklayacak dictionary
geoip_data = {}

# CSV dosyasını oku
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        organization = row['autonomous_system_organization']
        ip_range = row['network']
        asn = row['autonomous_system_number']
        
        if organization not in geoip_data:
            geoip_data[organization] = {'ipv4': [], 'asn': asn}
        
        geoip_data[organization]['ipv4'].append(ip_range)

# JSON verilerini dosyaya yaz
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(geoip_data, json_file, indent=4)

print(f"JSON veritabanı '{json_file_path}' dosyasına yazıldı.")
