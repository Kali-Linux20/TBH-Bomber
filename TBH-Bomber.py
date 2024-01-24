#---------------import------------------#
import  os,sys,time,requests,random,string
import shutil
from requests.structures import CaseInsensitiveDict
#--------------------clear------------------#
os.system("clear")
#--------------------coller------------------#
RED = '\033[1;31m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
sai="\033[1;30m"#à¦›à¦¾à¦‡
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
perpal = '\033[1;35m'
crim='\033[1;36m'
#--------------- slowly print----------------------#
def slowprint(s):
	for c in s + '\n' :
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(5. / 100)
#--------------- variable--------------- #

columns = shutil.get_terminal_size().columns
localTime = time.localtime()
tim=time.strftime("%I:%M:%S", localTime)

#--------------- check internet connection----------------------#
try:
 request = requests.get("https://www.google.com/", timeout=2)
 print("\n\033[1;37m[\033[1;32m#\033[1;37m]"+"\033[1;32m Connetcted ")
 time.sleep(3)
except (requests.ConnectionError, requests.Timeout) as exception:
 print("\n\033[1;37m[\033[1;32m#\033[1;37m] \033[1;31m Your Internet Connection Is Poor !")
 time.sleep(3)
#--------------- check update ----------------------#

def update():
	toolVersion="4"
	mainVersion = requests.get('https://github.com/Kali-Linux20/Update/blob/main/Bomber.txt').text
	if toolVersion in mainVersion:
		pass
	else:
		slowprint("\n    \033[92m[\033[37m!\033[92m] \033[37mTool Update Found!")
		time.sleep(0.5)
		slowprint("    \033[92m[\033[37m!\033[92m] \033[37mUpdating Tool: ", end="")
		os.system("cd .. && rm -rf TBH-Bomber && git clone https://github.com/Kali-Linux20/TBH-Bomber > /dev/null 2>&1")
		print("\033[37mDone")
		slowprint("\n    \033[92m[\033[37m*\033[92m] \033[37mStarting Tool...")
		time.sleep(0.8)
		os.system("cd .. && cd TBH-Bomber && python TBH-Bomber.py")
		
update()
print("kali is king")
print("kali is king")
