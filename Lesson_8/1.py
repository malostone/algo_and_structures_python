"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter, deque

def haffmanTree(string):
    counter = Counter(string)
    elementsSorted= deque(sorted(counter.items(), key=lambda item: item[1]))
    
    if len(elementsSorted) != 1:
        while len(elementsSorted) > 1:
            frequency  = elementsSorted[0][1] + elementsSorted[1][1]
            combined = {0: elementsSorted.popleft()[0],
                    1: elementsSorted.popleft()[0]}
            for i, _count in enumerate(elementsSorted):
                if frequency > _count[1]:
                    continue
                else:
                    elementsSorted.insert(i, (combined, frequency))
                    break
            else:

                elementsSorted.append((combined, frequency))
    else:
        frequency = elementsSorted[0][1]
        combined = {0: elementsSorted.popleft()[0], 1: None}
        elementsSorted.append((combined, frequency))
    return elementsSorted[0][0]


table = dict()


def haffmanСode(wood, way=''):
    if not isinstance(wood, dict):
        table[wood] = way
    else:
        haffmanСode(wood[0], way=f'{way}0')
        haffmanСode(wood[1], way=f'{way}1')

string = "Good news, everyone!"

haffmanСode(haffmanTree(string))

for i in string:
    print(table[i], end=' ')
print()
