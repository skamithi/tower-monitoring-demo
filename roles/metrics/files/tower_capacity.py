#!/var/lib/awx/venv/ansible/bin/python


"""
Converts the /api/v2/ping/ output from Ansible Tower
into something usable for monitoring purposes.

Input
-------
{
    "active_node": "tower1",
    "ha": true,
    "instance_groups": [
        {
            "capacity": 150,
            "instances": [
                "tower3",
                "tower2",
                "tower1"
            ],
            "name": "tower"
        }
    ],
    "instances": [
        {
            "capacity": 50,
            "heartbeat": "2018-05-10T12:47:21.845Z",
            "node": "tower2",
            "version": "3.2.3"
        },
        {
            "capacity": 50,
            "heartbeat": "2018-05-10T12:47:23.482Z",
            "node": "tower3",
            "version": "3.2.3"
        },
        {
            "capacity": 50,
            "heartbeat": "2018-05-10T12:47:36.446Z",
            "node": "tower1",
            "version": "3.2.3"
        }
    ],
    "version": "3.2.3"
}
-------------


outputs the following:
---------------

tower_system_capacity, host=tower1, sys_capacity=50

Then define a telegraf filter as follows

[[inputs.exec]]
   commands = ['/usr/local/bin/tower_capacity.py']
   data_format  = "influx"


Author: Stanley Karunditu
LICENSE: MIT

"""

from ansible.module_utils.urls import open_url
import json

rsp = open_url( 'http://localhost/api/v2/ping')
output = json.loads(rsp.read())
active_node = output.get('active_node')
sys_capacity = 0
for _instance in output.get('instances'):
     if  _instance.get('node') == active_node:
         sys_capacity = _instance.get('capacity')
         break

print("tower_system_capacity,host=%s value=%s" % (active_node, sys_capacity))
