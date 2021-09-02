import getpass

from key_script.aws.aws_menu import Aws
from key_script.docker.docker import docker_main
from key_script.git_gitHub.git_gitHub import github
from key_script.hadoop.hadoop import HadoopMainMenu
from key_script.kubernetes.kubernetes import kube_menu
from key_script.linux.linux_menu import linux
from key_script.ansible_roles.ansible_roles import roles

print("Welcome to Menu Program for Configuration Management of various technologies")
password = getpass.getpass()
if password != "123":
    exit()
path = input("How you want to communicate with this program: [Voice/Keyboard] :")
if path.lower() == 'voice':
    pass
elif path.lower() == 'keyboard':
    while True:
        print("Press 1 : AWS\nPress 2 : Docker\nPress 3 : Hadoop\nPress 5 : Linux/web server\nPress 6 : Git Actions\nPress 7 : Kubernetes Cluster Setup")

        choice = input("\nEnter your choice: ")
        if choice == '1':
            Aws()
        elif choice == '2':
            docker_main()
        elif choice == '3':
            HadoopMainMenu()
        elif choice == '4':
            kube_menu()
        elif choice == '5':
            linux()
        elif choice == '6':
            github()
        elif choice == '6':
            exit(0)
        elif choice == '7':
            roles()
        else:
            print("Wrong Choice!")

else:
    print("Wrong Choice..")


