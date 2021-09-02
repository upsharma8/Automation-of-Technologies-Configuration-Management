import getpass
import os
import subprocess


def run():
    os.chdir("Ansible/")
    os.system("ansible-playbook webserver.yml")
    os.chdir("../")


def webserverMain():
    os.chdir("key_script/linux/webservers/")
    while True:
        print(
            "\n\t\t\tEnter 1 to Configure on Local System\n\t\t\tEnter 2 to Configure on remote system\n\t\t\tEnter 3 to return")

        choice = input("\t\t\tEnter  your choice: ")
        if choice == "1":
            with open("Ansible/inventory", "w+") as inventory:
                inventory.write("localhost")
            run()
        elif choice == "2":
            ip = input("\t\t\tEnter IP address: ")
            username = input("\t\t\tEnter username: ")
            key_or_pass = input("\t\t\tLogin in VM using key/password: ")
            if key_or_pass == "password":
                password = getpass.getpass()
                with open("Ansible/inventory", "w+") as inventory:
                    inventory.write(f"{ip} ansible_user={username} ansible_ssh_pass={password}\n")
                run()

            elif key_or_pass.lower() == "key":
                path = input("\t\t\tEnter remote os login key path [path/key.pem] ")
                with open("Ansible/inventory", "w+") as inventory:
                    inventory.write(f"{ip} ansible_user={username} ansible_ssh_private_key_file={path}\n")
                run()
            else:
                print("\t\t\tWrong choice")

        elif choice == '3':
            os.chdir("../../../")
            return
        else:
            print("\t\t\tWrong choice!\n try again..")
