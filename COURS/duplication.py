import os

print("pid père : ", os.getpid())
pid = os.fork()
print("pid fils : ", pid)