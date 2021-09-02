from cloud_front import cloud_front
from route53 import route53
from vpc import vpc

while True:
    print("""
    Press 1: CloudFormation 
    Press 2: Route53
    Press 3: VPC 
    """)
    choice = input("Enter your Choice: 1")
    if choice == '1':
        cloud_front.cloudFront()
    elif choice == '2':
        route53.Route53()
    elif choice == '3':
        vpc.VPC()
    else:
        exit(0)
