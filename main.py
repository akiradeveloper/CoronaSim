P = 0.000000000019
N = 8000000000
D = 250
rem = N - 1
x = [1] * 14
for t in range(0,D):
    tot = sum(x)
    new = int(tot * P * rem)
    rem = max(rem-new,0)
    y = [0] * 14
    for i in range(0,13):
        y[i+1] = x[i]
    y[0] = new
    x = y
    cum = N-rem
    print("{} {}".format(t+1, cum))