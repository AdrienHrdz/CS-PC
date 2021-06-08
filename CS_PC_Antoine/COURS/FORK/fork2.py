import os
quiSuisJe = "le pere"
pid = os.fork()
if pid == 0 :
	quiSuisJe = "le fils"
	print("Je suis", quiSuisJe)
else :
	print("Je suis", quiSuisJe)
	os.wait()
os._exit(0)
