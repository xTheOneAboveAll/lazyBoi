import sys

import time

import base64

import os

import requests

import socket

import re

from multiprocessing.dummy import Pool as asshole

# headers

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#logo 

logo = """\x1b[1;34;40m

        

   ┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋┏━━┓     

   ┃┃╋╋╋╋╋╋╋╋╋╋╋╋╋┃┏┓┃      

   ┃┃╋╋┏━━┳━━━┳┓╋┏┫┗┛┗┳━━┳┓    

   ┃┃╋┏┫┏┓┣━━┃┃┃╋┃┃┏━┓┃┏┓┣┫    

   ┃┗━┛┃┏┓┃┃━━┫┗━┛┃┗━┛┃┗┛┃┃    

   ┗━━━┻┛┗┻━━━┻━┓┏┻━━━┻━━┻┛      

   ╋╋╋╋╋╋╋╋╋╋╋┏━┛┃WE ARE LAZY   

   ╋╋╋╋╋╋╋╋╋╋╋┗━━┛WE ARE CRAZY    

    

      [RANGE 2 REVERSE]

    [FOR ONLY LAZY PEOPLE]    

       [XTHEONEABOVEALL]    

"""

#lists

lips = []

prips = []

# clear func

def clear():

	if os.name == 'nt':		os.system('cls')

	else:

		os.system('clear')

		

# reverse ip func

# you can change api and regex

def reverser(ip):

	payload = 'https://1337hub.000webhostapp.com/?ip='+ip

	try:

		getdom = requests.get(payload,headers=headers).content.decode('utf8')

		getdom =getdom.replace("<body style='background-color:black;color:white'><code","")

		doms = re.findall(r">(.*?)<",getdom)

		for dom in doms:

				print('[\x1b[1;34;40m'+ip+'\x1b[1;37;40m]  ➟  [ \x1b[1;32;40mREVERSED\x1b[1;37;40m]  ➟  [ \x1b[1;33;40m'+dom+'\x1b[1;37;40m]')

				open('reversed.txt','a').write(dom+'\n')

	except:

		pass

# multiprocess for reverse ip

def prev():

	# you can add more threads

	pool = asshole(10)

	pool.map(reverser,lips)

	pool.close()

	pool.join()

# live ip checker func

def liveip(ip):

	global lips

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	sock.settimeout(5)

	result = sock.connect_ex((ip,80))

	if result == 0:

		print('[\x1b[1;32;40mLIVE IP\x1b[1;37;40m]    ⪢   [\x1b[1;36;40m'+ip+'\x1b[1;37;40m]')

		lips.append(ip)

	else:

		print('[\x1b[1;31;40mDEAD IP\x1b[1;37;40m]    ⪢   [\x1b[1;31;40m'+ip+'\x1b[1;37;40m]')

# multiprocess for live ip func

def prelive():

	# you can check threads

	pool = asshole(100)

	pool.map(liveip,prips)

	pool.close()

	pool.join()

	

# ip ranging func

def ranger(ip):

	global prips

	part = ip.split('.')

	part1 = part[0]

	part2 = part[1]

	for part3 in range(256):

			for part4 in range(256):

				ranged = part1+'.'+part2+'.'+str(part3)+'.'+str(part4)

				prips.append(ranged)

# check used ip func

def usedip():

	global uxip

	try:

		uxip = open('usedip.txt','r').read()

	except:

		open('usedip.txt','w+')

		uxip = ""

# domain to ip func		

def getip(url):

	clear()

	usedip()

	global uxip

	url=url.replace('\r','').replace('\n','').replace('https://','').replace('http://','').replace('/','')

	try:

		ip = socket.gethostbyname(url)

		if ip in uxip:

			print('[ \x1b[1;37;41mUSED IP \x1b[2;37;40m ]    ⋙   [ \x1b[1;37;41m'+ ip+

			'\x1b[1;37;40m] ')

		else:

			print('[ \x1b[1;37;42m'+url+'\x1b[2;37;40m ]    ⋙   [ \x1b[1;37;42m'+ ip+

			'\x1b[1;37;40m] ')

			open('usedip.txt','a').write(ip+'\n')

			uxip = uxip+ip+'\n'

			time.sleep(1)

			clear()

			print('\x1b[2;37;43m [Ranging....*_*] \x1b[0;37;40m')

			time.sleep(1)

			ranger(ip)

			clear()

			print('\x1b[1;37;43m [Checking live ips....*_*] \x1b[0;37;40m')

			time.sleep(1)

			prelive()

			clear()

			print('\x1b[1;37;43m [Reverse live ips....*_*] \x1b[0;37;40m')

			time.sleep(1)

			prev()

	except:

		print('[ \x1b[1;37;41m'+url+'\x1b[2;37;40m ]    ⋙   [ \x1b[1;37;41mDEAD SITE\x1b[1;37;40m] ')

# clean lists

def clnst():

	global prips

	global lips

	prips = []

	lips = []

	

# main

def main():

	clear()

	print(logo)

	urls=open(input('\x1b[0;37;40mSite List ⌦  '),'r+').readlines()

	for url in urls:

		clnst()

		getip(url)

		

main()

		
