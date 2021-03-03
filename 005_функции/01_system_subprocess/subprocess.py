
import os

os.environ['DISPLAY']=':0.0'
print('echo $DISPLAY')
# print(os.WEXITSTATUS(os.system('echo $DISPLAY')))
os.system('echo $DISPLAY')
# return_value = os.popen('ls').read()
# subprocess.run(..., check=True)
# subprocess.check_output() or subprocess.Popen()
# arch = subprocess.check_output("uname -a | awk '{print $9}'", shell=True)
# subprocess.call(cmd, shell=True)
import subprocess

cmd = "date"
returned_output = subprocess.check_output(cmd)  # returns output as byte string

print('Current date is:', returned_output.decode("utf-8"))  # using decode() function to convert byte string to string

print(os.popen('echo $DISPLAY').read())