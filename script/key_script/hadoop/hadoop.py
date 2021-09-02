import getpass
import os
import subprocess


###############################################################


def LocalHadoopInstall():
    status = 1
    print("\n\t\t\tPlease wait")
    if not subprocess.getstatusoutput("sudo yum install initscripts -y")[0]:
        if not subprocess.getstatusoutput("pip3 install gdown")[0]:
            if not os.system(
                    "sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm") and \
                    0 == os.system("sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm"):
                os.system("sudo rpm -ihv  jdk-8u171-linux-x64.rpm")
                status = os.system("sudo rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force")

    if status == 0:
        print("\n\t\t\tHadoop successfully installed  in your system")
    else:
        print("\n\t\t\tsomething went wrong please contact support team")


#################################################################


def LocalNodeConfigure(current_type):
    if current_type == "NameNode":
        os.system("sudo cp BIGDATA/templates/core-site/namenode/core-site.xml /etc/hadoop/core-site.xml")
        folder = input("\t\t\tEnter Directory: ")
        subprocess.getstatusoutput("sudo mkdir {}".format(folder))
        if not os.system("sudo cp BIGDATA/templates/hdfs-site/namenode/hdfs-site.xml /etc/hadoop/hdfs-site.xml"):
            return True

    elif current_type == "DataNode":
        os.system("sudo cp BIGDATA/templates/core-site/datanode/core-site.xml /etc/hadoop/core-site.xml")
        folder = input("\t\t\tEnter Directory: ")
        subprocess.getstatusoutput("sudo mkdir {}".format(folder))
        if not os.system("sudo cp BIGDATA/templates/hdfs-site/datanode/hdfs-site.xml /etc/hadoop/hdfs-site.xml"):
            return True

    else:
        os.system("sudo cp BIGDATA/templates/core-site/datanode/core-site.xml /etc/hadoop/core-site.xml")
        if not os.system("sudo cp BIGDATA/templates/hdfs-site/client/hdfs-site.xml /etc/hadoop/hdfs-site.xml"):
            return True
    return False


#####################################################################


def LocalCurrentNode():
    os.system('tput setaf 4')
    print(
        "\t\t\tCurrent system is.....\n\t\t\tEnter 1 For NameNode\n\t\t\tEnter 2 For DataNode\n\t\t\tEnter 3 For Client\n\t\t\tEnter 4 to return back")
    os.system('tput setaf 7')
    choice = input("\t\t\tEnter your Choice: ")
    if choice == "1":
        if LocalNodeConfigure("NameNode"):
            print("\t\t\tcompleted")
        else:
            print("\t\t\tSomething went Wrong")

    elif choice == '2':
        if LocalNodeConfigure("DataNode"):
            print("\t\t\tcompleted")
        else:
            print("\t\t\tSomething Went Wrong")
    elif choice == '3':
        if LocalNodeConfigure("Client"):
            print("\t\t\tClient Started.....")
        else:
            print("\t\t\tSomething Went Wrong")
    elif choice == '4':
        return
    else:
        print("\t\t\tSomething Went Wrong")


###################################################################################
###################################################################################


def RemoteHadoopInstall(username, password, Ip):
    status = None
    if 0 == subprocess.getstatusoutput("sudo yum install initscripts -y")[0]:
        if 0 == os.system("sshpass -p {}  ssh {}@{} yum install wget -y".format(password, username, Ip)):
            if 0 == os.system(
                    "sshpass -p {}  ssh {}@{} sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm".format(
                        password, username, Ip)) and 0 == os.system(
                "sshpass -p {}  ssh {}@{} sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm".format(
                    password, username, Ip)):
                if 0 == os.system(
                        "sshpass -p {}  ssh {}@{} rpm -ihv  jdk-8u171-linux-x64.rpm".format(password, username, Ip)):
                    status = os.system(
                        "sshpass -p {}  ssh {}@{} rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force".format(password, username,
                                                                                                     Ip))
    if status == 0:
        print("\t\t\tHadoop successfully installed  in your system")
    else:
        print("\t\t\tsomething went wrong please contact support team")


