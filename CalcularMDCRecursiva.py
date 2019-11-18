digito1 = int(input())
digito2 = int(input())
def mdc(a, b):
    return a if not b else mdc(b, a % b)

print(mdc(digito1, digito2))