#Currently recursion will be done


def fib(n: int):
    li = [0, 1]
    for i in range(2, n):
        li.append(li[i - 1] + li[i - 2])
    return li[n - 1]

if __name__ == "__main__":
    print(fib(8))




"""










"""