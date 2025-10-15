import math
import numpy as np
import matplotlib.pyplot as plt

n = 14
N = 100000

def f1(x):
    return (10 * x) / n

def f2(x):
    return (-5 / 3) * x + (160 / 3)

x_intersect = 22.4
y_intersect = f1(x_intersect)

print(f"Графики пересекаются в точке: ({x_intersect}, {y_intersect})")

x_min, x_max = 0, x_intersect
y_min, y_max = 0, f2(0)

a = x_max - x_min
b = y_max - y_min
S_rect = a * b
print(f"Стороны прямоугольника: {a}, {b}")
print(f"Площадь прямоугольника: {S_rect}")

x_points = np.random.uniform(x_min, x_max, N)
y_points = np.random.uniform(y_min, y_max, N)
condition = (y_points >= f1(x_points)) & (y_points <= f2(x_points))

M = np.sum(condition)
print(f"Точек внутри фигуры (M): {M}")
print(f"Общее количество точек (N): {N}")

S_approx = (M / N) * S_rect
print(f"Приближенная площадь фигуры: {S_approx}")

S_abs = math.sqrt((M / N * (1 - M / N)) / N) * S_rect
S_rel = S_abs / S_approx * 100
print(f"Абсолютная погрешность: {S_abs}")
print(f"Относительная погрешность: {S_rel}")

plt.scatter(x_points[:1000], y_points[:1000], color='blue', s=1, label='Случайные точки')
plt.scatter(x_points[:1000][condition[:1000]], y_points[:1000][condition[:1000]], color='red', s=1, label='Точки внутри')
x_vals = np.linspace(x_min, x_max, 100)
plt.plot(x_vals, f1(x_vals), color='green', linewidth=2, label=r'$y = \frac{5x}{7}$')
plt.plot(x_vals, f2(x_vals), color='purple', linewidth=2, label=r'$y = \frac{-5x}{3} + \frac{160}{3}$')
plt.axvline(x=0, color='orange', linewidth=2, label='x = 0')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Метод Монте-Карло для вычисления площади треугольника')
plt.legend()
plt.grid()
plt.show()