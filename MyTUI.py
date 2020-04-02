import os

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
exit
                                                                     1,4           Top
