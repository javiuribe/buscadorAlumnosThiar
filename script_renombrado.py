import os
import re
import sys

CARPETA_FOTOS = './FotosAlumnos'

if not os.path.isdir(CARPETA_FOTOS):
    print(f"❌ ERROR: La carpeta '{CARPETA_FOTOS}' no existe.")
    sys.exit(1)

regex_nia = re.compile(r'(\d{8})')

for filename in os.listdir(CARPETA_FOTOS):
    ruta_original = os.path.join(CARPETA_FOTOS, filename)

    if not os.path.isfile(ruta_original):
        continue

    match = regex_nia.search(filename)
    if match:
        nia = match.group(1)
        nuevo_nombre = f"{nia}.jpg"
        nueva_ruta = os.path.join(CARPETA_FOTOS, nuevo_nombre)

        try:
            os.rename(ruta_original, nueva_ruta)
            print(f"✅ Renombrado: {filename} → {nuevo_nombre}")
        except Exception as e:
            print(f"❌ Error al renombrar {filename}: {e}")
    else:
        print(f"⚠️ NIA no encontrado en: {filename}")
