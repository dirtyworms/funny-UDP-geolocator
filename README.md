funny-UDP-geolocator
Setup

Before running, install dependencies:

pip install geoip2

Also install Wireshark, since this tool relies on tshark.

Required Files

You must place the following MaxMind databases in your user folder:

C:\Users\yourname\
    ├── GeoLite2-City.mmdb
    └── GeoLite2-ASN.mmdb

You can download them from MaxMind’s website.

Without these files, the program will not work.

What it does

This script attempts to identify the source IP addresses of UDP/TCP packets captured via tshark, and then maps them to a geographic location using the GeoLite2 database.

Important Notes
Many detected IPs will belong to infrastructure providers such as Google Cloudflare Microsoft and Amazon
These are not real user locations, but server/CDN endpoints used by websites and apps.

Do not assume these IPs represent actual people, you will often be looking at data center traffic, not user devices. To know whether an IP address belongs to someone, keep in mind that server/CDN endpoints usually only appear briefly, usually interrupted by other server/CDN endpoints, while a real source IP will be repeatedly shown in the terminal so long as it is communicating with you.

Troubleshooting

If the program does not work:

Verify you are using the same Python interpreter where geoip2 is installed
(this is shown at the top of the script if you print sys.executable)
Ensure tshark is installed and accessible
Confirm the .mmdb files are in the correct directory
Run the script from a terminal to see errors (not by double-clicking)

Disclaimer

This project is intended for educational and networking experimentation purposes only. I do not endorse or encourage any misuse of network data or attempts to identify individuals.
