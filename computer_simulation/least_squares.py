import math
import numpy as np
import matplotlib.pyplot as plt

def gauss(matrix, b):
    matrix = np.array(matrix, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    for i in range(n):
        max_row_index = np.argmax(np.abs(matrix[i:, i])) + i
        matrix[[i, max_row_index]] = matrix[[max_row_index, i]]
        b[i], b[max_row_index] = b[max_row_index], b[i]
        for j in range(i + 1, n):
            index = matrix[j][i] / matrix[i][i]
            matrix[j] = matrix[j] - index * matrix[i]
            b[j] = b[j] - index * b[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(matrix[i], x)) / matrix[i][i]
    return x

x = [5, 15, 25, 35, 45,55]
x_smooth = np.linspace(min(x), max(x), 500)
y = [2.2, 2.4, 2.6, 2.7, 2.8, 2.9]
num = len(x)


# Линейная функция
result_1 = gauss([
    [sum(xi ** 2 for xi in x), sum(x)],
    [sum(x), num]
], [sum(xi * yi for [xi, yi] in zip(x, y)), sum(y)])


# Степенная функция
result_2 = gauss([
    [sum(math.log(xi) ** 2 for xi in x), sum(math.log(xi) for xi in x)],
    [sum(math.log(xi) for xi in x), num]
], [sum(math.log(xi) * math.log(yi) for [xi, yi] in zip(x, y)), sum(math.log(yi) for yi in y)])
result_2 = [result_2[0], math.exp(result_2[1])]


# Показательная функция
result_3 = gauss([
    [sum(xi ** 2 for xi in x), sum(x)],
    [sum(x), num]
], [sum(xi * math.log(yi) for [xi, yi] in zip(x, y)), sum(math.log(yi) for yi in y)])
result_3 = [result_3[0], math.exp(result_3[1])]


# Квадратичная функция
result_4 = gauss([
    [sum(xi ** 4 for xi in x), sum(xi ** 3 for xi in x), sum(xi ** 2 for xi in x)],
    [sum(xi ** 3 for xi in x), sum(xi ** 2 for xi in x), sum(x)],
    [sum(xi ** 2 for xi in x), sum(x), num]
], [sum(xi ** 2 * yi for [xi, yi] in zip(x, y)), sum(xi * yi for [xi, yi] in zip(x, y)), sum(y)])


def calculate_error(y_actual, y_predicted):
    return sum((y_act - y_pred) ** 2 for y_act, y_pred in zip(y_actual, y_predicted))

y_pred_1 = [result_1[0] * xi + result_1[1] for xi in x]
y_pred_2 = [result_2[1] * xi ** result_2[0] for xi in x]
y_pred_3 = [result_3[1] * math.exp(xi * result_3[0]) for xi in x]
y_pred_4 = [result_4[0] * xi ** 2 + result_4[1] * xi + result_4[2] for xi in x]

error_1 = calculate_error(y, y_pred_1)
error_2 = calculate_error(y, y_pred_2)
error_3 = calculate_error(y, y_pred_3)
error_4 = calculate_error(y, y_pred_4)

print(f'a_1 = {result_1[0]}, b_1 = {result_1[1]}')
print(f'a_2 = {result_2[0]}, b_2 = {result_2[1]}')
print(f'a_3 = {result_3[0]}, b_3 = {result_3[1]}')
print(f'a_4 = {result_4[0]}, b_4 = {result_4[1]}, c_4 = {result_4[2]}')

print("Суммарные квадратичные погрешности:")
print(f'Линейная функция: {error_1}')
print(f'Степенная функция: {error_2}')
print(f'Показательная функция: {error_3}')
print(f'Квадратичная функция: {error_4}')


y_new_1 = [result_1[0] * xi + result_1[1] for xi in x_smooth]
y_new_2 = [result_2[1] * xi ** result_2[0] for xi in x_smooth]
y_new_3 = [result_3[1] * math.exp(xi * result_3[0]) for xi in x_smooth]
y_new_4 = [result_4[0] * xi ** 2 + result_4[1] * xi + result_4[2] for xi in x_smooth]
plt.plot(x, y, label='Экспериментальные точки', color='black', marker='o', ls='none')
plt.plot(x_smooth, y_new_1, label='Линейная', color='blue')
plt.plot(x_smooth, y_new_2, label='Степенная', color='red')
plt.plot(x_smooth, y_new_3, label='Показательная', color='green')
plt.plot(x_smooth, y_new_4, label='Квадратичная', color='yellow')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()