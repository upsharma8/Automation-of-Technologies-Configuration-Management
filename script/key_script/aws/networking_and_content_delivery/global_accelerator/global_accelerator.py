import os


def GlobalAccelerator():
    print("""
    Enter 1: List
    Enter 2: Describe
    Enter 3: Create
    Enter 4: Delete
    """)
    choice = input("Enter your choice: ")
    if choice == '1':
        while True:
            print("""
            Enter 1 : list-accelerators
            Enter 2 : list-byoip-cidrs
            Enter 3 : list-custom-routing-accelerators
            Enter 4 : list-custom-routing-endpoint-groups
            Enter 5 : list-custom-routing-listeners
            Enter 6 : list-custom-routing-port-mappings
            Enter 7 : list-custom-routing-port-mappings-by-destination
            Enter 8 : list-endpoint-groups
            Enter 9 : list-listeners
            Enter 10 : list-tags        
            Enter 11 : list-tags-for-resource
            Enter 12 : To exit 
            """)
            if choice == '1':
                os.system('aws globalaccelerator list-accelerators')
            elif choice == '2':
                os.system('aws globalaccelerator list-byoip-cidrs')
            elif choice == '3':
                os.system('aws globalaccelerator list-custom-routing-accelerators')
            elif choice == '4':
                os.system('aws globalaccelerator list-custom-routing-endpoint-groups')
            elif choice == '5':
                os.system('aws globalaccelerator list-custom-routing-listeners')
            elif choice == '6':
                os.system('aws globalaccelerator list-custom-routing-port-mappings')
            elif choice == '7':
                os.system('aws globalaccelerator list-custom-routing-port-mappings-by-destination')
            elif choice == '8':
                os.system('aws globalaccelerator list-endpoint-groups')
            elif choice == '9':
                os.system('aws globalaccelerator list-listeners')
            elif choice == '10':
                os.system('aws globalaccelerator list-tags ')
            elif choice == '11':
                os.system('aws globalaccelerator list-tags-for-resource')
            else:
                exit()
    elif choice == '2':
        while True:
            print("""
            Enter 1 : describe-accelerator
            Enter 2 : describe-accelerator-attributes
            Enter 3 : describe-custom-routing-accelerator
            Enter 4 : describe-custom-routing-accelerator-attributes
            Enter 5 : describe-custom-routing-endpoint-group
            Enter 6 : describe-custom-routing-listener
            Enter 7 : describe-endpoint-group
            Enter 8 : describe-listener
            Enter 9 : To exit
            """)
            if choice == '1':
                acc_arn = input("Enter accelerator arn: ")
                os.system(f'aws globalaccelerator  describe-accelerator --accelerator-arn {acc_arn}')
            elif choice == '2':
                acc_arn = input("Enter accelerator arn: ")
                os.system(f'aws globalaccelerator  describe-accelerator-attributes --accelerator-arn {acc_arn}')
            elif choice == '3':
                acc_arn = input("Enter accelerator arn: ")
                os.system(f'aws globalaccelerator  describe-custom-routing-accelerator --accelerator-arn {acc_arn}')
            elif choice == '4':
                acc_arn = input("Enter accelerator arn: ")
                os.system(
                    f'aws globalaccelerator  describe-custom-routing-accelerator-attributes --accelerator-arn {acc_arn}')
            elif choice == '5':
                end_arn = input("Enter endpoint group arn: ")
                os.system(
                    f'aws globalaccelerator  describe-custom-routing-endpoint-group --endpoint-group-arn {end_arn}')
            elif choice == '6':
                l_arn = input("Enter listener arn: ")
                os.system(f'aws globalaccelerator  describe-custom-routing-listener --listener-arn {l_arn}')
            elif choice == '7':
                end_arn = input("Enter endpoint group arn: ")
                os.system(f'aws globalaccelerator  describe-endpoint-group --endpoint-group-arn {end_arn}')
            elif choice == '8':
                l_arn = input("Enter listener arn: ")
                os.system(f'aws globalaccelerator  describe-listener --listener-arn {l_arn}')
            else:
                exit()
    elif choice == '3':
        while True:
            print("""
            Enter 1: create accelerator
            Enter 2: create listener
            Enter 3: create endpoint group
            Enter 4: create custom routing accelerator
            Enter 5: create custom routing endpoint group
            Enter 6: create custom routing listener
            Enter 7: To return
            """)
            if choice == '1':
                name = input("Enter Global Accelerator name: ")
                tags = []
                for i in range(int(input("How many tags you want to add : "))):
                    key = input("Key: ")
                    value = input("Value: ")
                    tags.append("Key=" + key + "," + "Value=" + value)
                tags = "--tags ".join(tags)
                os.system(f"aws globalaccelerator  create-accelerator --name {name} --tags {tags}")
            elif choice == '2':
                acc_arn = input("Enter Global Accelerator arn: ")
                FromPort = input("FromPort: ")
                ToPort = input("ToPort: ")
                protocol = input("Enter protocol")
                affinity = input("add client affinity: [[srouceIP]] [y/n]")
                if affinity == 'y':
                    os.system(
                        f"aws globalaccelerator create-listener --accelerator-arn {acc_arn}  FromPort={FromPort},ToPort={ToPort} --protocol {protocol} --client-affinity SOURCE_IP")
                else:
                    os.system(
                        f"aws globalaccelerator create-listener --accelerator-arn {acc_arn}  FromPort={FromPort},ToPort={ToPort} --protocol {protocol}")
            elif choice == '3':
                l_arn = input("Enter listener arn: ")
                end_point_region = input("Enter EndPoint Region: ")
                health_check = input("Add Health Check : [Y/N]: ")

                os.system(f"aws globalaccelerator create-endpoint-group "
                          f"--listener-arn  {l_arn} "
                          f"--endpoint-group-region {end_point_region} "
                          f"--endpoint-configurations {None} "
                          f"--traffic-dial-percentage {None} ")

            elif choice == '4':
                name = input("Enter GA name: ")
                tags = []
                for i in range(int(input("How many tags you want to add : "))):
                    key = input("Key: ")
                    value = input("Value: ")
                    tags.append("Key=" + key + "," + "Value=" + value)
                tags = "--tags ".join(tags)
                os.system(f"aws globalaccelerator create-custom-routing-accelerator --name {name} --tags {tags}")
            elif choice == '5':
                pass
            elif choice == '6':
                pass
            elif choice == '7':
                return
            else:
                print("wrong choice!\n try again")
