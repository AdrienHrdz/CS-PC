import sys
import os

command = [
    ["/usr/bin/python3", ["python3","hello.py"]],
    ["/usr/bin/python3", ["python3","hello.py"]]
]


for i in range(len(command)):
    os.fork()
    os.execv(command[i][0], command[i][1])



#os.execv("/usr/bin/python3", ["python3","hello.py"])

#os.execlp("python3",'a', "./moyenne.py","13" ,"12","10")

#os.execlp("python3",'a', "./hello.py")