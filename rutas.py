import os
import subprocess

def convertir_video_a_y4m_640x480(ruta_video):
    carpeta, nombre = os.path.split(ruta_video)
    nombre_base, _ = os.path.splitext(nombre)
    ruta_y4m = os.path.join(carpeta, f"{nombre_base}_640x480.y4m")

    comando = [
        'ffmpeg',
        '-i', ruta_video,
        '-vf', 'scale=1280:720',  # Escala a 640x480 píxeles
        '-pix_fmt', 'yuv420p',
        ruta_y4m
    ]

    print(f"Convirtiendo: {ruta_video} -> {ruta_y4m}")
    resultado = subprocess.run(comando, capture_output=True, text=True)
    if resultado.returncode != 0:
        print(f"Error en la conversión de {ruta_video}:")
        print(resultado.stderr)
    else:
        print(f"Conversión completada: {ruta_y4m}")

# Lee las rutas desde el archivo de texto
with open('rutas.txt', 'r', encoding='utf-8') as f:
    videos = [line.strip() for line in f if line.strip()]

for video in videos:
    convertir_video_a_y4m_640x480(video)
