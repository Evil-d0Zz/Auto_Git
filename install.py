from os import system
from time import sleep

system("sudo chmod +x auto_git")
sleep(2)
system("sudo cp -r auto_git /bin/")
system("auto_git")
