import math
import numpy as np
import matplotlib.pyplot as plt

R = 14
N = 100000
S_rect = 4 * R ** 2

print(f"Площадь прямоугольника: {S_rect}")

x_points = np.random.uniform(-R, R, N)
y_points = np.random.uniform(-R, R, N)
condition = x_points ** 2 + y_points ** 2 <= R ** 2
M = np.sum(condition)

print(f"Точек внутри фигуры (M): {M}")
print(f"Общее количество точек (N): {N}")

S_approx = 4 * (M / N)
print(f"Приближенное значение числа pi: {S_approx}")

S_abs = math.sqrt((M / N * (1 - M / N)) / N) * 4
S_rel = S_abs / S_approx * 100
print(f"Абсолютная погрешность: {S_abs}")
print(f"Относительная погрешность: {S_rel}")

plt.scatter(x_points[:10000], y_points[:10000], color='blue', s=1, label='Случайные точки')
plt.scatter(x_points[:10000][condition[:10000]], y_points[:10000][condition[:10000]], color='red', s=1, label='Точки внутри')

theta = np.linspace(0, 2 * np.pi, 100)
x_circle = R * np.cos(theta)
y_circle = R * np.sin(theta)
plt.plot(x_circle, y_circle, color='green', linewidth=2, label=f'Окружность R = {R}')
plt.axhline(y=-R, color='purple', linewidth=2, linestyle='--')
plt.axhline(y=R, color='purple', linewidth=2, linestyle='--', label=f'Квадрат [{-R},{R}]×[{-R},{R}]')
plt.axvline(x=-R, color='purple', linewidth=2, linestyle='--')
plt.axvline(x=R, color='purple', linewidth=2, linestyle='--')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Метод Монте-Карло для вычисления числа pi')
plt.legend()
plt.grid()
plt.show()