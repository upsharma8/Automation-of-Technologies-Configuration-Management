import json
import os
import subprocess


def Key():
    while True:
        os.system('tput setaf 4')
        print(
            """\n\n\t\t\t\tPress 1: to create Key\n\t\t\t\tPress 2: to delete Key\n\t\t\t\tPress 3: to describe key pairs\n\t\t\t\tPress 4: Exit from this menu""")
        os.system('tput setaf 7')

        choice = input("\n\t\t\t\tEnter your choice : ")
        if choice == "1":
            key_name = input("\t\t\t\tEnter Key-name: ")
            os.system(
                "aws ec2 create-key-pair --key-name {} --query KeyMaterial --output text >  {}.pem".format(key_name,
                                                                                                           key_name))
        elif choice == "2":
            key_name = input("\t\t\t\tEnter Key-name: ")
            os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
        elif choice == "3":
            os.system("aws ec2 describe-key-pairs")
        elif choice == "4":
            return
        else:
            print("\t\t\t\tWrong Choice")
        input("\t\t\t\tEnter to continue..")
        os.system("clear")


def securityGroup():
    while True:
        os.system('tput setaf 4')
        print("""\n\n\t\t\t\tPress 1: Create security Group\n\t\t\t\tPress 2: Describe security Group
\t\t\t\tPress 3: Delete security Group\n\t\t\t\tPress 4: Add rule of security Group
\t\t\t\tPress 5: Delete rule of security Group\n\t\t\t\tPress 6: Exit from this menu""")
        os.system('tput setaf 7')

        choice = input("\n\t\t\t\tEnter your choice: ")
        if choice == '1':
            description = input("\t\t\t\tEnter Description of sg : ")
            group_name = input("\t\t\t\tEnter sg group Name : ")
            os.system("aws ec2  create-security-group --description {} --group-name {}".format(description, group_name))
        elif choice == '2':
            os.system("aws ec2 describe-security-groups")
        elif choice == '3':
            Id = input("\t\t\t\tEnter sg Id: ")
            os.system(" aws ec2 delete-security-group --group-id {}".format(Id))
        elif choice == '4':
            print("\t\t\t\tEnter 1 for ingress \n\t\t\t\tEnter 2 for egress")
            add = input("\t\t\t\tEnter your choice : ")
            security_id = input("\t\t\t\tEnter security id: ")
            protocol = input("\t\t\t\tEnter protocol: ")
            port = input("\t\t\t\tEnter Port: ")
            cidr = input("\t\t\t\tEnter Cidr: ")
            if add == "1":
                os.system(
                    "aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            elif add == "2":
                os.system(
                    "aws ec2 authorize-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            else:
                print("\t\t\t\tWrong Choice")
        elif choice == '5':
            print("\n\n\t\t\t\tEnter 1 for ingress \n\t\t\t\tEnter 2 for egress")
            delete = input("\t\t\t\tEnter your choice : ")
            security_id = input("\t\t\t\tEnter security id: ")
            protocol = input("\t\t\t\tEnter protocol: ")
            port = input("\t\t\t\tEnter Port: ")
            cidr = input("\t\t\t\tEnter Cidr: ")
            if delete == "1":
                os.system(
                    "aws ec2 revoke-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            elif delete == "2":
                os.system("aws ec2 revoke-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(
                    security_id, protocol, port, cidr))
            else:
                print("\t\t\t\tWrong Choice")
        elif choice == '6':
            break
        else:
            print("\t\t\t\tWrong Choice")
        input("\t\t\t\tEnter to continue..")
        os.system("clear")


def volume():
    while True:
        os.system('tput setaf 4')
        print('\n\n\t\t\t\tEnter 1: Describe volumes\n\t\t\t\tEnter 2: Create volumes\n\t\t\t\tEnter 3: Delete volume'
              '\n\t\t\t\tEnter 4: Attach volume\n\t\t\t\tEnter 5: Detach volume\n\t\t\t\tEnter 6: Modify '
              'volume\n\t\t\t\tEnter 7: Transfer volume to other AZ '
              '\n\t\t\t\tEnter 8: Transfer volume to Other Region\n\t\t\t\tPress 9: Exit from this menu')
        os.system('tput setaf 7')

        choice = input("\n\t\t\t\tEnter your Choice: ")
        if choice == "1":
            os.system("aws ec2 describe-volumes")
        elif choice == "2":
            az = input("\t\t\t\tEnter AZ : ")
            size = input("\t\t\t\tsize: ")
            os.system("aws ec2 create-volume --availability-zone {} --size {}".format(az, size))
        elif choice == "3":
            volume_id = input("\t\t\t\tEnter Volume ID : ")
            os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
        elif choice == "4":
            device = input("\t\t\t\tEnter  device Name: ")
            instance_id = input("\t\t\t\tInstance ID: ")
            volume_id = input("\t\t\t\tVolume ID: ")
            os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {} ".format(device, instance_id,
                                                                                                  volume_id))
        elif choice == "5":
            volume_id = input("\t\t\t\tVolume ID: ")
            os.system("aws ec2 detach-volume --volume-id {} --force".format(volume_id))
        elif choice == "6":
            print("\t\t\t\tmodify size only supported others features are coming soon")
            size = input("Enter size: ")
            volume_id = input("Enter Volume ID: ")
            os.system("aws ec2 modify-volume --volume-id {} --size {}".format(volume_id, size))
        elif choice == "7" or choice == "8":
            volume_id = input("\t\t\t\tEnter Volume ID: ")
            output = json.loads(subprocess.getoutput('aws ec2 describe-volumes --volume-ids {}'.format(volume_id)))
            if choice == "7":
                az = input("\t\t\t\tEnter availability zone: ")
                os.system("aws ec2 create-volume --availability-zone {} --snapshot-id {}".format(az,
                                                                                                 output["Volumes"][0][
                                                                                                     'SnapshotId']))
            if choice == '8':
                source_region = input("\t\t\t\tEnter source region : ")
                source_snapshot = input("\t\t\t\tEnter source snapshot id: ")
                destination_region = input("\t\t\t\tEnter destination region: ")
                os.system(
                    "aws ec2 copy-snapshot --source-region  {} --source-snapshot-id {} --destination-region {} ".format(
                        source_region, source_snapshot, destination_region))
            subprocess.getoutput("aws")
        elif choice == "9":
            return
        else:
            print("\t\t\t\tWrong Choice")
        input("\t\t\t\tEnter to continue..")
        os.system("clear")


