#miroir2
import sys

chaine_miroir = ''
temp_str = ''

for arg in sys.argv[1:]:
    for char in arg:
        temp_str = char + temp_str
    chaine_miroir = chaine_miroir + temp_str + ' '
    temp_str = ''

print(chaine_miroir)
