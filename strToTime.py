import re
import time

day=60*60*24
today=time.time()

def strToTime(ds):
	if(re.match(r'(?i)^today$',ds)):
		return 	today								#time.strftime("%A-%d-%B-%Y",time.localtime(today))

	elif(re.match(r'(?i)^tomorrow$',ds)):
		return today+day

	elif(re.match(r'(?i)^yesterday$',ds)):
		return today-day
	
	elif(re.match(r'(?i)next (\w+)',ds)):
		the_day=re.match(r'(?i)^next (\w+)$',ds).group(1)
		this_day=today+day
		while(not re.match(r"(?i)^"+time.strftime("%A",time.localtime(this_day))+"$",the_day)):
			this_day+=day
		return this_day	
	
	elif(re.match(r'(?i)last (\w+)',ds)):
		the_day=re.match(r'(?i)^last (.*)$',ds).group(1)
		this_day=today-day
		while(not re.match(r"(?i)^"+time.strftime("%A",time.localtime(this_day))+"$",the_day)):
			this_day-=day
		return this_day		

print(strToTime("last tuesday"))
print(time.strftime("%A-%d-%B-%Y",time.localtime(strToTime("last sUnday"))))
#print(time.strftime("%A",time.localtime(today)))		