import os
os.system("clear")
while(True):	
	os.system("tput setaf 1")
	print("\t\t\t Configure Docker")
	os.system("tput setaf 7")
	print("\t\t\t ................")
	print("""
	Press 1:Check installation of Docker-ce
	Press 2:To install Docker-ce
	Press 3:Services
	Press 4:Previous page
	""")
	print("Enter your choice:",end="")
	ch1=int(input())
	if ch1==1:
		os.system("rpm -q docker-ce")
	elif ch1==2:
		os.system("python3 install_docker.py")
	elif ch1==3:
		os.system("setenforce 0")			
		os.system("systemctl start docker")
		os.system("systemctl enable docker")
		os.system("systemctl status docker")
	elif ch1==4:
		os.chdir("/root/project")
		break
	else:
		print("Choose correct option...")
	input("Enter to continue...")
	os.system("clear")