def instance():
    while True:
        os.system('tput setaf 4')
        print(
            "\n\n\n\t\t\t\tPress 1: Get information about your instances\n\t\t\t\tPress 2: launch an EC2 instance\n\t\t\t\tPress 3: Start an instance\n\t\t\t\tPress 4: Stop an instance"
            "\n\t\t\t\tPress 5: Terminate an instance\n\t\t\t\tPress 6: Exit from this menu")

        os.system('tput setaf 7')

        choice = input("\n\t\t\t\tEnter your choice: ")
        if choice == "1":
            os.system("aws ec2 describe-instances")
        elif choice == "2":
            print("\t\t\t\tChoose the image-id:")
            
            print("\n\t\t\t\t\tPress 1: For Amazon Linux")
            print("\n\t\t\t\t\tPress 2: For Redhat Linux")
            ch=int(input("\t\t\t\tChoose the Image-Id: "))
            if ch==1:
                image_id = "ami-04db49c0fb2215364"
            else:
                image_id = "ami-06a0b4e3b7eb7a300"
            cnt = int(input("\t\t\t\tHow many instance you want to launch: "))
            key_name = input("\t\t\t\tEnter your key name: ")
            print("\n\t\t\t\t\tChoose subnet-id:")
            print("\n\t\t\t\tPress 1: For ap-south-1a")
            print("\n\t\t\t\tPress 2: For ap-south-1b")
            ch=int(input("\t\t\t\tChoose the Subnet-Id: "))
            if ch==1:
               subnet_id="subnet-f027da9b"
            elif ch==2:
               subnet_id="subnet-5b022017"
            
            instance_type = input("\t\t\t\tEnter instance type: ")
            security_group_id=input("\n\t\t\t\t Enter Security Group Id to use: ")
                     
            
               
            os.system(
                "aws ec2 run-instances --image-id {} --instance-type {}"
                " --count {} --subnet-id {} --key-name {} --security-group-ids {}".format(
                    image_id, instance_type, cnt, subnet_id, key_name, security_group_id))
            print("\t\t\t\tInstance Launched !!!")
        elif choice == "3":
            id2 = input("\t\t\t\tEnter your instance id :")
            os.system("aws ec2 start-instances --instance-ids {}".format(id2))
        elif choice == "4":
            id3 = input("\t\t\t\tEnter your instance id :")
            os.system("aws ec2 stop-instances --instance-ids {}".format(id3))
        elif choice == "5":
            Id = input("\t\t\t\tEnter instance id: ")
            os.system("aws ec2 terminate-instances --instance-ids {}".format(Id))
        else:
            if choice != '6':
                print("\t\t\t\tWrong Choice")
            return
        input("\t\t\t\tEnter to continue...")
        os.system("clear")


