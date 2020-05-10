import os
os.system("clear")
while True:
	os.system("tput setaf 1")
	print("\t\t\t Installation of Docker")
	os.system("tput setaf 7")
	print("\t\t\t.......................")
	print("""
	Press 1: To check the file of docker-ce is exist
	Press 2: Install the software
	Press 3: Previous page 
	""")
	print("Enter your choice:",end="")
	ch2=int(input())
	if ch2==1:
		while(True):
			print("""
			Press 1: To check docker-ce is available in system
			Press 2: To create docker file as repository
			Press 3: To see the file
			Press 4: Previous page
			""")
			print("Enter your Choise:",end="")
			ch3=int(input())
			if(ch3==1):
				os.system("yum list docker-ce")
			elif(ch3==2):
				os.chdir("/etc/yum.repos.d")
				print("Enter the name of Docker file:",end="")
				docker_file=input()
				os.system("gedit {}.repo".format(docker_file))
			elif(ch3==3):
				os.chdir("/etc/yum.repos.d")
				os.system("ls")
			elif(ch3==4):
				break
			else:
				print("Choose correct option...")
	elif ch2==2:
		os.system("yum install docker-ce --nobest -y")
	elif ch2==3:
		break
	else:
		print("Choose correct option...")
	input("Enter to continue...")
	os.system("clear")

