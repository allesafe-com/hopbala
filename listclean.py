input_file_path = '/opt/hopbala/output/Hetzner Online GmbH_ipv4.txt'
cleaned_file_path = '/opt/hopbala/output/Hetzner Online GmbH_ipv4.txt'

# Dosyayı oku ve "\n" karakterlerini temizle
with open(input_file_path, 'r') as file:
    content = file.read()
    cleaned_content = content.replace('\\n', '\n').strip()

# Temizlenmiş içeriği yeni dosyaya yaz
with open(cleaned_file_path, 'w') as file:
    file.write(cleaned_content)

print(f"Cleaned content written to {cleaned_file_path}")
