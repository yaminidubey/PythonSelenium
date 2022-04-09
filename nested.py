def B():
    def A(x):
        return x+1

    print(A)
    return A


c = B()
print(c)
print(c(4))