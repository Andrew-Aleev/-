class Somelist:
    def __init__(self, *args):
        self.a = list(args)
        if args and isinstance(self.a[0][1], int):
            self.a = sorted(self.a, key=lambda x: x[1], reverse=True)

    def values(self):
        return self.a

    def checked_values(self):
        k = []
        for i in self.a:
            if True in i:
                if str(i[1]) != '1':
                    k.append(i)
        return k

    def rest_values(self):
        k = []
        for i in self.a:
            if False in i:
                k.append(i)
        return k


class ShoppingList:
    def __init__(self, *args):
        self.a = list(args)

    def values(self):
        return self.a

    def checked_values(self):
        k = []
        for i in self.a:
            if True in i:
                k.append(i)
        return k

    def rest_values(self):
        k = []
        for i in self.a:
            if False in i:
                k.append(i)
        return k

    def append(self, k):
        self.a.append((k, False))
        return self.a

    def check(self, k):
        for i in range(len(self.a)):
            if self.a[i][0] == k:
                self.a[i] = (self.a[i][0], True)


class Route(Somelist):
    def append(self, *args):
        k = list(args)
        if not self.a or (int(k[1].split(':')[0]) > int(self.a[-1][1].split(':')[0])
                          or (int(k[1].split(':')[0]) == int(self.a[-1][1].split(':')[0])
                              and int(k[1].split(':')[1]) > int(self.a[-1][1].split(':')[1]))):
            self.a.append((k[0], k[1], False))

    def check(self, k):
        for i in range(len(self.a)):
            if self.a[i][0] == k:
                self.a[i] = (self.a[i][0], self.a[i][1], True)


class TODOList(Somelist):
    def append(self, *args):
        k = tuple(args)
        self.a.append((k[0], k[1], False))
        self.a = sorted(self.a, key=lambda x: x[1], reverse=True)

    def check(self, k):
        for i in range(len(self.a)):
            if self.a[i][0] == k:
                self.a[i] = (self.a[i][0], self.a[i][1], True)

path = Route(("Stratford", "12:15", False),
             ("Hackney Central", "12:24", False),
             ("Dalston Kingsland", "12:36", False))
path.append("Camden Road", "12:45")
path.append("Richmond", "11:52")
print(*path.values(), sep="\n")
print()
path.check("Stratford")
path.check("Hackney Central")
print(*[x[0] for x in path.rest_values()], sep="\n")

