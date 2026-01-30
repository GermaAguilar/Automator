import os
import shutil

# 1. Define la ruta de la carpeta que quieres organizar
# Nota: Cambia 'Carpeta_Prueba' por una ruta real, ej: 'C:/Users/TuUsuario/Downloads'
ruta = 'C:/Users/gaguilar/Downloads'

# 2. Diccionario de organización
formatos = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Instaladores': ['.exe', '.msi', '.dmg'],
    'Archivos': ['.doc', '.xls ', '.xlsm']  
}

# 3. La magia ocurre aquí
def organizar():
    # Listamos los archivos en la ruta
    for archivo in os.listdir(ruta):
        nombre, extension = os.path.splitext(archivo)
        
        # Buscamos a qué carpeta pertenece la extensión
        for carpeta, lista_extensiones in formatos.items():
            if extension.lower() in lista_extensiones:
                ruta_carpeta = os.path.join(ruta, carpeta)
                
                # Si la carpeta no existe, la creamos
                if not os.path.exists(ruta_carpeta):
                    os.makedirs(ruta_carpeta)
                
                # Movemos el archivo
                shutil.move(os.path.join(ruta, archivo), os.path.join(ruta_carpeta, archivo))
                print(f"Movido: {archivo} -> {carpeta}")

if __name__ == "__main__":
    organizar()
    print("¡Limpieza completada!")