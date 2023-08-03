def get_stars(n):
    fractal = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            fractal.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            fractal.append(n[i % len(n)] * 3)
    return fractal
 
 
stars = ["***", "* *", "***"]
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e += 1
 
for i in range(e):
    stars = get_stars(stars)
for i in stars:
    print(i)