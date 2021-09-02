import os


def pod_service(namespace='default'):
    while True:
        print("\n\t\t\tEnter 0: run yaml file\n\t\t\tEnter 1: List Pod\n\t\t\tEnter 2: List Pod with Labels\n\t\t\tEnter 3: Wide List Pod\n\t\t\tEnter 4: Get YAML file for running Pod"
        "\n\t\t\tEnter 5: Describe Pod\n\t\t\tEnter 6: Create Pod\n\t\t\tEnter 7: Expose Pod\n\t\t\tEnter 8: Delete Pod\n\t\t\tEnter 9: Delete All Pods\n\t\t\tEnter 10: see Logs of Pod"
        "\n\t\t\tEnter 11: To Exit")
        choice = input("\t\t\tEnter your choice: ")
        if choice == '0':
            yml = input("\t\t\tEnter: \n")
            with open('pod.yml', "w+") as pod_file:
                pod_file.write(yml)
            os.system(f'kubectl apply -f pod.yml -n {namespace}')
        elif choice == '1':
            os.system(f'kubectl get pods -n {namespace}')
        elif choice == '2':
            os.system(f'kubectl get pod --show-labels -n {namespace}')
        elif choice == '3':
            os.system(f'kubectl get pod -o wide -n {namespace}')
        elif choice == '4':
            pod_name = input("\t\t\tEnter pod_name: ")
            os.system(f'kubectl get pod {pod_name} -o yaml -n {namespace}')
        elif choice == '5':
            pod = input("\t\t\tEnter Pod Name: ")
            os.system(f'kubectl describe {pod} -n {namespace}')
        elif choice == '6':
            pod_name = input("\t\t\tEnter pod_name: ")
            image = input('\t\t\tEnter image name: ')
            os.system(f"\t\t\tkubectl run {pod_name} --image {image} -n {namespace}")
        elif choice == '7':
            pod_name = input("\t\t\tEnter pod_name: ")
            expose_type = input("\t\t\tEnter expose type [NodePort/ClusterIP/LoadBalancer]: ")
            port = input('\t\t\tEnter port number: ')
            os.system(f'kubectl expose pod/{pod_name} --type={expose_type} --port={port} -n {namespace}')
            os.system(f'kubectl get svc {pod_name} -n {namespace}')
        elif choice == '8':
            pod_name = input("\t\t\tEnter pod_name: ")
            os.system(f'kubectl delete pod {pod_name} -n {namespace}')
        elif choice == '9':
            os.system(f'kubectl delete pod --all -n {namespace}')
        elif choice == '10':
            pod_name = input("\t\t\tEnter pod_name: ")
            os.system(f'kubectl logs pod {pod_name} -n {namespace}')
        else:
            if choice != "11":
                print("\t\t\tWrong Choice")
            return