###############################################################################


def RemoteNodeConfigure(current_type, username, password, Ip):
    # HDFS-Site file Configure
    if current_type == "NameNode":
        os.system(
            "sshpass -p {} scp BIGDATA/templates/core-site/namenode/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(
                password, username, Ip))
        folder = input("\t\t\tEnter CurrentNode Directory: ")
        subprocess.getoutput("sshpass -p {} ssh {}@{} sudo mkdir {}".format(password, username, Ip, folder))
        if not os.system(
                "sshpass -p {} scp BIGDATA/templates/hdfs-site/namenode/hdfs-site.xml {}@{}:/etc/hadoop/hdfs-site.xml".format(
                    password, username, Ip)):
            return True

    elif current_type == "DataNode":
        os.system(
            "sshpass -p {} scp BIGDATA/templates/core-site/datanode/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(
                password, username, Ip))
        folder = input("\t\t\tEnter CurrentNode Directory: ")
        subprocess.getoutput("sshpass -p {} ssh {}@{} sudo mkdir {}".format(password, username, Ip, folder))
        if not os.system(
                "sshpass -p {} scp  BIGDATA/templates/hdfs-site/datanode/hdfs-site.xml {}@{}:/etc/hadoop/hdfs-site.xml".format(
                    password, username, Ip)):
            return True

    else:
        os.system(
            "sshpass -p {} scp BIGDATA/templates/core-site/datanode/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(
                password, username, Ip))
        if not os.system(
                "sshpass -p {} scp  BIGDATA/templates/hdfs-site/client/hdfs-site.xml {}@{}:/etc/hadoop/hdfs-site.xml".format(
                    password, username, Ip)):
            return True

    return False


########################################################################


def RemoteCurrentNode(username, password, Ip):
    os.system('tput setaf 4')
    print(
        "\n\t\t\tCurrent system is.....\n\t\t\tEnter 1 For NameNode\n\t\t\tEnter 2 For DataNode\n\t\t\tEnter 3 For Client\n\t\t\tEnter 4 to return back")
    os.system('tput setaf 7')
    choice = input("\t\t\tEnter your Choice: ")
    if choice == "1":
        if RemoteNodeConfigure("NameNode", username, password, Ip):
            print("\t\t\tcompleted")
        else:
            print("\t\t\tSomething went Wrong")
    elif choice == '2':
        if RemoteNodeConfigure("DataNode", username, password, Ip):
            print("\t\t\tcompleted")
        else:
            print("Something went Wrong")
    elif choice == '3':
        if RemoteNodeConfigure("Client", username, password, Ip):
            print("\t\t\tCompleted")
        else:
            print("\t\t\tSomething went Wrong")
    elif choice == '4':
        return
    else:
        print("\t\t\twrong choice")


########################################################################
########################################################################


def CloudHadoopInstall(username, key_path, Ip):
    status = None
    if 0 == subprocess.getstatusoutput(
            "ssh -i {} {}@{} sudo yum install initscripts -y".format(key_path, username, Ip))[0]:
        if 0 == os.system("ssh -i {} {}@{} sudo yum install wget -y".format(key_path, username, Ip)):
            if 0 == os.system(
                    "ssh -i {} {}@{} sudo wget https://hadoop-bucket9.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm".format(
                        key_path, username, Ip)) and 0 == os.system(
                "ssh -i {} {}@{} sudo wget https://hadoop-bucket9.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm".format(
                    key_path, username, Ip)):
                if 0 == os.system(
                        "ssh -i {} {}@{} sudo rpm -ihv  jdk-8u171-linux-x64.rpm".format(key_path, username, Ip)):
                    status = os.system(
                        "ssh -i {} {}@{} sudo rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force".format(key_path, username,
                                                                                                 Ip))
    if status == 0:
        print("\t\t\tHadoop successfully installed  in your system")
    else:
        print("\t\t\tsomething went wrong")

    ########################################################################


