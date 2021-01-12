import time
import functools

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def generate(self, count):
        current = self
        for _ in range(count):
            yield current
            current = current.next

class CupsGame:
    def __init__(self, data):
        self.min = min(data)
        self.max = max(data)
        self.cups = {value: Node(value) for value in data}

        def link(previous, cup):
            previous.next = cup
            return cup

        last_cup = functools.reduce(link, self.cups.values())
        self.current = last_cup.next = self.cups[data[0]]

    def run(self, iterations):
        start = time.time()
        for iteration in range(iterations):
            *pick_up, self.current.next = self.current.generate(5)

            index = self.current.value
            while self.cups[index] in pick_up:
                index -= 1
                if index < self.min:
                    index = self.max

            destination = self.cups[index]
            pick_up[-1].next = destination.next
            destination.next = pick_up[1]

            self.current = self.current.next

            if iteration % 1000000 == 0:
                print("{:.0f}% {:.0f}s".format(iteration/10000000*100, time.time()-start))

    def getCups(self, value, count):
        return [cup.value for cup in self.cups[value].next.generate(count)]

raw = "193467258"
# raw = "389125467"
data = list(map(int, raw)) + list(range(10, 1000001))

game = CupsGame(data)
game.run(10000000)
output = game.getCups(1, 2)
print(output[0] * output[1])
