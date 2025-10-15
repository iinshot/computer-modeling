def neyman_modified(n, r0, r1):
    if n < 2:
        return [r0, r1][:n]
    sequence = [r0, r1]
    for i in range(2, n):
        prev1 = sequence[i - 2]
        prev2 = sequence[i - 1]
        product = prev1 * prev2
        product_str = f"{product:.8f}"
        frac_part = product_str.split('.')[1]
        frac_part = frac_part.ljust(8, '0')
        middle_digits = frac_part[2:6]
        new_number = float("0." + middle_digits)
        sequence.append(new_number)
    return sequence

N = 10
R0 = 0.5836
R1 = 0.2176
print(neyman_modified(N, R0, R1))