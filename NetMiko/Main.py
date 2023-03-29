#This i script to make a excel fil of IOS config.
#We use netmiko and textfsm to parse the output. 
#use pandas to make a excel file.
#
#Author: Magnus Haugen

from getpass import getpass
from netmiko import ConnectHandler

commands = ["show version","show cdp nei detail", "show interfaces","show ip bgp neighbors","show isis nei det", "show ip route stat",  "show vlan", "show vrf det", "show snmp", "show inventory", "show platform","show running-config"]


def userInput():
    #ipaddress = input("Ip address of then device: ")
    #username = input("Username: ")
    #password = getpass("Password: ")
    
    #Hardcoded for testing
    ipaddress = "192.168.111.55"
    username = "admin"
    password = "Magnus123"
    return ipaddress, username, password



def connectToDevice(ipaddress, username, password):
    device = {
        "device_type": "cisco_ios",
        "host": ipaddress,
        "username": username,
        "password": password,
        "secret": password
    }
    print("Connected to device...")
    connect = ConnectHandler(**device)
    print("Connection succesfull")
    return connect

def runCommands(connect,commands):
    output = connect.send_command(commands[0], use_textfsm=True)
    #output = connect.send_command(commands[0])
    print(output)
    
    connect.disconnect()


def main():
    print("Welcome to ARCH")
    print("This is a tool to make a excel file of IOS config")
    print("How do you want to connect to the device?")
    print("1. Ssh to a single device")
    print("2. Ssh to a prefix of devices")
    print("3. Ssh to a from a csv list")

    tasks = input("Choose a number: ")

    if tasks == "1":
        ipaddress, username, password = userInput()
        connect = connectToDevice(ipaddress, username, password)
        runCommands(connect,commands)

    elif tasks == "2":
        print("This funcsion is to ready jet")
        main()
    elif tasks == "3":
        print("This funcsion is to ready jet")
        main()




if __name__ == "__main__":
    main()

