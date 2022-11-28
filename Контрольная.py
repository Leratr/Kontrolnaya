class GoodIfrit_7():

    def __init__(self, height, name, kind):
        self.height = height
        self.name = name
        self.kind = kind

    def change_goodness(self, value):
        self.value = value

    def __add__(self):
        if self.kind + self.value < 0:
            gi.kind = 0
        number = int(input())
        return self.kind + self.value and self.height + number

    def __str__(self):
        return self.name, self.height, self.kind

gi = GoodIfrit_7(2, "GoodIfrit", 100)
gi.change_goodness(20)
print(gi.__add__())
print(gi.__str__())
gi1 = []
gi1.append

