#coding=utf-8
import os
import time

commands = []

commands.append("""""")

for i in range(len(commands)):
    cur_command = commands[i]
    print(cur_command)
    os.system(cur_command)
    time.sleep(2)