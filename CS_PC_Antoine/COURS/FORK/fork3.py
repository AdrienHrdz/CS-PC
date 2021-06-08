import os
print("Je suis le processus PERE = ", os.getpid())
pid1 = os.fork()
print(pid1)
pid2 = os.fork()
print(pid2)
