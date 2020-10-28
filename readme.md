# ARCH
ARCH is a tool for documentation of Cisco devices(mainly IOS-XE routers).   

Usually, you would use Ansible with TextFSM, Nornir, or Genie if you have that available.  
But if you only have SecureCRT (with a small libery) or in a limeted python Enviorment then ARCH can be used. 


ARCH have three standalone parts.  

## Part 1: Geahter informatsion  
[Using SecureCRT:](https://github.com/LetMeGoogleIt4You/ARCH/blob/master/Part1/SecureCRT.md)  

[Using Netmiko(Alternativ):](https://github.com/LetMeGoogleIt4You/ARCH/blob/master/Part1/Netmiko.md)    

## Part 2: Parse informasion and create a csv files  
[Using SecureCRT or Python:](https://github.com/LetMeGoogleIt4You/ARCH/blob/master/Part2/readme.md)  

## Part 3: Create one excel file from all csv file   
[Using Python (Not SecureCRT combability jet):](https://github.com/LetMeGoogleIt4You/ARCH/blob/master/Part3/readme.md)  


## Nots

ARCH is still under development, so bugs and changes can occur.     
This tool mainly focues on ISR and ASR routers should work on most IOS-XE devices.  

If you want to do some development, testing on your own feel free to do so.  
also, there are some notebooks for easy troubleshooting in the [Dev folder](https://github.com/LetMeGoogleIt4You/ARCH/blob/master/Dev/readme.md)




