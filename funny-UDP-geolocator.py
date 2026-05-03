import sys
print(sys.executable)
try:
    import geoip2.database
    import socket
    import subprocess
    import ipaddress
    import os

    cmd = r"C:\Program Files\Wireshark\tshark.exe -i 5"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    my_ip = socket.gethostbyname(socket.gethostname())

    base = os.path.expanduser("~")

    reader = geoip2.database.Reader(os.path.join(base, "GeoLite2-City.mmdb"))
    asn_reader = geoip2.database.Reader(os.path.join(base, "GeoLite2-ASN.mmdb"))

    BLOCKED_ORGS = [
        "Google", "Cloudflare", "Microsoft",
        "Amazon", "Akamai", "Apple"
    ]

    def is_bot_infra(ip):
        try:
            asn = asn_reader.asn(ip)
            org = (asn.autonomous_system_organization or "").lower()
            return any(bad.lower() in org for bad in BLOCKED_ORGS)
        except:
            return False

    def is_noise_ip(ip):
        try:
            ip_obj = ipaddress.ip_address(ip)
            return ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_multicast
        except:
            return True

    def get_ip_location(ip):
        try:
            response = reader.city(ip)
            country = response.country.name or "Unknown"
            subdivision = response.subdivisions.most_specific.name or "Unknown"
            city = response.city.name or "Unknown"
            return country, subdivision, city
        except:
            return "Unknown", "Unknown", "Unknown"

    for line in iter(process.stdout.readline, b""): 
        columns = str(line).split(" ")

        if "UDP" in columns or "TCP" in columns or "SKYPE" in columns:

            if "->" in columns:
                src_ip = columns[columns.index("->") - 1]
            elif "\\xe2\\x86\\x92" in columns:
                src_ip = columns[columns.index("\\xe2\\x86\\x92") - 1]
            else:
                continue

            if src_ip == my_ip:
                continue

            if is_noise_ip(src_ip):
                continue

            if is_bot_infra(src_ip):
                continue

            try:
                country, sub, city = get_ip_location(src_ip)
                print(f">>> {country}, {sub}, {city}")

            except Exception as e:
                try:
                    real_ip = socket.gethostbyname(src_ip)
                    country, sub, city = get_ip_location(real_ip)
                    print(f">>> {country}, {sub}, {city}")

                except Exception as e2:
                    print("Error:", e2)

except Exception as e:
    print("Script crashed:")
    print(e)

input("Press Enter to exit...")
