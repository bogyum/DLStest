from gateClass import gate

X = [[0,0], [0,1], [1,0], [1,1]]

### AND gate ###

ANDgate = gate(-0.7, 0.5, 0.5)
ANDgate.show_weight()

def AND(x1, x2):
    return ANDgate.op(x1, x2)

print("AND Result: ")

for xi in X:
    print(xi, AND(xi[0], xi[1]))

### OR gate ###
ORgate = gate(0.0, 0.5, 0.5)
ORgate.show_weight()

def OR(x1, x2):
    return ORgate.op(x1, x2)

print("OR Result: ")
for xi in X:
    print(xi, OR(xi[0], xi[1]))

### NAND gate ###
NANDgate = gate(-0.7, 0.5, 0.5)
NANDgate.show_weight()

def NAND(x1, x2):
    result = NANDgate.op(x1, x2)
    if result == 0:
        return 1
    else:
        return 0

print("NAND Result: ")
for xi in X:
    print(xi, NAND(xi[0], xi[1]))

### XOR gate ###
def XOR(x1, x2):
    y1 = NAND(x1, x2)
    y2 = OR(x1, x2)
    return AND(y1, y2)

print("XOR Result: ")
for xi in X :
    print(xi, XOR(xi[0], xi[1]))


### half adder ###
print("Half adder: ")
def half_adder(x1, x2):
    s = XOR(x1, x2)
    c = AND(x1, x2)
    return (s, c)


for AB in [(0,0), (1,0), (0,1), (1,1)]:
    S, C = half_adder(AB[0], AB[1])
    print(str(AB) + " -> " + str(S) + ", " + str(C))

