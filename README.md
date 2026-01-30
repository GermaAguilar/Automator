# File Organizer Python

Un script sencillo y eficiente para mantener tu carpeta de descargas (o cualquier otra) impecable. Este proyecto clasifica automáticamente tus archivos en subcarpetas basadas en su extensión.

## Características
* **Automatización total:** Mueve archivos a carpetas como "Documentos", "Imágenes", "Videos", etc.
* **Gestión de errores:** Incluye manejo de `PermissionError` (ideal para evitar fallos si tienes un archivo abierto).
* **Auto-creación:** Si la carpeta de destino no existe, el script la crea por ti.

## Cómo empezar

### Requisitos previos
Solo necesitas tener instalado **Python 3.x**. No requiere librerías externas pesadas, ya que utiliza módulos nativos.

### Instalación
1. Clona este repositorio o descarga el archivo `.py`.
2. Asegúrate de que el script esté en la misma ruta o configura la variable `ruta` en el código.

### Configuración
En el archivo `organizador.py`, modifica la línea de la ruta según tu usuario:
```python
ruta = 'C:/Users/TU_USUARIO/Downloads'
