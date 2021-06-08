import os
print("PID du PERE : ", os.getpid())
pid= os.fork()
print("PID du FILS : ", pid)