def AMI():
    while True:
        os.system('tput setaf 4')
        print(
            "\n\n\t\t\t\tPress 1: Describe Images\n\t\t\t\tPress 2: Create Amazon Machine Image\n\t\t\t\tPress 3: Make Image Public"
            "\n\t\t\t\tPress 4: Make Image Private\n\t\t\t\tPress 5: Delete Amazon Machine Image\n\t\t\t\tPress 6: Exit from this menu")
        os.system('tput setaf 7')

        choice = input("\n\t\t\t\tEnter your Choice: ")
        if choice == '1':
            os.system("aws ec2 describe-images --image-ids {}".format(input("Enter image id: ")))
        elif choice == '2':
            instance_id = input("\t\t\t\tEnter instance id : ")
            ami_name = input("\t\t\t\tEnter AMI Name: ")
            description = input("\t\t\t\tEnter Description of  instance : ")
            os.system(
                "aws ec2 create-image --instance-id {} --name '{}' --description '{}' --no-reboot".format(instance_id,
                                                                                                          ami_name,
                                                                                                          description))
        elif choice == '3':
            image_id = input("\t\t\t\tEnter Image ID: ")
            os.system("aws ec2 deregister-image --image-id {}".format(image_id))
        else:
            if choice != '6':
                print("\t\t\t\tWrong choice")
            return
        input("\t\t\t\tEnter to continue......")
        os.system("clear")


def Snapshots():
    while True:
        os.system('tput setaf 4')
        print(
            "\n\n\t\t\t\tPress 1: Display All Snapshot\n\t\t\t\tPress 2: Display snapshot attribute\n\t\t\t\tPress 3: create-snapshot\n\t\t\t\tPress 4: delete-snapshot "
            "\n\t\t\t\tPress 5: copy-snapshot\n\t\t\t\tPress 6: return")
        os.system('tput setaf 7')

        choice = input("\n\t\t\t\tEnter your choice: ")
        if choice == '1':
            os.system("aws ec2 describe-snapshots")
        elif choice == '2':
            attribute = input("\t\t\t\tEnter attribute : ")
            snapshot_id = input("\t\t\t\tEnter snapshot_id: ")
            os.system(
                "aws ec2 describe-snapshot-attributes --attribute {}   --snapshot-id {}".format(attribute, snapshot_id))
        elif choice == '3':
            volume_id = input("\t\t\t\tvolume_id : ")
            description = input("\t\t\t\tSnapshot description: ")
            key, value = input("\t\t\t\tEnter tag key and value: eg key=value ").split("=")
            os.system(
                f"aws ec2 create-snapshot --volume-id {volume_id} --description {description} --tag-specifications "
                f"'ResourceType=snapshot,Tags=[Key={key}, Value={value}]'")
        elif choice == '4':
            snapshot_id = input("\t\t\t\tEnter snapshot_id: ")
            os.system(f"aws ec2 delete-snapshot --snapshot-id {snapshot_id}")
        elif choice == '5':
            source_region = input("\t\t\t\tEnter source region : ")
            source_snapshot = input("\t\t\t\tEnter source snapshot id: ")
            destination_region = input("\t\t\t\tEnter destination region: ")
            os.system(
                "aws ec2 copy-snapshot --source-region  {} --source-snapshot-id {} --destination-region {} ".format(
                    source_region, source_snapshot, destination_region))
        else:
            if choice != '6':
                print("\t\t\t\tWrong Choice")
            return
        input("\t\t\t\tEnter to continue...")
        os.system("clear")


