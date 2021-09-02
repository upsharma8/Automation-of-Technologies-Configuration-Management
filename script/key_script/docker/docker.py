import getpass
import os
from distutils.spawn import find_executable

"""
35.154.213.32
/root/Desktop/FYProject/script/key_script/kubernetes/installation/Ansible/ARTH.pem
"""


########################################
def docker_installation_service(username='root', ip='localhost', password="", key=""):
    os.chdir('key_script/docker/')
    if password != '':
        with open("Ansible/inventory", "w+") as inventory:
            inventory.write(f"{ip} ansible_user={username} ansible_ssh_pass={password}\n")
    elif key != '':
        with open("Ansible/inventory", "w+") as inventory:
            inventory.write(f"{ip} ansible_user={username} ansible_ssh_private_key_file={key}\n")
    elif password is '' and key is '' and ip is 'localhost':
        with open("Ansible/inventory", "w+") as inventory:
            inventory.write(f"{ip} ansible_connection=local\n")
    else:
        print("wrong info")
        return

    os.chdir(os.getcwd() + '/Ansible')

    if not find_executable("ansible") is None:
        os.system(f"ansible-playbook setup.yml")
    else:
        os.system(f"ansible-playbook setup.yml")

    os.chdir(os.getcwd() + "/../")
    os.chdir('../../')


def local_docker_image():
    while True:
        os.system('tput setaf 4')
        print("""\n\t\tEnter 1 to list\n\t\tEnter 2 to pull\n\t\tEnter 3 to remove image\n\t\tEnter 4 to docker menu""")
        os.system('tput setaf 7')

        choice = input("\t\tEnter : ")
        if choice == '1':
            os.system("docker images")
        if choice == "2":
            image = input("\t\tEnter image  name[os]:version ")
            os.system("docker pull {}".format(image))
        elif choice == "3":
            image = input("\t\tEnter image  name[os:version]: ").strip()
            os.system("docker rmi {}".format(image))
        elif choice == "4":
            return
        else:
            print("\t\twrong choice")
        input("\t\tEnter to continue..")
        os.system("clear")


def local_docker_container_service():
    while True:
        os.system('tput setaf 4')
        print(
            "\n\t\tEnter 1 to see running containers\n\t\tEnter 2 to see all containers\n\t\tEnter 3 to create container\n\t\tEnter 4 to delete container\n\t\tEnter 5 to stop container\n\t\tEnter 6 to start container\n\t\tEnter 7 to docker menu")
        os.system('tput setaf 7')
        choice = input("\t\tEnter your choice : ")
        if choice == '1':
            os.system("docker  ps -a")
        elif choice == "2":
            os.system("docker ps")
        elif choice == '3':
            name = input("\t\tEnter name: ")
            osname = input("\t\tEnter image [:]")
            os.system("docker  run  -dit --name {}  {}".format(name, osname))
        elif choice == '4':
            name = input("\t\tEnter name/ID: ")
            os.system("docker rm -f {}".format(name))
        elif choice == '5':
            name = input("\t\tEnter name/ID: ")
            os.system("docker stop {}".format(name))
        elif choice == '6':
            name = input("\t\tEnter name/ID: ")
            os.system("docker start {}".format(name))
        elif choice == '7':
            return
        else:
            print("\t\tWrong choice")
        input("\t\tEnter to continue...")
        os.system("clear")


####################################################
# PassOS#
#####################################################
def remote_docker_Image_service(username, password, IP):
    while True:
        os.system('tput setaf 4')
        print("""\n\t\tEnter 1 to list\n\t\tEnter 2 to pull\n\t\tEnter 3 to remove image\n\t\tEnter 4 to docker menu""")
        os.system('tput setaf 7')

        choice = input("\n\t\tEnter : ")

        if choice == "1":
            image = input("\t\tEnter image  name[os]:version ")
            os.system("sshpass -p {} ssh {}@{} sudo docker pull {}".format(username, password, IP, image))
        elif choice == "2":
            image = input("\t\tEnter image  name[os:version]: ").strip()
            os.system("sshpass -p {} ssh {}@{} sudo docker rmi {}".format(username, password, IP, image))
        elif choice == "3":
            return
        else:
            print("\t\twrong choice")

        input("\t\tEnter to continue..")
        os.system("clear")


