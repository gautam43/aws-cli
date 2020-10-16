import speech_recognition as sr
import os
import subprocess
import pyttsx3
print("\t\t\tWelcome to the AWS Assistant")
print("\t\t\t----------------------------\n")

print("Speak your Requirements ... we are listening ..",end='')
r=sr.Recognizer()

with sr.Microphone() as source:
	print("Start saying..")
	audio = r.listen(source)
	print("we got it, plz wait....")

ch=r.recognize_google(audio)
print(ch)

volId=eval(subprocess.getoutput("aws ec2 describe-volumes  --filters  --query Volumes[-1].VolumeId "))

InstId=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].InstanceId "))

if ("create" in ch) and ("keypair" in ch or ("key" in ch and "pair" in ch) ):
	pyttsx3.speak("Enter the keyname")
	keyname=input("Enter the keyname :")
	os.system("aws ec2 create-key-pair --key-name {} ".format(keyname))
	pyttsx3.speak("Key pair created successfully")

elif ("delete" in ch) and ("keypair" in ch or ("key" in ch and "pair" in ch) ):
	pyttsx3.speak("Enter the keyname")
	keyname=input("Enter the keyname :")
	os.system("aws ec2 delete-key-pair --key-name {} ".format(keyname))
	pyttsx3.speak("Key pair deleted successfully")

elif ("list" in ch) and ("keypair" in ch or ("key" in ch and "pair" in ch) ):
	os.system("aws ec2 describe-key-pairs")

elif ("security" in ch) and ("group" in ch) and ("create" in ch):
	pyttsx3.speak("Enter the security group name")	
	secgrp=input("Enter the security group name :")
	#desc=created security grp with AWS-CLI
	os.system("aws ec2 create-security-group --description security --group-name {} ".format(secgrp) )
	pyttsx3.speak("security group created successfully")

elif ("security" in ch) and ("group" in ch) and ("delete" in ch):
	pyttsx3.speak("Enter the security group name")	
	secgrp=input("Enter the security group name :")
	os.system("aws ec2 delete-security-group --group-name {} ".format(secgrp) )
	pyttsx3.speak("security group deleted successfully")

elif ("list" in ch) and ("security" in ch) and ("groups" in ch):
		os.system("aws ec2 describe-security-groups")

elif ("launch" in ch) and ("instance" in ch):
	os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name gautam-aws --subnet-id subnet-933930fb --count 1 ")
	pyttsx3.speak("Instance launch successfully")

elif ("create" in ch) and ("volume" in ch):
	os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 1")
	pyttsx3.speak("volume created successfully")

elif ("start" in ch) and ("instance" in ch):
	os.system("aws ec2 start-instances --instance-ids {}".format(InstId) )
	pyttsx3.speak("Instance started successfully")

elif ("stop" in ch) and ("instance" in ch):
	os.system("aws ec2 stop-instances --instance-ids {}".format(InstId) )
	pyttsx3.speak("Instance stopped successfully")

elif ("terminate" in ch) and ("instance" in ch):
	os.system("aws ec2 terminate-instances --instance-ids {}".format(InstId) )
	pyttsx3.speak("Instance terminated successfully")

elif ("attach" in ch) and ("volume" in ch):
	os.system("aws ec2 attach-volume --volume-id {} --device /dev/sdf --instance-id {}".format(volId,InstId) )
	pyttsx3.speak("volume attached successfully")

elif ("thanks" in ch) or ("assistant" in ch) or ("quit" in ch):
	pyttsx3.speak("Welcome Gautam call me Whenever you want")
	