def CloudNodeConfigure(current_type, username, key_path, Ip):
    # HDFS-Site file Configure
    if current_type == "NameNode":
        if not os.system(
                "scp -i {}  /root/master_files/core-site.xml {}@{}:/home/{}/".format(key_path,
                                                                                                       username, Ip,
                                                                                                       username)) and not os.system(
            "ssh -i {} {}@{} sudo cp core-site.xml /etc/hadoop/core-site.xml".format(key_path, username,
                                                                                     Ip)) and not os.system(
            "ssh -i {} {}@{} sudo rm core-site.xml".format(key_path, username, Ip)):
            pass
        else:
            return False
        folder = input("\t\t\tEnter Directory: ")
        subprocess.getoutput("ssh -i {} {}@{} sudo mkdir {}".format(key_path, username, Ip, folder))
        if not os.system("scp -i {} /root/master_files/hdfs-site.xml {}@{}:/home/{}/".format(key_path,
                                                                                                               username,
                                                                                                               Ip,
                                                                                                               username)) and not os.system(
            "ssh -i {} {}@{} sudo cp hdfs-site.xml /etc/hadoop/hdfs-site.xml".format(key_path, username,
                                                                                     Ip)) and not os.system(
            "ssh -i {} {}@{} sudo rm hdfs-site.xml".format(key_path, username, Ip)):
            return True
    elif current_type == "DataNode":
        if not os.system(
                "scp -i {}  /root/slave_files/core-site.xml {}@{}:/home/{}/".format(key_path,
                                                                                                       username, Ip,
                                                                                                       username)) and not os.system(
            "ssh -i {} {}@{} sudo cp core-site.xml /etc/hadoop/core-site.xml".format(key_path, username,
                                                                                     Ip)) and not os.system(
            "ssh -i {} {}@{} sudo rm core-site.xml".format(key_path, username, Ip)):
            pass
        else:
            return False
        folder = input("\t\t\tEnter Directory: ")
        subprocess.getoutput("ssh -i {} {}@{} sudo mkdir {}".format(key_path, username, Ip, folder))
        if not os.system("scp -i {} /root/slave_files/hdfs-site.xml {}@{}:/home/{}/".format(key_path,
                                                                                                               username,
                                                                                                               Ip,
                                                                                                               username)) and not os.system(
            "ssh -i {} {}@{} sudo cp hdfs-site.xml /etc/hadoop/hdfs-site.xml".format(key_path, username,
                                                                                     Ip)) and not os.system(
            "ssh -i {} {}@{} sudo rm hdfs-site.xml".format(key_path, username, Ip)):
            return True
    else:
        if not os.system(
                "scp -i {}  BIGDATA/templates/core-site/datanode/core-site.xml {}@{}:/home/{}/".format(key_path,
                                                                                                       username, Ip,
                                                                                                       username)) and not os.system(
            "ssh -i {} {}@{} sudo cp core-site.xml /etc/hadoop/core-site.xml".format(key_path, username,
                                                                                     Ip)) and not os.system(
            "ssh -i {} {}@{} sudo rm core-site.xml".format(key_path, username, Ip)):
            pass
        else:
            return False
        if not os.system(
                "scp -i {} BIGDATA/templates/hdfs-site/client/hdfs-site.xml {}@{}:/home/{}/".format(key_path, username,
                                                                                                    Ip,
                                                                                                    username)) and not os.system(
            "ssh -i {} {}@{} sudo cp hdfs-site.xml /etc/hadoop/hdfs-site.xml".format(key_path, username,
                                                                                     Ip)) and not os.system(
            "ssh -i {} {}@{} sudo rm hdfs-site.xml".format(key_path, username, Ip)):
            return True
    return False


##########################################################################

