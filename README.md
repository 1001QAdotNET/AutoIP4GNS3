### AutoIP4GNS3
While waiting for AutoNetKit to be added to GNS3 and UNL I decided to create this quick and dirty project to help me automate the basic configs for my labs

This will be more of a POC (proof of concept) than sound code. Due to limited time resource I do not plan to deal with errors or make the code extremely user friendly. If you feel like contributing to this please feel free to branch the code, make the changes and I will gladly add your work to this. 

####How to use it:  

1. Install Python 2.7  
2. Install Exscript (https://github.com/knipknap/exscript/wiki/Installation-Guide)  
3. Create your topology in GNS3  
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
TOPOLOGYFILENALE="AutoIP4GNS3-IOS.gns3"         the name of the topology file  (this is a must, ou have to change it)  
BASEIP="10.0.0.0/255.255.255.0"                 the IP range that will be subnetted   
BASELOOPIP="192.168.1.0/255.255.255.0"          the IP range used for loopbacks  
SUBNETMASKBITS=30**                             subnet mask used for submnetting the BASEIP range  
```  
Report here any problems or suggestions. I will improve the code as the time becomes available.    
  
Have fun.   





