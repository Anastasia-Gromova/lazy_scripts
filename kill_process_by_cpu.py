import os

# stores the output from top command
process = os.popen('top -b -n1')
b = process.readlines()

# starting point
check = b[0]
i = 0

# running untill there comes the list of processes
while '%CPU' not in b[i]:
        i += 1

# getting PID from the next line (first line in the list - the highest CPU)
ID =  b[i+1].split(' ')[0]

os.system('kill -9 ' + ID)
