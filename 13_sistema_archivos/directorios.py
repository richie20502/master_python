import os
import shutil

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("ya existe el difrectorio")

#eliminar carpeta
#os.rmdir("./mi_carpeta")
r1= "./mi_carpeta"
r2="./mi_carpeta_copia"
shutil.copytree(r1, r2)