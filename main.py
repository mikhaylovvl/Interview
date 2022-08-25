class Stack:
    def __init__(self, stack):
        self.stack = list(stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, el):
        self.stack.append(el)
        print(self.stack)

    def pop(self):
        self.stack.pop()
        print(self.stack)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def balance_parentheses(self):
        temp_stack = []
        for el in self.stack:
            if el in "([{":
                temp_stack.append(el)
                continue
            if el in ")]}":
                if temp_stack[-1] == "(" and el == ")":
                    temp_stack.pop()
                    continue
                elif temp_stack[-1] == "[" and el == "]":
                    temp_stack.pop()
                    continue
                elif temp_stack[-1] == "{" and el == "}":
                    temp_stack.pop()
                    continue
                else:
                    temp_stack.append(el)

        if len(temp_stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    # задание 1
    a = input("Введите строку: ").strip()
    stack_1 = Stack(a)

    # isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    print(stack_1.isEmpty())

    # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    stack_1.push("e")

    # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    stack_1.pop()

    # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    print(stack_1.peek())

    # size - возвращает количество элементов в стеке.
    print(stack_1.size())

    # задание 2
    b = "(((([{}]))))"
    stack_2 = Stack(b)
    print(f"Баланс скобок --> {stack_2.balance_parentheses()}")

    c = "{{[(])]}}"
    stack_3 = Stack(c)
    print(f"Баланс скобок --> {stack_3.balance_parentheses()}")