def remote_docker_container_service(username, password, IP):
    while True:
        os.system('tput setaf 4')
        print("""\n\t\tEnter 1 to see running containers\n\t\tEnter 2 to see all containers\n\t\tEnter 3 to create container\n\t\tEnter 4 to delete container\n\t\tEnter 5 to stop container
        \t\tEnter 6 to start container\n\t\tEnter 7 to docker menu""")
        os.system('tput setaf 7')
        choice = input("\t\tEnter: ")
        if choice == '1':
            os.system("sshpass -p {} ssh {}@{} sudo docker  ps -a")
        elif choice == "2":
            os.system("sshpass -p {} ssh {}@{} sudo docker ps")
        elif choice == '3':
            name = input("\t\tEnter name: ")
            osname = input("\t\tEnter image [:]")
            os.system("sshpass -p {} ssh {}@{} sudo docker run -dit --name {} {}".format(password, username, IP, name,
                                                                                         osname))
        elif choice == '4':
            name = input("\t\tEnter name/ID: ")
            os.system("sshpass -p {} ssh {}@{} sudo docker rm -f {}".format(password, username, IP, name))
        elif choice == '5':
            name = input("\t\tEnter name/ID: ")
            os.system("sshpass -p {} ssh {}@{} sudo docker stop {}".format(password, username, IP, name))
        elif choice == '6':
            name = input("\t\tEnter name/ID: ")
            os.system("sshpass -p {} ssh {}@{} sudo docker start {}".format(password, username, IP, name))
        elif choice == '7':
            return
        else:
            print("\t\tWrong choice")
        input("\t\tEnter to contine..")
        os.system("clear")


############################################
# KeyOS#
############################################
def key_docker_Image_service(path, username, IP):
    while True:
        os.system('tput setaf 4')
        print("""\n\t\tEnter 1 to pull\n\t\tEnter 2 to remove image\n\t\tEnter 3 to docker menu""")
        os.system('tput setaf 7')
        choice = input("\t\tEnter : ")
        if choice == "1":
            image = input("\t\tEnter image  name[os]:version ")
            os.system("ssh -i  {} {}@{} sudo docker pull {}".format(path, username, IP, image))
        elif choice == "2":
            image = input("\t\tEnter image  name[os:version]: ").strip()
            os.system("ssh -i  {} {}@{} sudo docker rmi {}".format(path, username, IP, image))
        elif choice == "3":
            return
        else:
            print("\t\twrong choice")
        input("\t\tEnter to continue..")
        os.system("clear")


def key_docker_container_service(path, username, IP):
    while True:
        os.system('tput setaf 4')
        print(
            "\n\t\tEnter 1 to see running containers\n\t\tEnter 2 to see all containers\n\t\tEnter 3 to create container"
            "\n\t\tEnter 4 to delete container\n\t\tEnter 5 to stop container\n\t\tEnter 6 to start container\n\t\tEnter 7 to docker menu")
        os.system('tput setaf 7')
        choice = input("\t\tEnter: ")
        if choice == '1':
            os.system("ssh -i  {} {}@{} sudo docker  ps -a")
        elif choice == "2":
            os.system("ssh -i  {} {}@{} sudo docker ps")
        elif choice == '3':
            name = input("\t\tEnter name: ")
            osname = input("\t\tEnter image [:]")
            os.system("ssh -i  {} {}@{} sudo docker run -dit --name {} {}".format(path, username, IP, name, osname))
        elif choice == '4':
            name = input("\t\tEnter name/ID: ")
            os.system("ssh -i  {} {}@{} sudo docker rm -f {}".format(path, username, IP, name))
        elif choice == '5':
            name = input("\t\tEnter name/ID: ")
            os.system("ssh -i  {} {}@{} sudo docker stop {}".format(path, username, IP, name))
        elif choice == '6':
            name = input("\t\tEnter name/ID: ")
            os.system("ssh -i  {} {}@{} sudo docker start {}".format(path, username, IP, name))
        elif choice == '7':
            return
        else:
            print("\t\tWrong choice")
        input("\t\tEnter to continue...")
        os.system("clear")


