elif c==3:
    os.system("ls -f")
    print()
elif c==4:
    print("Enter file name : ",end="")
    f=input()
    os.system("touch "+f)
    print("File successfully created")
elif c==5:
    os.system(live)
    #print("Exiting...")
    #os.system("sleep 2")
    #exit()
else:
    print("Next time choose wisely...")
    os.system(live)
    #print("Exiting in ")
    #exit()

os.system("tput setaf 7")
exit()


                                                              63,0-1        Bot
