import math
import numpy as np
import matplotlib.pyplot as plt

n = 14
N = 100000
a = 0
b = 5

def f(x):
    return np.sqrt(29 - n * np.cos(x) ** 2)

x_test = np.linspace(a, b, 1000)
y_test = f(x_test)
f_max = np.max(y_test)
f_min = np.min(y_test)
S_rect = (b - a) * f_max

print(f"Минимальное значение функции: {f_min}")
print(f"Максимальное значение функции: {f_max}")
print(f"Площадь прямоугольника: {S_rect}")

x_points = np.random.uniform(a, b, N)
y_points = np.random.uniform(0, f_max, N)
condition = y_points <= f(x_points)
M = np.sum(condition)

print(f"Точек внутри фигуры (M): {M}")
print(f"Общее количество точек (N): {N}")

S_approx = (M / N) * S_rect
print(f"Приближенное значение интеграла: {S_approx}")

S_abs = math.sqrt((M / N * (1 - M / N)) / N) * S_rect
S_rel = S_abs / S_approx * 100
print(f"Абсолютная погрешность: {S_abs}")
print(f"Относительная погрешность: {S_rel}")

plt.scatter(x_points[:1000], y_points[:1000], color='blue', s=1, label='Случайные точки')
plt.scatter(x_points[:1000][condition[:1000]], y_points[:1000][condition[:1000]], color='red', s=1, label='Точки внутри')
plt.plot(x_test, y_test, color='green', linewidth=2, label=r'$y = \sqrt{29 - 14\cos^2x}$')
plt.axhline(y=f_max, color='purple', linewidth=2, linestyle='--', label=f'y = {f_max:.2f}')
plt.axvline(x=a, color='orange', linewidth=2, label=f'x = {a}')
plt.axvline(x=b, color='red', linewidth=2, label=f'x = {b}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Метод Монте-Карло для вычисления интеграла')
plt.legend()
plt.grid()
plt.show()