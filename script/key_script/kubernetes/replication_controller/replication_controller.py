import os


def replication_controller_service(namespace='default'):
    while True:
        print("\n\t\t\tEnter 0: RUN YAML FILE\n\t\t\tEnter 1: List RC\n\t\t\tEnter 2: List RC with Labels\n\t\t\tEnter 3: Wide List RC\n\t\t\tEnter 4: Get YAML file for running RC"
        "\n\t\t\tEnter 5: Describe RC\n\t\t\tEnter 6: Expose RC\n\t\t\tEnter 7: Delete RC\n\t\t\tEnter 8: Delete ALL RC\n\t\t\tEnter 9: TO EXIT")
        choice = input("\t\t\tEnter your choice: ")
        if choice == '0':
            yml = input("\t\t\tEnter Path of yaml files: \n")
            with open('rc.yml', "w+") as pod_file:
                pod_file.write(yml)
                os.system(f'kubectl apply -f rc.yml -n {namespace}')
        elif choice == '1':
            os.system(f'kubectl get rc -n {namespace}')
        elif choice == '2':
            os.system(f'kubectl get rc --show-labels -n {namespace}')
        elif choice == '3':
            os.system(f'kubectl get rc -o wide -n {namespace}')
        elif choice == '4':
            rc_name = input("\t\t\tEnter rc name: ")
            os.system(f'kubectl get rc {rc_name} -o yaml -n {namespace}')
        elif choice == '5':
            rc_name = input("\t\t\tEnter rc Name: ")
            os.system(f'kubectl describe {rc_name} -n {namespace}')
        elif choice == '6':
            rc_name = input("\t\t\tEnter rc_name: ")
            expose_type = input("\t\t\tEnter expose type [NodePort/ClusterIP/LoadBalancer]: ")
            port = input('\t\t\tEnter port number: ')
            os.system(f'kubectl expose pod/{rc_name} --type={expose_type} --port={port} -n {namespace}')
            os.system(f'kubectl get svc {rc_name} -n {namespace}')
        elif choice == '7':
            rc_name = input("\t\t\tEnter pod_name: ")
            os.system(f'kubectl delete rc {rc_name} -n {namespace}')
        elif choice == '8':
            os.system(f'kubectl delete rc --all -n {namespace}')
        else:
            if choice != '9':
                print("\t\t\twrong choice!")
            return
