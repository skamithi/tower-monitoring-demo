#!/var/lib/awx/venv/ansible/bin/python


"""
Telegraf exec script

Helps detect rabbitmq status. Checks if any network partitions are detected and
how many hosts are partitioned.


Author: Stanley Karunditu
LICENSE: MIT

"""

from ansible.module_utils.urls import open_url
from socket import gethostname;
import json

rsp = open_url( 'http://localhost:15672/api/nodes/',
               url_username='guest',
               url_password='guest')
output = json.loads(rsp.read())
_hostname = gethostname()
partitions = []
for entry in output:
    if entry.get('name').split('@')[1] in _hostname:
        partitions = entry.get('partitions')
        break
print("tower_network_partitions,host=%s partitions=\"%s\",length=%s" % (_hostname, ';'.join(partitions), len(partitions)))

