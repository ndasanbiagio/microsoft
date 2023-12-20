import os
import shutil

archivo = open('curso.txt','w')
archivo.write('texto de prueba')

shutil.move('curso.txt', "C:\\windows")



#Para eliminar se usa os.rm
#shutil.rmt elimina todo
















archivo.close()

print(os.listdir())