import re

regex = '^[a-z0-9]+[\-_]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def main():

    mail = input("Lütfen uygun bir e posta adresi giriniz: ")

    if(re.search(regex, mail)):
        print("Girdiğiniz mail doğrudur")

    else:
        print("Girdiğiniz mail yanlıştır.")


if __name__ == "__main__":
    main()
