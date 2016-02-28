### AutoIP4GNS3
While waiting for AutoNetKit to be added to GNS3 and UNL I decided to create this quick and dirty project to help me automate the basic configs for my labs

This will be more of a POC (proof of concept) than sound code but as is it will save you a lot of time. Due to limited time resource I do not plan to deal with errors or make the code extremely user friendly. If you feel like contributing to this please feel free to branch the code, make the changes and I will gladly add your work to this. 

####How to use it:  

1. Install Python 2.7  
2. Install the exscript, json,pprint, netaddr modules
3. Create your topology in GNS3 (do not configure anything on the devices)  
4. Save your topology  
5. Start your devices, make sure that they are up an drunning before attempting to run the script  
6. The script and the topology file must be in the same folder.   
  ..*-if you want to work with multiple topologies then copy the topology files where the script is  
  ..*-if you modify the topology file quite often then copy the script in folder where the .gns3 project file is  

For Qemu appliances make sure you release the console, the script uses the console to configure the devices. For other appliances 
Make sure yor templates use network interface name formats consitent with what the appliance uses for interface names (ex: GigabitEthernet0/{0})  
  
Before you run the script you need at least to indicate which file you want the script to work with.  
Please change the lines below as per your needs:  
```
TOPOLOGYFILENALE="AutoIP4GNS3-IOS.gns3"         the name of the topology file  (this is a must, you have to change it)  
BASEIP="10.0.0.0/255.255.255.0"                 the IP range that will be subnetted   
BASELOOPIP="192.168.1.0/255.255.255.0"          the IP range used for loopbacks  
SUBNETMASKBITS=30                               subnet mask used for submnetting the BASEIP range  
```  
**Save your configurations manualy or add a line to the script just before the lines that are closing the connction**

####Problems
The script is in its infancy and I am sure that my lab work will force me to improve the script. For now please keep in mind that it was tested on topologies with Cisco routers only. Do not expect this to work on switches :-) unless they are L3 switches

As long as your appliance is listed on the Exscript protocol drivers http://knipknap.github.io/exscript/api/Exscript.protocols-module.html the script should work fine (make sure you have the correct template settings for interface names) 
Report here any problems or suggestions. I will improve the code as the time becomes available.    
  
Have fun.   





