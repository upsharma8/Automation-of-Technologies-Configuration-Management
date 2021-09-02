import os

def roles():
   
    print("Menu for Ansibel_Roles:\nPress 1: For Setting up Haproxy on AWS Cloud\nPress 2: For Setting up Kubernetes Clster on the AWS Cloud")
    while True:
        ch=int(input())
        if ch == 2:
            os.chdir('/root/automation/script/key_script/ansible_roles/kubernetes-role')
            os.system("ansible-playbook kubernete-role.yml --ask-vault-password")
        else:
            print("Setting the haproxy cluster")
