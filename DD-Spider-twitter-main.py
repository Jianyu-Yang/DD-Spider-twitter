import os
import importlib
import requests
import self as self
import urllib3
# importlib.import_module("python-twitter")

print(os.system('pip install python-twitter'))
print(os.system('pip install requests'))
print(os.system('pip install urllib3'))

def parse_sites(filename):
    with open(filename, "r", encoding='UTF-8') as f:
        raw_sites = f.read().rstrip().lstrip()

    raw_sites = raw_sites.replace("\t", ",") \
                         .replace("\r", ",") \
                         .replace("\n", ",") \
                         .replace(" ", ",")
    raw_sites = raw_sites.split(",")

    sites = list()
    for raw_site in raw_sites:
        site = raw_site.lstrip().rstrip()
        if site:
            sites.append(site)
    return sites

cur_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(cur_dir, "sites.txt")
sites = parse_sites(filename)

for site in sites:
    site = site[0:site.find('%', 1)]
    user_filename = os.path.join(cur_dir, site)
    if os.path.exists(user_filename):
        command = 'twphotos -u ' + site + ' -i'
    else:
        command = 'twphotos -u ' + site
    os.system(command)
input(print("下载已完成，请按任意键退出！"))