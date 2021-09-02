import os
import subprocess


def authTypePass(username, password, ip):
    while True:
        os.system('tput setaf 4')
        print("\n\t\t\t-------------------LVM MENU------------------------\n\t\t\t-        Enter 1 : Display all Disks              -\n\t\t\t---------------------------------------------------"
              "\n\t\t\t-        Enter 2 : Display Mount Points           -\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 3 : Create PV/VG/LV                -"
              "\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 4 : Display PV/VG/LV               -\n\t\t\t---------------------------------------------------"
              "\n\t\t\t-        Enter 5 : Delete PV/VG/LV                -\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 6 : Mount LV                       -"
              "\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 7 : UnMount                        -\n\t\t\t---------------------------------------------------"
              "\n\t\t\t-        Enter 8 : Extend VG/LV                   -\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 9 : Reduce LV                      -"
              "\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 10 : Exit                          -\n\t\t\t---------------------------------------------------")

        os.system('tput setaf 7')
        choice = input("\t\t\tEnter your choice: ")
        if choice == '1':
            os.system("sshpass -p {} ssh {}@{} sudo fdisk -l".format(password, username, ip))
        elif choice == '2':
            os.system("sshpass -p {} ssh {}@{} sudo df -hT".format(password, username, ip))
        elif choice == '3':
            create = input("\t\t\tEnter PV/VG/LV: ")
            if create.lower() == 'pv':
                HD_name = input("\t\t\tDisk Name: ")
                os.system("sshpass -p {} ssh {}@{} sudo pvcreate {}".format(password, username, ip, HD_name))
            elif create.lower() == 'vg':
                HD_name = input("\t\t\tEnter space separated disk names: ")
                vg_name = input("\t\t\tEnter volume group Name: ")
                os.system(
                    "sshpass -p {} ssh {}@{} sudo vgcreate {} {}".format(password, username, ip, vg_name, HD_name))
            elif create.lower() == 'lv':
                vg_name = input("\t\t\tEnter volume group name: ")
                lv_name = input("\t\t\tEnter logical volume name: ")
                lv_size = input("\t\t\tEnter LV size: ")
                os.system(
                    "sshpass -p {} ssh {}@{} sudo lvcreate --name {} --size +{}G {} ".format(password, username, ip,
                                                                                             lv_name, lv_size, vg_name))
            else:
                print("\t\t\tWrong create operation")
        elif choice == '4':
            display = input("\t\t\tDisplay PV/VG/LV : ")
            if display.lower() == 'pv':
                os.system("sshpass -p {} ssh {}@{} sudo pvdisplay".format(password, username, ip))
            elif display.lower() == 'vg':
                os.system("sshpass -p {} ssh {}@{} sudo vgdisplay".format(password, username, ip))
            elif display.lower() == 'lv':
                os.system("sshpass -p {} ssh {}@{} sudo lvdisplay".format(password, username, ip))
            else:
                print("\t\t\tWrong create operation")
        elif choice == '5':
            delete = input("\t\t\tDelete PV/VG/LV : ")
            if delete.lower() == 'pv':
                delete_hd = input("\t\t\tEnter PV name: ")
                os.system("sshpass -p {} ssh {}@{} sudo pvremove {}".format(password, username, ip, delete_hd))
            elif delete.lower() == 'vg':
                delete_hd = input("\t\t\tEnter VG name: ")
                os.system("sshpass -p {} ssh {}@{} sudo vgremove {}".format(password, username, ip, delete_hd))
            elif delete.lower() == 'lv':
                vg_name = input("\t\t\tEnter VG name: ")
                lv_name = input("\t\t\tEnter LG name: ")
                os.system(
                    "sshpass -p {} ssh {}@{} sudo lvremove /dev/{}/{}".format(password, username, ip, vg_name, lv_name))
            else:
                print("\t\t\tWrong create operation")
        elif choice == '6':
            lv_name = input("\t\t\tENTER NAME OF LV:")
            vg_name = input("\t\t\tENTER VG NAME: ")
            os.system("sshpass -p {} ssh {}@{} sudo mkfs.ext4 /dev/{}/{}".format(password, username, ip, vg_name,
                                                                                 lv_name))
            folder = input("\t\t\tENTER FOLDER NAME TO MOUNT:")
            os.system("sshpass -p {} ssh {}@{} sudo mkdir {}".format(password, username, ip, folder))
            os.system(
                "sshpass -p {} ssh {}@{} sudo mount /dev/{}/{} {}".format(password, username, ip, vg_name, lv_name,
                                                                          folder))
        elif choice == '7':
            folder = input("\t\t\tEnter folder Name")
            os.system("sshpass -p {}  ssh {}@{} sudo umount {}".format(password, username, ip, folder))

        elif choice == '8':
            extend = input("\t\t\tExtend VG/LV : ")
            if extend == 'LV':
                size_change = input("\t\t\tENTER SIZE TO BE INCREASED:")
                vg_name = input("\t\t\tENTER VG NAME: ")
                lv_name = input("\t\t\tENTER NAME OF LV:")
                os.system(
                    "sshpass -p {} ssh {}@{} sudo lvextend --size +{}G  /dev/{}/{}".format(password, username, ip,
                                                                                           size_change, vg_name,
                                                                                           lv_name))
                os.system(
                    "sshpass -p {} ssh {}@{} sudo resize2fs /dev/{}/{}".format(password, username, ip, vg_name,
                                                                               lv_name))
            elif extend == "VG":
                pv = input("\t\t\tEnter new PV name: ")
                vg = input("\t\t\tEnter VG-Name: ")
                os.system("sshpass -p {} ssh {}@{} sudo vgextend {} {}".format(password, username, ip, vg, pv))
            else:
                print("\t\t\tWrong create opertion")
        elif choice == '9':
            vg_name = input("\t\t\tENTER VG NAME: ")
            lv_name = input("\t\t\tENTER NAME OF LV:")
            new_size = input("\t\t\tENTER SIZE UPTO WHICH LV SHOULD BE REDUCED:")
            if 'n' == input("\t\t\tlv is mounted y/n: "):
                os.system("sshpass -p {} ssh {}@{} sudo e2fsck -f /dev/{}/{}".format(password, username, ip, vg_name,
                                                                                     lv_name))
                os.system("sshpass -p {} ssh {}@{} sudo lvreduce -r -L {}G /dev/{}/{}".format(password, username, ip,
                                                                                              new_size, vg_name,
                                                                                              lv_name))
            else:
                print("\t\t\tplease umount lv else you might loose online work")
        elif choice == '10':
            exit()
        else:
            print("\t\t\tWrong Choice")
        input("\t\t\tEnter to continue")
        os.system("clear")


