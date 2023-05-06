import requests

# Define the list of URLs
urls = [
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/ultimate.txt',
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/doh.txt',
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/native.winoffice.txt',
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/native.tiktok.txt',
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/native.apple.txt',
]

# Fetch the host lists and merge them into one
hosts = set()

for url in urls:
    response = requests.get(url)
    hosts.update(response.text.strip().split('\n'))

# Remove duplicate hosts
hosts = set(hosts)

# Remove lines that contain specific patterns
patterns = [
    'www.effectivecreativeformat.com',
    'myniceposts.com',
]

hosts = [host for host in hosts if not any(pattern in host for pattern in patterns)]

# Write the merged and cleaned up host list to a file
with open('hosts.txt', 'w') as f:
    f.write('\n'.join(hosts))
