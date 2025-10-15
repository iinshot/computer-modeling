def neyman_method(n, r0):
    sequence = [r0]
    for i in range(1, n):
        square = r0 ** 2
        square_str = f"{square:.6f}"
        frac_part = square_str.split('.')[1]
        frac_part = frac_part.ljust(6, '0')
        middle_digits = frac_part[1:4]
        new_number = float("0." + middle_digits)
        sequence.append(new_number)
        r0 = new_number
    return sequence

N = 10
R0 = 0.583
print(neyman_method(N, R0))