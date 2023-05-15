class Operator:
    def __init__(self, l, r):
        self.l = l
        self.r = r
def main():
    op = []
    pr = []
    n = int(input("Enter the number of values: "))
    for i in range(n):
        left = input("Left: ")
        right = input("Right: ")
        op.append(Operator(left, right))
    print("Intermediate Code:")
    for i in range(n):
        print(f"{op[i].l} = {op[i].r}")
    z = 0
    for i in range(n - 1):
        temp = op[i].l
        for j in range(n):
            if temp in op[j].r:
                pr.append(Operator(op[i].l, op[i].r))
                z += 1
    pr.append(Operator(op[n - 1].l, op[n - 1].r))
    z += 1
    print("\nAfter Dead Code Elimination:")
    for k in range(z):
        print(f"{pr[k].l} = {pr[k].r}")
    for m in range(z):
        tem = pr[m].r
        for j in range(m + 1, z):
            if pr[j].r in tem:
                t = pr[j].l
                pr[j].l = pr[m].l
                for i in range(z):
                    if t in pr[i].r:
                        a = pr[i].r.index(t)
                        pr[i].r = pr[i].r[:a] + pr[m].l + pr[i].r[a+1:]
    print("\nEliminate Common Expression:")
    for i in range(z):
        print(f"{pr[i].l} = {pr[i].r}")
    for i in range(z):
        for j in range(i + 1, z):
            if pr[i].l == pr[j].l and pr[i].r == pr[j].r:
                pr[i].l = ''
    print("\nOptimized Code:")
    for i in range(z):
        if pr[i].l != '':
            print(f"{pr[i].l} = {pr[i].r}")
if __name__ == '__main__':
    main()
