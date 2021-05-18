import os,sys

if len(sys.argv) < 2:
    print("pas de param")

print(sys.argv)

for arg in sys.argv[1:]:
    print(arg)

sys.exit()