>>> random.seed(100)
>>> actual_value, rounded_value = 100, 100

>>> for _ in range(1000000):
...     randn = random.uniform(-0.05, 0.05)
...     actual_value = actual_value + randn
...     rounded_value = round(rounded_value + randn, 3)
...

>>> actual_value
96.45273913513529

>>> rounded_value
96.258
