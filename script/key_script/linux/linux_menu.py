import os
import subprocess

from key_script.linux.logical_volume_manager.lvm import LVM
from key_script.linux.webservers.webserver import webserverMain


def key_pass():
    ipAddress = input("\t\t\tEnter IP of target System :")
    username = input("\t\t\tUserName: ")
    auth_type = input("\t\t\tEnter Authentication type-->  [key/password] : ")

    if auth_type.lower() == "key":
        key_path = input("\t\t\tEnter key and path from base directory: ")
        cmd = input("\t\t\tEnter cmd : ")
        os.system(f"ssh -i  {key_path} {username}@{ipAddress} sudo {cmd}")
    elif auth_type.lower() == "password" or auth_type.lower() == "pass":
        print("\t\t\tSetting Up environment please wait")
        subprocess.getoutput("yum install sshpass -y")
        password = input("\t\t\tEnter password: ")
        cmd = input("\t\t\tEnter cmd : ")
        os.system(f"ssh -p {password} {username}@{ipAddress} sudo {cmd}")
    else:
        print("\t\t\tNot Valid")
        return


def linux():
    print("\n\t\tPress 1: For Running any command\n\t\tPress 2: For Logical Volume Manager\n\t\tPress 3: Apache Webserver Configuration\n\t\tPress 4: Exit")

    choice = input("\t\tEnter your choice: ")
    if choice == '1':
        key_pass()
    elif choice == '2':
        LVM()
    elif choice == '3':
        webserverMain()
    elif choice == '4':
        return
    else:
        print("\n\t\tWrong Choice!")
    input("\n\t\tEnter to continue...")
    os.system("clear")


