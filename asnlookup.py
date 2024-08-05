#!/usr/bin/python

import sys
import json
import argparse
import os
from termcolor import colored

def banner():
    print('''\\n
    ____ ____ _  _ _    ____ ____ _  _ _  _ ___\\n
    |__| [__  |\\ | |    |  | |  | |_/  |  | |__]\\n
    |  | ___] | \\| |___ |__| |__| | \\_ |__| |\\n
                    asnlookup.com\\n
     Author: Yassine Aboukir (@yassineaboukir)\\n''')

def parse_args():
    # parse the argument
    parser = argparse.ArgumentParser(epilog='\\tExample: \\r\\npython ' + sys.argv[0] + ' -o twitter')
    org = parser.add_argument('-o', '--org', help='Organization to look up.', required=True)
    nmapscan = parser.add_argument('-n', '--nmapscan', help='Run Nmap port scanning.', required=False, action='store', nargs='?', const='-p 1-65535 -T4 -A -v')
    masscan = parser.add_argument('-m', '--masscan', help='Run Masscan port scanning.', required=False, action='store', nargs='?', const='-p0-65535 --rate 200')
    return parser.parse_args()

def get_ip_space(organization):
    # retrieve ip space from local database
    try:
        with open('geoip_database.json', 'r') as db_file:
            ip_space = json.load(db_file).get(organization, {})
    except Exception as e:
        print(colored('[!] Couldn\'t read local geoip database: {}'.format(e), 'red'))
        sys.exit(1)

    if ip_space:
        path_ipv6 = os.path.dirname(os.path.realpath(__file__)) + '/output/' + organization + '_ipv6.txt'
        path_ipv4 = os.path.dirname(os.path.realpath(__file__)) + '/output/' + organization + '_ipv4.txt'
        ipv4_exist =  False
        ipv6_exist =  False

        if not os.path.exists('output'):
            os.makedirs('output')
        elif os.path.isfile('./output/' + organization + '.txt') == True:
            os.system('cd ./output/ && rm -f ' + organization + '.txt')

        for ip_range in ip_space.get('ipv4', []):
            ipv4_exist = True
            with open(path_ipv4, 'a') as ipv4_file:
                ipv4_file.write(ip_range + '\\n')

        for ip_range in ip_space.get('ipv6', []):
            ipv6_exist = True
            with open(path_ipv6, 'a') as ipv6_file:
                ipv6_file.write(ip_range + '\\n')

        if ipv4_exist:
            print(colored('[+] IPv4 addresses are stored in: ' + path_ipv4, 'green'))
        if ipv6_exist:
            print(colored('[+] IPv6 addresses are stored in: ' + path_ipv6, 'green'))
    else:
        print(colored('[!] No IP space found for organization: ' + organization, 'red'))
        sys.exit(1)

if __name__ == '__main__':
    banner()
    args = parse_args()
    get_ip_space(args.org)
