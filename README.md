# funny-UDP-geolocator

A lightweight packet inspection tool that uses `tshark` and GeoLite2 databases to map observed IP addresses from UDP/TCP traffic to approximate geographic locations.

> ⚠️ This tool is intended for educational and networking experimentation purposes only.

---

## 📦 Setup

### Install dependencies

Run the following before using the script:

```bash
pip install geoip2
```
### Install Wireshark

This tool depends on tshark, which is included with Wireshark.

Download:
https://www.wireshark.org/

### 📁 Required Files

You must download and place the following MaxMind databases in your user directory:

```bash
C:\Users\yourname\
├── GeoLite2-City.mmdb
└── GeoLite2-ASN.mmdb
```
You can obtain these from MaxMind:
https://dev.maxmind.com/geoip/geolite2-free-geolocation-data

Without these files, the program will not function.
### 🧠 What This Tool Does

This script:

Captures network packets using tshark
Extracts source IP addresses from UDP/TCP traffic
Filters out private and noise IPs
Uses GeoLite2 to resolve approximate location data
Filters known infrastructure providers (CDNs, cloud services)
## ⚠️ Important Notes

Many detected IP addresses will belong to infrastructure providers such as:

- Google
- Cloudflare
- Microsoft
- Amazon
- Akamai
- Apple

These are not individual users, but servers, CDNs, or backend services.

### 🚫 Do NOT assume:
That an IP address represents a real person’s location
That geographic results are precise or user-level accurate
### ✔️ What you are actually seeing:
- CDN traffic
- API requests
- Server-to-server communication
- Load-balanced routing infrastructure
## 🔍 How to Interpret Results

To better understand output:

- Short-lived IPs → usually CDN/server infrastructure
- Repeated IPs over time → more likely active communication source
- Private IPs (192.168.x.x, 10.x.x.x) → local network traffic, ignored
## 🛠️ Troubleshooting

If the program does not work:

### 1. Python interpreter mismatch

Ensure you are using the same Python environment where geoip2 is installed. The program prints the version at the top when it launches. Cross reference this with the version of python where you ran the pip command.

### 2. Missing dependencies

Verify installation:

pip install geoip2

### 3. tshark not working

Ensure Wireshark is installed
Verify tshark is available in PATH
Run as administrator if needed

### 4. Database files missing

Confirm .mmdb files are located in C:\Users\yourname\

