import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import os
from train_mnist import SimpleNet

# Vamos a usar torchvision para "leer" o predecir los números escritos a mano en el directorio raíz  data\img_6.jpg, data\img_65.jpg, data\img_83.jpg
# Carga del modelo
model = SimpleNet()
model.load_state_dict(torch.load('modelo_mnist.pth'))
model.eval() # Importante para decirle al modelo que ahora está en modo de evaluación
images = []
for root, dirs, files in os.walk('mnsit'):
    for file in files:
        base, extension = os.path.splitext(file)
        if (extension.lower() == '.jpg'):
            full_path = os.path.join(root, file)
            images.append(full_path)

def predict(image):
    # Definimos las transformaciones que se deben aplicar a la imagen para que coincida con el formato MNIST
    transformations = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # Aplicamos las transformaciones a la imagen
    img_transformed = transformations(image)

    # Convertimos la imagen para que tenga una dimensión de lote (que PyTorch espera)
    img_batch = img_transformed.unsqueeze(0)  # Agrega un batch dimension en la posición 0

    # Verificamos las dimensiones de la imagen resultante
    print(img_batch.shape)

    # Hacer la predicción
    with torch.no_grad():  # No necesitamos seguir el rastro de los gradientes
        outputs = model(img_batch)
        _, predicted = torch.max(outputs, 1)

    # El resultado 'predicted' es el índice del dígito que el modelo predice
    print(f'El modelo predice que el dígito es: {predicted.item()}')

for image_path in images:
    image = Image.open(image_path)
    predict(image)