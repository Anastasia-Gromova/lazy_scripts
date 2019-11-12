import os
import re
import time
import thread

a = os.popen('ls ~/Documents/OOP/lectures').read()
max_value =  max(map(int, re.findall(r'\d+', a)))

string1 = 'xdotool type ~/Documents/OOP/lectures && xdotool key Return'

def ecl():
	os.system('~/Desktop/Link_to_eclipse')

def ecl2():
	os.system('xdotool key BackSpace')
	os.system(string1)

thread.start_new(ecl, ())

def check():
	proccess = os.popen('top -b -n1')
	b = proccess.readlines()
	for i in range(len(b)):
		if 'java' in b[i]:
			temp = [value for value in b[i].split(' ') if value != '']
			temp[8].replace(',', '.')
			if float(temp[8].replace(',', '.')) < 5:
				print temp[8]
				return 1
	return 0

i = 0
while i == 0:
	i += check()
	time.sleep(0.7)

thread.start_new(ecl2, ())

j = 0
while j == 0:
	j += check()
	time.sleep(0.7)

os.system('xdotool key ctrl+n')
time.sleep(1)

os.system('xdotool type Java && xdotool key space && xdotool type Project')
time.sleep(1)
os.system('xdotool key Return')

string2 = 'xdotool type lecture_' + str(max_value + 1) + ' && xdotool key Return'
os.system(string2)
