import os
import re
import time
import thread

# store the directories in the workspace
a = os.popen('ls ~/Documents/OOP/lectures').read()

# find the maximum integer, containing in the name of the directory 
# in this case they are called lecture_1, lecture_2 etc. We want to create project for the next lecture
max_value =  max(map(int, re.findall(r'\d+', a)))

# type the name of the workspace in eclipse and press enter. Will be used as a terminal command
string1 = 'xdotool type ~/Documents/OOP/lectures && xdotool key Return'

def ecl():
	os.system('~/Desktop/Link_to_eclipse')

def ecl2():
	os.system('xdotool key BackSpace')
	os.system(string1)

# starting thread to continue scripting commands with the running eclipse
thread.start_new(ecl, ())

# checks for the %CPU, if eclipse loaded
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

# same with next commands
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

''' Another method to do that is to open full screen, so that the menu 
    would be always on the same place and click whenever you need.
    To check the location of the coursor, you can use 'xdotool getmouselocation'
    
    os.system('xdotool key ctrl+super+Up')
    os.system('xdotool mousemove 327 386 click 1')
    '''

# type the name of the project folder for the next lesson and press enter.
string2 = 'xdotool type lecture_' + str(max_value + 1) + ' && xdotool key Return'
os.system(string2)
