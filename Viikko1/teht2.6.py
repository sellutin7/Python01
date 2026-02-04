import random

# Kolmenumeroinen koodi (0-9)

koodi1 = ""
for _ in range(3):
    koodi1 += str(random.randint(0, 9))

# Nelinumeroinen koodi (1-6)

koodi2 = ""
for _ in range(4):
    koodi2 += str(random.randint(1, 6))

print("Kolmenumeroinen koodi:", koodi1)
print("Nelinumeroinen koodi:", koodi2)