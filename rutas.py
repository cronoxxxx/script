import os
import subprocess
import concurrent.futures

def convertir_video_a_y4m(ruta_video):
    carpeta, nombre = os.path.split(ruta_video)
    nombre_base, _ = os.path.splitext(nombre)
    ruta_y4m = os.path.join(carpeta, f"{nombre_base}.y4m")

    comando = [
        'ffmpeg',
        '-hide_banner',
        '-loglevel', 'error',
        '-i', ruta_video,
        '-pix_fmt', 'yuv420p',
        '-vf', 'scale=1280:720',
        '-c:v', 'rawvideo',
        '-q:v', '3',            # Calidad (1=mejor, 31=peor; ajusta según lo necesites)
        '-an',
        ruta_y4m
    ]

    print(f"Convirtiendo: {ruta_video} -> {ruta_y4m}")
    resultado = subprocess.run(comando, capture_output=True, text=True)
    if resultado.returncode != 0:
        print(f"Error en la conversión de {ruta_video}:")
        print(resultado.stderr)
    else:   
        print(f"Conversión completada: {ruta_y4m}")

if __name__ == '__main__':
    with open('rutas.txt', 'r', encoding='utf-8') as f:
        videos = [line.strip() for line in f if line.strip()]

    # Ejecuta todas las conversiones en paralelo
    with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
        executor.map(convertir_video_a_y4m, videos)
