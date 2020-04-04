import os

while True:
    os.system("clear")
    os.system("tput setaf 1")

    print("\t\t\t Welcome to my TUI")
    print("\t\t\t*-----------------*")

    os.system("tput setaf 4")

    print("""
    Press 1 : To see currrent date and time
    Press 2 : To see Calander
    Press 3 : To list files
    Press 4 : To create file
    Press 5 : To exit
    """)

    os.system("tput setaf 3")

    live="""a=3
    while [ $a -ge 0 ]
    do
    echo -ne "Exiting...$a`sleep 1`\b\b\b\b\b\b\b\b\b\b\b"
    a=$((a-1))
    done
    """

    print("Enter your choice : ",end="")
    c=int(input())
    print()

    os.system("tput setaf 6")

    if c==1:
        os.system("date")
        print()
    elif c==2:
        os.system("cal")
    elif c==3:
        os.system("ls -f")
        print()
    elif c==4:
        print("Enter file name : ",end="")
        f=input()
        os.system("touch {0}".format(f))
        print("File successfully created")
        print()
    elif c==5:
        os.system(live)
        #print("Exiting..")
        os.system("tput setaf 7")
        exit()
    else:
        print("Next time choose wisely...")
        os.system(live)
        #print("Exiting in ")
        os.system("tput setaf 7")
        exit()

    print("Press ENTER to continue ...")
    input()
