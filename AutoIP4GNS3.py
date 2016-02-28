'''
Created on Feb 27, 2016

@author: wwww.1001qa.net
'''
import json
import pprint
import netaddr
from Exscript.protocols import Telnet

def ConnectEx(server,consoleport):
        #account = read_login()     # Prompt the user for his name and password
        conn = Telnet()
        #conn.debug=5               # Uncomment this if you have problems with connecting to the device
        conn.connect(server,consoleport)
        print "Trying to wake up the console"
        conn.execute("\r\n\r\n") # 
        conn.execute("enable")   #
        #conn.login(account)        # Authenticate on the remote host
        return conn      

BASEIP="10.0.0.0/255.255.255.0"
BASELOOPIP="192.168.1.0/255.255.255.0"
SUBNETMASKBITS=30
TOPOLOGYFILENAME="AutoIP4GNS3-IOS.gns3"
ip=netaddr.IPNetwork(BASEIP)
loopbacks=netaddr.IPNetwork(BASELOOPIP)
loopbackip=loopbacks[0]
subnets=list(ip.subnet(SUBNETMASKBITS))
#print subnets
project= json.loads(open(TOPOLOGYFILENAME).read())
#pprint.pprint(project)
for node in project['topology']['nodes']:
    print node['label']['text']   
    node['Configured']='no'
    for port in (node['ports']):
        port['IP']=unicode('')
        port['Netmask']=unicode('')
        #pprint.pprint (port)
for link in project['topology']['links']:
    print "-------------Link ",link['id']," configuration------------------"
    subnet=subnets.pop(0)    
    for node in project['topology']['nodes']:
        
        if node['id']==link['destination_node_id']:
            node['Configured']='yes'
            print node['label']['text']
            for port in node['ports']:
                if port['id']==link['destination_port_id']:
                    port['IP']=str(subnet[1])
                    port['Netmask']=str(subnet.netmask)
                    pprint.pprint(port)
        if node['id']==link['source_node_id']:
            node['Configured']='yes'
            print node['label']['text']
            for port in node['ports']:
                if port['id']==link['source_port_id']:
                    port['IP']=str(subnet[2])
                    port['Netmask']=str(subnet.netmask)
                    pprint.pprint(port)
        
for node in project['topology']['nodes']:
    for server in project['topology']['servers']:
        if server['id']==node['server_id'] and node['Configured']=='yes':
            print "\nConfiguring node:",node['label']['text']
            conn=ConnectEx(server['host'],node['properties']['console'])
            conn.execute("config term")
            print "\tChanging the hostname to reflect the GNS3 object label"
            conn.execute("hostname "+node['label']['text'])
            print "\tConfiguring the ports"
            for port in node['ports']:
                if port['IP']!='':
                    conn.execute("interface "+port['name'])
                    conn.execute('ip address '+port['IP']+' '+ port['Netmask'])
                    conn.execute('no shut')
            print "\tConfiguring the loopback"
            conn.execute('interface loopback 0')
            loopbackip=loopbackip+1
            conn.execute('ip address '+str(loopbackip)+' '+ '255.255.255.0')
            print "\tConfiguring OSPF"
            conn.execute('router ospf 100')
            conn.execute('network 10.0.0.0 0.0.0.255 area 0')
            conn.execute('network 192.168.1.0 0.0.0.255 area 0')
            print "Closing the connection"        
            conn.execute('exit')
            conn.execute('exit')
            conn.close(force=True)
print """
*****************************************
*                  DONE                 *
*****************************************                     
"""            
