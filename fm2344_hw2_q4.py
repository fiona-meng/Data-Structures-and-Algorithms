def e_approx(n):
    factorial = 1
    sum = 1
    for i in range(1, n+1):
        factorial *= i
        sum += 1 / factorial
    return sum


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)