#############################################################
# MainMenu#
##############################################################
def local_docker_menu():
    while True:
        os.system('tput setaf 4')
        print(
            "\n\t\tEnter 1 to install docker\n\t\tEnter 2 to check docker info\n\t\tEnter 3 to work with Container Images "
            "\n\t\tEnter 4 to container operations\n\t\tEnter 5 to main menu")
        os.system('tput setaf 7')
        choice = input("\n\t\tEnter your choice: ")
        if choice == "1":
            docker_installation_service(username=input("\t\tuser-name: "))
        elif choice == '2':
            os.system("docker info")
        elif choice == '3':
            local_docker_image()
        elif choice == '4':
            local_docker_container_service()
        elif choice == '5':
            return
        else:
            print("\t\tWrong choice")
        input("\t\tEnter to continue... ")
        os.system("clear")


def remote_pass_menu(username, password, IP):
    while True:
        os.system('tput setaf 4')
        print(
            "\n\t\tEnter 1 to install docker\n\t\tEnter 2 to check docker info\n\t\tEnter 3 to work with Container Images "
            "\n\t\tEnter 4 to container operations\n\t\tEnter 5 to main menu")
        os.system('tput setaf 7')

        choice = input("\n\t\tEnter your choice: ")
        if choice == "1":
            docker_installation_service(username=username, ip=IP, password=password)

        elif choice == '2':
            os.system("sshpass -p {} ssh {}@{} sudo docker info".format(password, username, IP))
        elif choice == '3':
            remote_docker_Image_service(username, password, IP)
        elif choice == '4':
            remote_docker_Image_service(username, password, IP)
        elif choice == '5':
            return
        else:
            print("\t\tWrong choice")
        input("\t\tEnter to continue... ")
        os.system("clear")


def key_docker_os(path, username, IP):
    while True:
        os.system('tput setaf 4')
        print(
            "\t\tEnter 1 to install docker\n\t\tEnter 2 to check docker info\n\t\tEnter 3 to work with Container Images "
            "\n\t\tEnter 4 to container operations\n\t\tEnter 5 to main menu")
        os.system('tput setaf 7')

        choice = input("\n\t\tEnter your choice: ")
        if choice == "1":
            docker_installation_service(username=username, ip=IP, key=path)
        elif choice == '2':
            os.system("ssh -i {} {}@{} sudo docker info".format(path, username, IP))
        elif choice == '3':
            key_docker_Image_service(path, username, IP)
        elif choice == '4':
            key_docker_container_service(path, username, IP)
        elif choice == '5':
            return
        else:
            print("\t\tWrong choice")
        input("\t\tEnter to continue... ")
        os.system("clear")


def docker_main():
    os_type = input("\n\t\tEnter local to work on local operating system\n"
                    "\t\tEnter remote to work on remote operating system\n"
                    "\t\t:")
    if os_type == "local":
        local_docker_menu()
    elif os_type == 'remote':
        IP = input("\t\tEnter IP Address : ")
        username = input("\t\tEnter username : ")
        key_or_pass = input("\t\tLogin using Key or password : ")
        if key_or_pass == "password":
            password = getpass.getpass()
            remote_pass_menu(username, password, IP)
        elif key_or_pass.lower() == "key":
            path = input("\t\tEnter key path [path/key.pem] : ")
            key_docker_os(path, username, IP)
        else:
            print("\t\tWrong Choice")
    else:
        print("\t\tWrong Choice")
        return
