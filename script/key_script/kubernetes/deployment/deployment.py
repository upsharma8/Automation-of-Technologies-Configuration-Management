import os
import uuid


def write_deployment_file(namespace, data):
    Id = uuid.uuid4()
    with open(f"deployment-setup-files/{Id}.yaml") as deployment_file:
        deployment_file.write(data)
    os.system(f"kubectl apply -f deployment-setup-files/{Id}.yaml -n {namespace}")


def deployment(namespace='default'):
    os.chdir("key_script/kubernetes/deployment")

    os.system('tput setaf 4')
    print("\n\t\t\tPress 1: To create deployment from file content[Enter file content]\n\t\t\tPress 2: Path to deployment file\n\t\t\tPress 3: Display All Deployment"
    "\n\t\t\tPress 4: Display deployment with Labels\n\t\t\tPress 5: Delete Deployment \n\t\t\tPress 6: Delete all Deployment\n\t\t\tPress 7: return to previous menu")
    os.system('tput setaf 7')

    choice = input('Enter your choice: ')
    if choice == '1':
        write_deployment_file(namespace, input("Enter deployment file data[hint: copy-paste]: "))
    elif choice == '2':
        os.system(f"kubectl apply -f {input('Path To deployment file/.file.yaml : ')} -n {namespace}")
    elif choice == '3':
        os.system(f"kubectl get deployment -n {namespace}")
    elif choice == '4':
        os.system(f"kubectl get deployment --show-labels -n {namespace}")
    elif choice == '5':
        os.system(f"kubectl delete deployment {input('Enter deployment name: ')} -n {namespace}")
    elif choice == '6':
        os.system(f"kubectl delete deployment --all -n {namespace}")
    elif choice == '7':
        return
    else:
        print("Wrong choice!\nplease try again")

    os.chdir("../../..")
