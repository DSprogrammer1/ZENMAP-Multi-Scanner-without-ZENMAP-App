#!/usr/bin/env python
# -*- coding utf-8 -*-

import os 

def operations():
	print("""  
	+++++++⚠️ZENMAP SCAN OPERATIONS⚠️+++++++++
	😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️
	  				   😈️
	  				  😈️
	  			        😈️
	  			      😈️
	  			    😈️
	  		          😈️
	  		        😈️
	  	    	      😈️
	  		   😈️
	  		 😈️
	  	       😈️
	  	     😈️
	 	   😈️
	 	 😈️
	       😈️
	     😈️
	   😈️
	 😈️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️
       😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️😈️
       ☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️
	-----------------------------------------
	Please Enter Target Adress for Quick Scan
	--quick 		Quick Scan
	--intense		Intense Scan
	--intense-all		All Ports Intense Scan
	--intense-no-ping	No ping in Scan
	--ping-scan		Ping Scan in NMAP
	--quick-plus		Qucik plus scan
	------------------------------------------
	☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️
	""")
	print("Please enter the operation key_word: \n---> ")
	key_word=input()
	if(key_word=="--quick"):
		ip_adress=input("Please Input Target ip Address: ")
		os.system("nmap -T4 -F "+ip_adress)
	if(key_word=="--intense"):
		ip_adress=input("Please Input Target ip Address: ")
		os.system("nmap -T4 -A -v "+ip_adress)
	if(key_word=="--intense-all"):
		ip_adress=input("Please Input Target ip Address: ")
		os.system("nmap -p 1-65535 -T4 -A -v "+ip_adress)
	if(key_word=="--ping-scan"):
		ip_adress=input("Please Input Target ip Address: ")
		os.system("nmap -sn "+ip_adress)
	if(key_word=="--quick-plus"):
		ip_adress=input("Please Input Target ip Address: ")
		os.system("nmap -sV -T4 -O -F -version-light " +ip_adress)
	else:
		print("Syntax Error ")

operations()
