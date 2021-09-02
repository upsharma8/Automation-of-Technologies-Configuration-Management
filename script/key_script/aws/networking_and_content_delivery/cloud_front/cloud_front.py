import os


def cloudFront():
    while True:
        cf = input('Press 1: for creating distribution')
        if cf == "1":
            bucketnm = input("\n ENTER RESPECTIVE BUCKET NAME:")
            objectnm = input("\n ENTER THE OBJECT NAME YOU WANT TO DISTRIBUTE [optional]:")
            os.system(
                "aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(
                    bucketnm, objectnm))
        else:
            print("Exit")
            return
        input("Enter to continue......")
        os.system("clear")
