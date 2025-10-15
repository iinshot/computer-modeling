import math
import numpy as np
import matplotlib.pyplot as plt

n = 14
N = 100000
A = n + 10
B = n - 10
a = np.sqrt(A)
b = np.sqrt(B)
x_min, x_max = -a, a
y_min, y_max = -b, b
S_rect = (x_max - x_min) * (y_max - y_min)

print(f"Полуоси эллипса: a = {a}, b = {b}")
print(f"Площадь прямоугольника: {S_rect}")

x_points = np.random.uniform(x_min, x_max, N)
y_points = np.random.uniform(y_min, y_max, N)
rho_points = np.sqrt(x_points ** 2 + y_points ** 2)
theta_points = np.arctan2(y_points, x_points)
condition = rho_points ** 2 <= A * np.cos(theta_points) ** 2 + B * np.sin(theta_points) ** 2
M = np.sum(condition)

print(f"Точек внутри фигуры (M): {M}")
print(f"Общее количество точек (N): {N}")

S_approx = (M / N) * S_rect
print(f"Приближенное значение площади фигуры: {S_approx}")

S_abs = math.sqrt((M / N * (1 - M / N)) / N) * S_rect
S_rel = S_abs / S_approx * 100
print(f"Абсолютная погрешность: {S_abs}")
print(f"Относительная погрешность: {S_rel}")

theta_plot = np.linspace(0, 2 * np.pi, 1000)
rho_plot = np.sqrt(A * np.cos(theta_plot) ** 2 + B * np.sin(theta_plot) ** 2)
x_plot = rho_plot * np.cos(theta_plot)
y_plot = rho_plot * np.sin(theta_plot)

plt.plot(x_plot, y_plot, color='green', linewidth=2, label=rf'${A}cos^2\theta + {B}sin^2\theta = \rho^2$')
plt.axhline(y=y_min, color='purple', linewidth=1, linestyle='--')
plt.axhline(y=y_max, color='purple', linewidth=1, linestyle='--', label='Границы прямоугольника')
plt.axvline(x=x_min, color='purple', linewidth=1, linestyle='--')
plt.axvline(x=x_max, color='purple', linewidth=1, linestyle='--')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)
plt.scatter(x_points[:10000], y_points[:10000], color='blue', s=1, label='Случайные точки')
plt.scatter(x_points[:10000][condition[:10000]], y_points[:10000][condition[:10000]], color='red', s=1, label='Точки внутри')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Метод Монте-Карло для вычисления площади фигуры, \n ограниченной замкнутой линией')
plt.legend()
plt.grid()
plt.show()