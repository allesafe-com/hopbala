# IP aralıklarını tanımla
start_ip_1 = "0.0.0.0"
end_ip_1 = "85.255.255.255"
start_ip_2 = "86.0.0.0"
end_ip_2 = "170.255.255.255"
start_ip_3 = "171.0.0.0"
end_ip_3 = "255.255.255.255"

# Tarama ayarları
ports = "80,443,5060,8088,8089"
rate = 50000
output_file_1 = "masscan_output_1.xml"
output_file_2 = "masscan_output_2.xml"
output_file_3 = "masscan_output_3.xml"

# Masscan komutları
masscan_command_1 = f"sudo masscan {start_ip_1}-{end_ip_1} -p{ports} --rate={rate} -oX {output_file_1} --exclude 255.255.255.255"
masscan_command_2 = f"sudo masscan {start_ip_2}-{end_ip_2} -p{ports} --rate={rate} -oX {output_file_2} --exclude 255.255.255.255"
masscan_command_3 = f"sudo masscan {start_ip_3}-{end_ip_3} -p{ports} --rate={rate} -oX {output_file_3} --exclude 255.255.255.255"

print("Masscan command for IP range 0.0.0.0 - 85.255.255.255:")
print(masscan_command_1)
print("\nMasscan command for IP range 86.0.0.0 - 170.255.255.255:")
print(masscan_command_2)
print("\nMasscan command for IP range 171.0.0.0 - 255.255.255.255:")
print(masscan_command_3)
