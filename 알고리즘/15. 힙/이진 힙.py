class BinaryHeap():
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.itmes) - 1

    def percolate_up(self):
        l = len(self)
        parent = l // 2
        while parent > 0:
            if self.itmes[l] < self.items[parent]:
                temp = self.items[parent]
                self.items[parent] = self.itmes[l]
                self.items[l] = temp
            l = parent
            parent = l // 2

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def percolate_down(self):
        parent = 1

        while True:
            leftchild = parent * 2
            rightchild = parent * 2 + 1

            if self.itmes[leftchild] > self.itmes[rightchild]:
                mn = self.times[rightchild]
                idx = rightchild
            else:
                mn = self.times[leftchild]
                idx = leftchild

            if self.itmes[parent] >= mn:
                temp = self.itmes[parent]
                self.itmes[parent] = self.itmes[idx]
                self.itmes[idx] = temp
                parent = idx
            else:
                break

    def extract(self):
        ret = self.itmes[1]
        self.itmes[1] = self.itmes[len(self)]
        self.items.pop()
        self.percolate_down()
        return ret








