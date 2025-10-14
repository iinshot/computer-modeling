def lemar_method(n, r0, g):
    sequence = [r0]
    for i in range(1, n):
        product = g * r0
        new_number = product - int(product)
        sequence.append(new_number)
        r0 = new_number
    return sequence

N = 10
R0 = 0.585
g = 927
print(lemar_method(N, R0, g))