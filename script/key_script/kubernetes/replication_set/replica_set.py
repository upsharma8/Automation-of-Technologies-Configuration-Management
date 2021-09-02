import os


def replication_set_service(namespace='default'):
    while True:
        print("\n\t\t\tPress 0: RUN YAML FILE\n\t\t\tPress 1: List RS\n\t\t\tPress 2: List RS with Labels\n\t\t\tPress 3: Wide List RS\n\t\t\tPress 4: Get YAML file for running RS"
        "\n\t\t\tPress 5: Describe RS\n\t\t\tPress 6: Expose RS\n\t\t\tPress 7: Delete RS\n\t\t\tPress 8: Delete ALL RS\n\t\t\tPress 9: TO EXIT")

        choice = input("\t\t\tEnter your choice: ")
        if choice == '0':
            yml = input("\t\t\tEnter Data: \n")
            with open('rs.yml', "w+") as pod_file:
                pod_file.write(yml)
            os.system(f'kubectl apply -f rs.yml -n {namespace}')
        elif choice == '1':
            os.system(f'kubectl get rs -n {namespace}')
        elif choice == '2':
            os.system(f'kubectl get rs --show-labels -n {namespace}')
        elif choice == '3':
            os.system(f'kubectl get rs -o wide -n {namespace}')
        elif choice == '4':
            rs_name = input("\t\t\tEnter rs name: ")
            os.system(f'kubectl get rs {rs_name} -o yaml -n {namespace}')
        elif choice == '5':
            rs_name = input("\t\t\tEnter rs Name: ")
            os.system(f'kubectl describe {rs_name} -n {namespace}')
        elif choice == '6':
            rs_name = input("\t\t\tEnter rc_name: ")
            expose_type = input("\t\t\tEnter expose type [NodePort/ClusterIP/LoadBalancer]: ")
            port = input('\t\t\tEnter port number: ')
            os.system(f'kubectl expose pod/{rs_name} --type={expose_type} --port={port} -n {namespace}')
            os.system(f'kubectl get svc {rs_name} -n {namespace}')
        elif choice == '7':
            rs_name = input("\t\t\tEnter pod_name: ")
            os.system(f'kubectl delete rs {rs_name} -n {namespace}')
        elif choice == '8':
            os.system(f'kubectl delete rs --all -n {namespace}')
        else:
            if choice == '9':
                print("\t\t\twrong choice!")
            return
