import os

from key_script.aws.compute.elastic_compute.elastic_compute import EC2Menu


def compute():
    os.system("clear")
    while True:
        os.system('tput setaf 4')
        print('''\n\n\t\tPress 1: EC2\n\t\tPress 2: Elastic BeanStalk\n\t\tPress 3: Exit from this menu''')
        os.system('tput setaf 7')
        choice = input("\n\t\tEnter Your Choice:")
        if choice == '1':
            EC2Menu()
        elif choice == '2':
            pass
        else:
            if choice != '3':
                print("\t\tWrong choice")
            return
        os.system("clear")
