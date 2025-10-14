def lemar_modified(a, m, x0, n):
    sequence = [x0]
    seen = {x0: 0}
    repeat_position = None
    for i in range(1, n):
        next_val = (a * x0) % m
        if next_val in seen and repeat_position is None:
            repeat_position = i
        seen[next_val] = i
        sequence.append(next_val)
        x0 = next_val
        if repeat_position is not None and i >= repeat_position + 5:
            break
    return sequence, repeat_position

a = 11
m = 127
X0 = 15
N = 100
sequence, repeat_pos = lemar_modified(a, m, X0, N)
print(f"Длина последовательности до первого повторения: {repeat_pos}")
print(f"Сгенерировано чисел: {len(sequence)}")
for i in range(0, len(sequence)):
    print(f"X{i} = {sequence[i]}")