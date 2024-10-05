import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
import numpy as np
import matplotlib.pyplot as plt

# Параметры
IMG_HEIGHT = 256
IMG_WIDTH = 256
BATCH_SIZE = 32
EPOCHS = 10
LEARNING_RATE = 0.001

# Генератор данных для аугментации изображений
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# Загрузка обучающих данных (укажи путь к данным)
train_data_dir = "D:/sunspot/dataset"
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='binary')

# Создание модели
model = Sequential([
    Input(shape=(IMG_HEIGHT, IMG_WIDTH, 3)),  # Явно задаем входной слой
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    Flatten(),
    
    Dense(512, activation='relu'),
    Dropout(0.5),
    
    Dense(1, activation='sigmoid')  # выходной слой для бинарной классификации
])

# Компиляция модели
model.compile(optimizer=Adam(learning_rate=LEARNING_RATE),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Тренировка модели
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // BATCH_SIZE,
    epochs=EPOCHS)

# Сохранение обученной модели
model.save('sunspot_detector.h5')

# Функция для загрузки и предобработки изображения
def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = image.img_to_array(img)  # Преобразуем в массив
    img_array = np.expand_dims(img_array, axis=0)  # Добавляем размерности для модели
    img_array /= 255.0  # Нормализуем изображение (0-1)
    return img_array

# Функция для предсказания
def predict_sunspot(img_path):
    img = load_and_preprocess_image(img_path)
    
    prediction = model.predict(img)
    
    if prediction[0][0] > 0.5:
        result = "Солнечные пятна обнаружены"
    else:
        result = "Солнечные пятна не обнаружены"
    
    # Отображаем изображение и результат предсказания
    plt.imshow(image.load_img(img_path))
    plt.axis('off')
    plt.title(result)
    plt.show()

    return result

# Пример использования для предсказания
img_path ="D:\sunspot\images (4).jpeg"
result = predict_sunspot(img_path)
print(result)
print(f"Final training accuracy: {history.history['accuracy'][-1]}")
