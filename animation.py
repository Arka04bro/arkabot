from vpython import *

# Создаем сцену
scene1 = canvas(title='Solar System with Super Fast Satellite', width=800, height=500, background=color.black)

# Устанавливаем камеру сверху
scene1.camera.pos = vector(0, 10, 0)  # Камера сверху на высоте 10 единиц
scene1.camera.axis = vector(0, -1, 0)  # Камера смотрит вниз на ось Y

# Создаем Солнце
sun = sphere(pos=vector(0, 0, 0), radius=1.5, color=color.yellow)

# Создаем планеты с индивидуальными орбитами, размерами и следами
mercury = sphere(pos=vector(2.5, 0, 0), radius=0.1, color=color.gray(0.5), make_trail=True)
venus = sphere(pos=vector(4, 0, 0), radius=0.15, color=color.orange, make_trail=True)
earth = sphere(pos=vector(5.5, 0, 0), radius=0.2, color=color.blue, make_trail=True)
mars = sphere(pos=vector(7, 0, 0), radius=0.15, color=color.red, make_trail=True)

# Создаем спутник, вращающийся вокруг Солнца, ближе к Солнцу
satellite = sphere(pos=vector(1.8, 0, 0), radius=0.05, color=color.white, make_trail=True)

# Угловые скорости для каждой планеты
angular_velocity_mercury = 0.08  # Меркурий
angular_velocity_venus = 0.03  # Венера
angular_velocity_earth = 0.02  # Земля
angular_velocity_mars = 0.015  # Марс
angular_velocity_satellite = 2.0  # Увеличенная скорость спутника

# Время для анимации
time = 0

# Основной цикл анимации
while True:
    rate(100)  # Ограничаем скорость обновления анимации (100 кадров в секунду)

    # Обновляем позиции планет по орбитам вокруг Солнца
    mercury.pos = vector(2.5 * cos(angular_velocity_mercury * time), 0, 2.5 * sin(angular_velocity_mercury * time))
    venus.pos = vector(4 * cos(angular_velocity_venus * time), 0, 4 * sin(angular_velocity_venus * time))
    earth.pos = vector(5.5 * cos(angular_velocity_earth * time), 0, 5.5 * sin(angular_velocity_earth * time))
    mars.pos = vector(7 * cos(angular_velocity_mars * time), 0, 7 * sin(angular_velocity_mars * time))

    # Обновляем позицию спутника по орбите вокруг Солнца с увеличенной угловой скоростью
    satellite.pos = vector(1.8 * cos(angular_velocity_satellite * time), 0, 1.8 * sin(angular_velocity_satellite * time))

    # Увеличиваем время для плавного движения
    time += 0.01
