class Node(object):
    def __init__(self, conteined_object, next = None):
        self.conteined_object = conteined_object
        self.next = next

class MyQueue(object):
    def __init__(self, head = None):
        self.head = Node(conteined_object = head, next = None)
        self.end_of_queue = self.head

    def add(self, new):
        if self.head.conteined_object is None:
            self.head.conteined_object = new
        else:
            self.end_of_queue.next = Node(new, None)
            self.end_of_queue = self.end_of_queue.next

    def remove(self):
        if self.head == self.end_of_queue:
            self.head = Node()
            self.end_of_queue = self.head
        else:
            self.head = self.head.next

    def clear(self):
        self.__init__()

    def turn_into(self):
        array = []
        element = self.head
        while element.next is not None:
            array.append(element.conteined_object)
            element = element.next
        if element.conteined_object is not None:
            array.append(element.conteined_object)
        return array

class Country(object):
    def __init__(self, name: str, capital: str, population: int):
        self.name = name
        self.capital = capital
        self.population = population

    def __str__(self):
        return f"Country - {self.name}; Capital - {self.capital}; Population - {self.population}"

if __name__ == "__main__":
    int_array = [2, 9, 4, 11, 6, 13, 8]
    Country_array = [
    Country("USA", "Washington", 328200000),
    Country("Russia", "Moscow", 144500000),
    Country("Ukraine", "Kiev", 41980000)
    ]
    int_queue = MyQueue()
    Country_queue = MyQueue()
    for i in int_array:
        int_queue.add(i)

    for i in Country_array:
        Country_queue.add(i)

    print(int_queue.turn_into())
    print([str(c) for c in Country_queue.turn_into()])