from key_script.kubernetes.configure_client.configure_client import configure_client_service
from key_script.kubernetes.installation.kube_installation import installation
from key_script.kubernetes.nodes.node import node_service
from key_script.kubernetes.persistant_volume.persistant_volume import pv_service
from key_script.kubernetes.persistant_volume_claim.persistant_volume_claim import pvc_service
from key_script.kubernetes.pods.pod import pod_service
from key_script.kubernetes.replication_controller.replication_controller import replication_controller_service
from key_script.kubernetes.replication_set.replica_set import replication_set_service
from key_script.kubernetes.role_role_bindings.role_role_bindings import role_role_bindings_service
from key_script.kubernetes.secret.secret import secret_service
from key_script.kubernetes.service.services import service_service


def kube_menu():
    while True:
        print("\n\t\tEnter 1: For install Kubernetes multi Node Cluster\n\t\tEnter 2: For configure Client Program in your system\n\t\tEnter 3: For Pod\n\t\tEnter 4: For PVC #TO DO: implementation"
        "\n\t\tEnter 5: For PV #TO DO: Impl\n\t\tEnter 6: For ReplicationController\n\t\tEnter 7: For Replica Set\n\t\tEnter 8: For Secret #TO DO: IMPL\n\t\tEnter 9: For Service #TO DO: IMPL"
        "\n\t\tEnter 10: For Node #TO DO: IMPL\n\t\tEnter 11: Role and ROle Bindings #TO DO: IMPL\n\t\tEnter 12: Return to Previous Menu")
        choice = input("\t\tEnter your choice: ")
        if choice == '1':
            installation()

        elif choice == '2':
            configure_client_service()
        elif choice == '3':
            pod_service()

        elif choice == '4':
            pvc_service()

        elif choice == '5':
            pv_service()

        elif choice == '6':
            replication_controller_service()

        elif choice == '7':
            replication_set_service()

        elif choice == '8':
            secret_service()

        elif choice == '9':
            service_service()

        elif choice == '10':
            node_service()

        elif choice == '11':
            role_role_bindings_service()

        else:
            if choice != '12':
                print("\t\tWrong Choice!")
                return
            print("\t\tTry again...")
        print("\t\tEnter to continue...")