def CloudCurrentNode(username, key_path, Ip):
    os.system('tput setaf 4')
    print(
        "\n\t\t\tCurrent system is.....\n\t\t\tEnter 1 For NameNode\n\t\t\tEnter 2 For DataNode\n\t\t\tEnter 3 For Client\n\t\t\tEnter 4 to return back")
    os.system('tput setaf 7')
    choice = input("\t\t\tEnter your Choice: ")
    if choice == "1":
        if CloudNodeConfigure("NameNode", username, key_path, Ip):
            print("\t\t\tcompleted")
        else:
            print("\t\t\tSomething went Wrong")

    elif choice == '2':
        if CloudNodeConfigure("DataNode", username, key_path, Ip):
            print("\t\t\tCompleted")
        else:
            print("\t\t\tSomething went Wrong")
    elif choice == '3':
        if CloudNodeConfigure("Client", key_path, username, Ip):
            print("\t\t\tClient Started.....")
        else:
            print("\t\t\tSomething went Wrong")
    elif choice == '4':
        return
    else:
        print("\t\t\twrong choice ")


####################################################################################
####################################################################################
####################################################################################


def HadoopMainMenu():
    os.system('tput setaf 3')
    print("\t\t=====================================================")
    print("\t\t\tWelcome to Hadoop menu !!")
    print("\t\t=====================================================")
    os.system('tput setaf 4')

    ostype = input(
        """\n\t\tEnter local to work on local operating system\n\t\tEnter remote to work on remote operating system\n\t\t:""")
    if ostype == "local":
        while True:
            os.system('tput setaf 4')
            print(
                "\n\t\tEnter 1 to install hadoop\n\t\tEnter 2 to configure node\n\t\tEnter 3 to format name-node\n\t\tEnter 4 to start/stop hadoop service"
                "\n\t\tEnter 5 to get cluster report\n\t\tEnter 6 to  see all files\n\t\tEnter 7 to put/rm/read File\n\t\tEnter 8 to return")

            os.system('tput setaf 7')
            choice = input("\t\tEnter your choice: ")

            if choice == "1":
                LocalHadoopInstall()
            elif choice == "2":
                LocalCurrentNode()
            elif choice == '3':
                os.system("hadoop namenode -format")
            elif choice == "4":
                s = input("\t\tEnter start/stop hadoop service : ")
                if s == "start":
                    service = input("\t\tservice NameNode/Datanode : ")
                    if service.lower() == "namenode":
                        os.system("hadoop-daemon.sh start namenode")
                    elif service.lower() == "datanode":
                        os.system("hadoop-daemon.sh start datanode")
                elif s == "stop":
                    service = input("\t\tservice NameNode/Datanode : ")
                    if service.lower() == "namenode":
                        os.system("hadoop-daemon.sh stop namenode")
                    elif service.lower() == "datanode":
                        os.system("hadoop-daemon.sh stop datanode")
                else:
                    print("\t\twrong input ")
            elif choice == "5":
                os.system("hadoop dfsadmin -report")
            elif choice == "6":
                os.system("hadoop fs -ls /")
            elif choice == "7":
                c = input("\t\tEnter put/rm/read File")
                if c.lower() == 'put':
                    file_name = input("\t\tEnter file name [PATH/filename] : ")
                    os.system("hadoop fs -put {} /".format(file_name))
                elif c.lower() == "rm":
                    file_name = input("\t\tEnter File name : ")
                    os.system("hadoop fs -rm /{}".format(file_name))
                elif c.lower() == "read":
                    file_name = input("\t\tEnter file name : ")
                    os.system("hadoop fs -cat /{}".format(file_name))
            elif choice == "8":
                return
            else:
                print("\t\tnot supported")
            input("\t\tPress Enter to continue........")
            os.system('clear')

    elif ostype == "remote":
        username = input("\t\tEnter os username : ").strip()
        ip = input("\t\tEnter os ip: ").strip()
        key_or_password = input("\t\tConnect using password/Key : ").strip()
        if key_or_password.lower() == "password" or key_or_password == "pass":
            password = getpass.getpass("Enter password: ")
            os.system("yum install sshpass")
            while True:
                os.system('tput setaf 4')
                print(
                    "\n\t\tEnter 1 to install hadoop\n\t\tEnter 2 for configure node\n\t\tEnter 3 to format name-node\n\t\tEnter 4 for start/stop hadoop service"
                    "\n\t\tEnter 5 for get cluster report\n\t\tEnter 6 to see all files in cluster\n\t\tEnter 7 to put/rm/read File\n\t\tEnter 8 to return")
                os.system('tput setaf 7')
                choice = input("\t\tEnter you choice : ")
                if choice == "1":
                    RemoteHadoopInstall(username, password, ip)
                elif choice == "2":
                    RemoteCurrentNode(username, password, ip)
                elif choice == "3":
                    os.system(
                        "sshpass -p {} ssh {}@{} hadoop namenode -format".format(password, username, ip))
                elif choice == "4":
                    s = input("\t\tEnter start/stop hadoop service : ")
                    if s == "start":
                        service = input("\t\tservice NameNode/Datanode : ")
                        if service.lower() == "namenode":
                            os.system(
                                "sshpass -p {} ssh {}@{} hadoop-daemon.sh start namenode".format(password, username,
                                                                                                 ip))
                            os.system('sleep 5')
                            service_state = subprocess.getstatusoutput(
                                "sshpass -p {} ssh {}@{} sudo jps".format(password, username, ip))
                            if service_state[0] == 0 and 'NameNode' in service_state[1]:
                                print("\t\tNameNode Started")
                            else:
                                print("\t\tfailed to start service")
                        elif service.lower() == "datanode":
                            os.system(
                                "sshpass -p {} ssh {}@{} hadoop-daemon.sh start datanode".format(password, username,
                                                                                                 ip))
                            os.system('sleep 3')
                            service_state = subprocess.getstatusoutput(
                                "sshpass -p {} ssh {}@{} sudo jps".format(password, username, ip))
                            if service_state[0] == 0 and 'DataNode' in service_state[1]:
                                print("\t\tDataNode Started")
                            else:
                                print("\t\tfailed to start service")
                        else:
                            print("\t\tWrong Input")
                    elif s == "stop":
                        service = input("\t\tservice NameNode/Datanode:")
                        if service.lower() == "namenode":
                            os.system(
                                "sshpass -p {} ssh {}@{} hadoop-daemon.sh stop namenode".format(password, username, ip))
                        elif service.lower() == "datanode":
                            os.system(
                                "sshpass -p {} ssh {}@{} hadoop-daemon.sh stop datanode".format(password, username, ip))
                        else:
                            print("\t\tWrong Input")
                    else:
                        print("\t\twrong input ")
                elif choice == '5':
                    os.system(
                        "sshpass -p {} ssh {}@{} hadoop dfsadmin -report".format(password, username, ip))
                elif choice == '6':
                    os.system(
                        "sshpass -p {} ssh {}@{} hadoop fs -ls /".format(password, username, ip))
                elif choice == "7":
                    c = input("\t\tEnter put/rm/read File")
                    if c.lower() == 'put':
                        file_name = input("\t\tEnter file name [PATH/filename] : ")
                        os.system(
                            "sshpass -p {} ssh {}@{} hadoop fs -put {} /".format(password, username, ip, file_name))
                    elif c.lower() == "rm":
                        file_name = input("\t\tEnter File name : ")
                        os.system("sshpass -p {} ssh {}@{} hadoop fs -rm /{}".format(password, username, ip, file_name))
                    elif c.lower() == "read":
                        file_name = input("\t\tEnter file name : ")
                        os.system(
                            "sshpass -p {} ssh {}@{} hadoop fs -cat /{}".format(password, username, ip, file_name))
                elif choice == '9':
                    exit()
                else:
                    print("\t\tnot supported")
                input("\t\tPress Enter to continue........")
                os.system('clear')
        elif key_or_password.lower() == "key":
            key = input("\t\tEnter key in this format { PATH/KeyName.pem } : ")
            while True:
                os.system('tput setaf 4')
                print(
                    "\n\t\tEnter 1 to install hadoop\n\t\tEnter 2 for configure node\n\t\tEnter 3 to format namenode\n\t\tEnter 4 start/stop hadoop service"
                    "\n\t\tEnter 5 to get cluster report\n\t\tEnter 6 to see all files in cluster\n\t\tEnter 7 to put/read/rm file in cluster\n\t\tEnter 8 to return")
                os.system('tput setaf 7')
                choice = input("\t\tEnter your choice: ")
                if choice == "1":
                    CloudHadoopInstall(username, key, ip)
                elif choice == "2":
                    CloudCurrentNode(username, key, ip)
                elif choice == "3":
                    os.system("ssh -i {} {}@{} sudo hadoop namenode -format".format(key, username, ip))
                elif choice == "4":
                    s = input("\t\tEnter start/stop hadoop service : ")
                    if s == "start":
                        service = input("\t\tservice NameNode/Datanode : ")
                        if service.lower() == "namenode":
                            os.system(
                                "ssh -i {} {}@{} sudo hadoop-daemon.sh start namenode".format(key, username, ip))
                            os.system('sleep 3')
                            service_state = subprocess.getstatusoutput(
                                "ssh -i {} {}@{} sudo jps".format(key, username, ip))
                            if service_state[0] == 0 and 'NameNode' in service_state[1]:
                                print("\t\tNameNode Started")
                            else:
                                print("\t\tfailed to start service")
                        elif service.lower() == "datanode":
                            os.system(
                                "ssh -i {} {}@{} sudo hadoop-daemon.sh start datanode".format(key, username, ip))
                            os.system('sleep 3')
                            service_state = subprocess.getstatusoutput(
                                "ssh -i {} {}@{} sudo jps".format(key, username, ip))
                            if service_state[0] == 0 and 'DataNode' in service_state[1]:
                                print("\t\tDataNode Started")
                            else:
                                print("\t\tfailed to start service")
                        else:
                            print("\t\tWrong Input")

                    elif s == "stop":
                        service = input("\t\tservice NameNode/Datanode : ")
                        if service.lower() == "namenode":
                            os.system(
                                "ssh -i {} {}@{} sudo hadoop-daemon.sh stop namenode".format(key, username, ip))
                        elif service.lower() == "datanode":
                            os.system(
                                "ssh -i {} {}@{} sudo hadoop-daemon.sh stop datanode".format(key, username, ip))
                        else:
                            print("\t\tWrong Input")
                    else:
                        print("\t\twrong input ")
                elif choice == '5':
                    os.system(
                        "ssh -i {} {}@{} sudo hadoop dfsadmin -report".format(key, username, ip))
                elif choice == '6':
                    os.system(
                        "ssh -i {} {}@{} sudo hadoop fs -ls /".format(key, username, ip))
                elif choice == "7":
                    c = input("\t\tEnter put/rm/read File")
                    if c.lower() == 'put':
                        file_name = input("\t\tEnter file name [PATH/filename] : ")
                        os.system("ssh -i {} {}@{} hadoop fs -put {} /".format(key, username, ip, file_name))
                    elif c.lower() == "rm":
                        file_name = input("\t\tEnter File name : ")
                        os.system("ssh -i {} {}@{} hadoop fs -rm /{}".format(key, username, ip, file_name))
                    elif c.lower() == "read":
                        file_name = input("\t\tEnter file name : ")
                        os.system("ssh -i {} {}@{} hadoop fs -cat /{}".format(key, username, ip, file_name))
                elif choice == '8':
                    return
        else:
            print("\t\tnot supported")
        input("\t\tPress Enter to continue........")
        os.system('clear')
