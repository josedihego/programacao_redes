#pip3 install geoip2
# https://dev.maxmind.com/geoip/geolite2-free-geolocation-data
# https://github.com/P3TERX/GeoLite.mmdb
# https://git.io/GeoLite2-City.mmdb
# pip3 install cartopy

from scapy.all import *
from scapy.layers.inet import traceroute_map

from scapy.layers.inet import traceroute
#conf.geoip_city = "geo_base/GeoLite2-City.mmdb"
#a, _ = traceroute(["www.google.co.uk", "www.secdev.org"], verbose=0)
#a.world_trace()


conf.geoip_city = "geo_base/GeoLite2-City.mmdb"
traceroute_map(["www.google.co.uk", "www.secdev.org"], notifier=1)