def authTypeKey(username, keyPath, ip):
    while True:
        os.system('tput setaf 4')
        print(
            "\n\t\t\t-------------------LVM MENU------------------------\n\t\t\t-        Enter 1 : Display all Disks              -\n\t\t\t---------------------------------------------------"
            "\n\t\t\t-        Enter 2 : Display Mount Points           -\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 3 : Create PV/VG/LV                -"
            "\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 4 : Display PV/VG/LV               -\n\t\t\t---------------------------------------------------"
            "\n\t\t\t-        Enter 5 : Delete PV/VG/LV                -\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 6 : Mount LV                       -"
            "\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 7 : UnMount                        -\n\t\t\t---------------------------------------------------"
            "\n\t\t\t-        Enter 8 : Extend VG/LV                   -\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 9 : Reduce LV                      -"
            "\n\t\t\t---------------------------------------------------\n\t\t\t-        Enter 10 : Exit                          -\n\t\t\t---------------------------------------------------")
        os.system('tput setaf 7')
        choice = input("\t\t\tEnter your choice: ")
        if choice == '1':
            os.system("ssh -i {}  {}@{} sudo fdisk -l".format(keyPath, username, ip))
        elif choice == '2':
            os.system("ssh -i {} {}@{} sudo df -hT".format(keyPath, username, ip))
        elif choice == '3':
            create = input("\t\t\tEnter PV/VG/LV: ")
            if create.lower() == 'pv':
                HD_name = input("\t\t\tDisk Name: ")
                os.system("ssh -i {} {}@{} sudo pvcreate {}".format(keyPath, username, ip, HD_name))
            elif create.lower() == 'vg':
                HD_name = input("\t\t\tEnter space separated disk names: ")
                vg_name = input("\t\t\tEnter volume group Name: ")
                os.system(
                    "ssh -i {} {}@{} sudo vgcreate {} {}".format(keyPath, username, ip, vg_name, HD_name))
            elif create.lower() == 'lv':
                vg_name = input("\t\t\tEnter volume group name: ")
                lv_name = input("\t\t\tEnter logical volume name: ")
                lv_size = input("\t\t\tEnter LV size: ")
                os.system(
                    "ssh -i {} {}@{} sudo lvcreate --name {} --size +{}G {} ".format(keyPath, username, ip,
                                                                                     lv_name, lv_size, vg_name))
            else:
                print("\t\t\tWrong create opertion")
        elif choice == '4':
            display = input("\t\t\tDisplay PV/VG/LV : ")
            if display.lower() == 'pv':
                os.system("ssh -i {} {}@{} sudo pvdisplay".format(keyPath, username, ip))
            elif display.lower() == 'vg':
                os.system("ssh -i {} {}@{} sudo vgdisplay".format(keyPath, username, ip))
            elif display.lower() == 'lv':
                os.system("ssh -i {} {}@{} sudo lvdisplay".format(keyPath, username, ip))
            else:
                print("\t\t\tWrong create opertion")
        elif choice == '5':
            delete = input("\t\t\tDelete PV/VG/LV : ")
            if delete.lower() == 'pv':
                delete_hd = input("\t\t\tEnter PV name: ")
                os.system("ssh -i {} {}@{} sudo pvremove {}".format(keyPath, username, ip, delete_hd))
            elif delete.lower() == 'vg':
                delete_hd = input("\t\t\tEnter VG name: ")
                os.system("ssh -i {} {}@{} sudo vgremove {}".format(keyPath, username, ip, delete_hd))
            elif delete.lower() == 'lv':
                vg_name = input("\t\t\tEnter VG name: ")
                lv_name = input("\t\t\tEnter LG name: ")
                os.system(
                    "ssh -i {} {}@{} sudo lvremove /dev/{}/{}".format(keyPath, username, ip, vg_name, lv_name))
            else:
                print("\t\t\tWrong create operation")
        elif choice == '6':
            folder = input("\t\t\tEnter folder Name")
            os.system("ssh -i {} {}@{} sudo umount -f {}".format(keyPath, username, ip, folder))
        elif choice == '7':
            lv_name = input("\t\t\tENTER NAME OF LV:")
            vg_name = input("\t\t\tENTER VG NAME: ")
            os.system("ssh -i  {} {}@{} sudo mkfs.ext4 /dev/{}/{}".format(keyPath, username, ip, vg_name, lv_name))
            folder = input("\t\t\tENTER FOLDER NAME TO MOUNT:")
            os.system("ssh -i {} {}@{} sudo mkdir {}".format(keyPath, username, ip, folder))
            os.system(
                "ssh -i {} {}@{} sudo mount /dev/{}/{} {}".format(keyPath, username, ip, vg_name, lv_name, folder))
        elif choice == '8':
            extend = input("\t\t\tExtend VG/LV : ")
            if extend == 'LV':
                size_change = input("\t\t\tENTER SIZE TO BE INCREASED:")
                vg_name = input("\t\t\tENTER VG NAME: ")
                lv_name = input("\t\t\tENTER NAME OF LV:")
                os.system(
                    "ssh -i {} {}@{} sudo lvextend --size +{}G  /dev/{}/{}".format(keyPath, username, ip, size_change,
                                                                                   vg_name, lv_name))
                os.system(
                    "ssh -i {} {}@{} sudo resize2fs /dev/{}/{}".format(keyPath, username, ip, vg_name, lv_name))
            elif extend == "VG":
                pv = input("\t\t\tEnter new PV name: ")
                vg = input("\t\t\tEnter VG-Name: ")
                os.system("ssh -i {} {}@{} sudo vgextend {} {}".format(keyPath, username, ip, vg, pv))
            else:
                print("\t\t\tWrong create operation")
        elif choice == '9':
            vg_name = input("\t\t\tENTER VG NAME: ")
            lv_name = input("\t\t\tENTER NAME OF LV:")
            new_size = input("\t\t\tENTER SIZE UPTO WHICH LV SHOULD BE REDUCED:")
            if 'n' == input("\t\t\tlv is mounted y/n: "):
                os.system("ssh -i {} {}@{} sudo e2fsck -f /dev/{}/{}".format(keyPath, username, ip, vg_name, lv_name))
                os.system(
                    "ssh -i {} {}@{} sudo lvreduce -r -L {}G /dev/{}/{}".format(keyPath, username, ip, new_size, vg_name,
                                                                               lv_name))
            else:
                print("\t\t\tplease umount lv else you might loose online work")
        elif choice == '10':
            exit()
        else:
            print("\t\t\tWrong Choice")
        input("\t\t\tEnter to continue")
        os.system("clear")


########################################################
########################################################
def LVM():
    ipAddress = input("\t\t\tEnter IP of target System :")
    username = input("\t\t\tUserName: ")
    auth_type = input("\t\t\tEnter Authentication type-->  [key/password] : ")

    if auth_type.lower() == "key":
        key_path = input("\t\t\tEnter key path from base directory: ")
        authTypeKey(username, key_path, ipAddress)
    elif auth_type.lower() == "password" or auth_type.lower() == "pass":
        print("\t\t\tSetting Up environment please wait")
        subprocess.getoutput("yum install sshpass -y")
        password = input("\t\t\tEnter password: ")
        authTypePass(username, password, ipAddress)
    else:
        print("N\t\t\tot Valid")
        exit(0)
