import os
import time 
for horas in range(24):
    for minutos in range (60):
        for segundos in range (60):
            os.system ("cls")
            print(f"El tiempo que llevas jugando es de: {horas}:{minutos}:{segundos}")
            time.sleep(1)