import os


def installation():
    os.chdir("key_script/kubernetes/installation")

    from distutils.spawn import find_executable

    os.chdir(os.getcwd() + '/Ansible')
    if find_executable("pip3") is None:
        os.system(f"ansible-playbook python3.yml")

    os.chdir(os.getcwd() + "/../")

    os.system("ansible-galaxy install rohitraut3366.kubernetes_master_node")
    os.system("ansible-galaxy install rohitraut3366.kubernetes_slave_node")

    print("\t\t\tEnter details of nodes")
    print("\t\t\t\t\t\t****Master-Details****")
    ip = input("\t\t\tEnter IP address of Master Node: ").strip()
    user_name = input("\t\t\tBase operating system username: [NOTE: User must have privileges]: ").strip()
    pass_or_key = input("\t\t\tEnter Authentication type: 'P' for password or 'K' for Key: ").strip()
    if pass_or_key is "K":
        key = input("\t\t\tEnter private key name & location with complete path: path/key.ppk").strip()
        with open("Ansible/inventory", "w+") as inventory:
            inventory.write("[tag_Name_K8S_Master]\n")
            inventory.write(f"{ip} ansible_user={user_name} ansible_ssh_private_key_file={key}\n")

    elif pass_or_key is 'P':
        password = input("\t\t\tEnter password required to login: ").strip()
        with open("Ansible/inventory", "w+") as inventory:
            inventory.write("[tag_Name_K8S_Master]\n")
            inventory.write(f"{ip} ansible_user={user_name} ansible_ssh_pass={password}\n")

    else:
        print("\t\t\tWrong Choice! \n\t\t\tPlease try again...")

    print("\t\t\t\t\t\t****Slave-Node-Details****")
    number_of_nodes = int(input("\t\t\tEnter number of nodes: "))
    for n in range(number_of_nodes):
        ip = input("\t\t\tEnter IP address of Slave Node: ").strip()
        user_name = input("\t\t\tBase operating system username: [NOTE: User must have privileges]: ").strip()
        pass_or_key = input("\t\t\tEnter Authentication type: 'P' for password or 'K' for Key: ").strip()
        if pass_or_key is "K":
            key = input("\t\t\tEnter private key name & location with complete path: path/key.ppk").strip()
            with open("Ansible/inventory", "a+") as inventory:
                inventory.write("[slave]\n")
                inventory.write(f"{ip}  ansible_user={user_name} ansible_ssh_private_key_file={key}\n")

        elif pass_or_key is 'P':
            password = input("\t\t\tEnter password required to login: ").strip()
            with open("Ansible/inventory", "a+") as inventory:
                inventory.write("[slave]\n")
                inventory.write(f"{ip} ansible_user={user_name} ansible_ssh_pass={password}\n")

        else:
            print("\t\t\tWrong Choice! \n\t\t\tPlease try again...")

    print("Reched Successfully")
    os.chdir(os.getcwd() + '/Ansible')
    if not find_executable("ansible") is None:
        os.system(f"ansible-playbook setup.yml")
        print("Reached to Execution")
    os.chdir(os.getcwd() + "/../")

    os.chdir("../../..")