def ElasticIPS():
    while True:
        os.system('tput setaf 4')
        print(
            "\n\t\t\t\tEnter 1: Display All IP\n\t\t\t\tEnter 2: Allocate ElasticIPS\n\t\t\t\tEnter 3: Associate ElasticIPS\n\t\t\t\tEnter 4: disassociate-address ElasticIPS "
            "\n\t\t\t\tEnter 5: release-address ElasticIPS\n\t\t\t\tPress 6: return")
        os.system('tput setaf 7')

        choice = input("\n\t\t\t\tEnter your choice: ")
        if choice == '1':
            os.system("aws ec2 describe-addresses")
        elif choice == '2':
            os.system("aws ec2 allocate-address")
        elif choice == '3':
            instance_id = input("\t\t\t\tinstance id: ")
            ipaddress = input("\t\t\t\tElastic ip address: ")
            os.system(f"aws ec2 associate-address --instance-id {instance_id} --public-ip {ipaddress}")
        elif choice == '4':
            ipaddress = input("\t\t\t\tElastic ip address: ")
            os.system(f"aws ec2 disassociate-address --public-ip {ipaddress}")
        elif choice == '5':
            ipaddress = input("\t\t\t\tElastic ip address: ")
            os.system(f"aws ec2 release-address --public-ip {ipaddress}")
        else:
            return
        input("\t\t\t\tEnter to continue......")
        os.system("clear")


def NetworkInterfaces():
    os.system("clear")
    pass


def LoadBalancers():
    os.system("clear")
    pass


def TargetGroups():
    os.system("clear")
    pass


def AutoScalingLaunchConfiguration():
    os.system("clear")
    pass


def AutoScalingGroups():
    os.system("clear")
    pass


def EC2Menu():
    while True:
        os.system('tput setaf 4')
        print('''\n\n\t\t\tPress 1: FOR KEY PAIR\n\t\t\tPress 2: FOR SECURITY GROUP	\n\t\t\tPress 3: FOR EC2 INSTANCE
\t\t\tPress 4: FOR VOLUMES\n\t\t\tPress 5: FOR AMI\n\t\t\tPress 6: FOR Snapshot\n\t\t\tPress 7: FOR Elastic IPS
\t\t\tPress 8: FOR Network InterFaces\n\t\t\tPress 9: FOR Target Groups\n\t\t\tPress 10: FOR Auto Scaling Launch Configuration
\t\t\tPress 11: FOR Auto Scaling Group\n\t\t\tPress 12: RETURN
            ''')
        os.system('tput setaf 7')
        choice = input("\n\t\t\tEnter Your Choice:")
        if choice == '1':
            Key()
        elif choice == '2':
            securityGroup()
        elif choice == '3':
            instance()
        elif choice == '4':
            volume()
        elif choice == '5':
            AMI()
        elif choice == '6':
            Snapshots()
        elif choice == '7':
            ElasticIPS()
        elif choice == '8':
            NetworkInterfaces()
        elif choice == '9':
            TargetGroups()
        elif choice == '10':
            AutoScalingLaunchConfiguration()
        elif choice == '11':
            AutoScalingGroups()
        elif choice == '12':
            return
        else:
            print("\t\t\t\tWrong choice")
        input("\t\t\t\tEnter to continue...")
        os.system("clear")
