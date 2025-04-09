import cv2
import os

def take_photo_and_save():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)  # El número 0 indica la cámara predeterminada
    
    if not cap.isOpened():
        print("Error al abrir la cámara")
        return
    
    # Capturar un fotograma
    ret, frame = cap.read()
    
    # Si la captura es exitosa, guardar la imagen en el escritorio
    if ret:
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        photo_path = os.path.join(desktop_path, 'captured_photo.jpg')
        cv2.imwrite(photo_path, frame)
        print(f"Fotografía guardada en: {photo_path}")
    else:
        print("Error al capturar la foto")
    
    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función para capturar la foto y guardarla
take_photo_and_save()
