# #Exercise 1 
# my_list = [5,1,23,64,7,5,13,74,134,46]
# # my_list = ["One", "piece", "per", "time"]
# my_iter = iter(my_list)

# for _ in range(len(my_list)):
#     print(next(my_iter))







#Exercise 3




# class MyIter():
#     def __init__(self, my_list:list):
#         self.__mylist = my_list
#         self.__start = len(my_list)

#     def __iter__(self):
#         self.__index = self.__start
#         return self

#     def __next__(self):
#         if self.__index == 0:
#             raise StopIteration
#         result = self.__mylist[self.__index-1]
#         self.__index -= 1
#         return result


# my_list = [23,5,"gheh","31","ggg"]
# list = []
# for i in MyIter(my_list):
#     print(i)
#     list.append(i)
# print(list)







#Exersice 2 







# """
# Пример реализации списка с итератором
# """


# class MyList(object):
#     """Класс списка"""

#     class _ListNode(object):
#         """Внутренний класс элемента списка"""

#         # По умолчанию атрибуты-данные хранятся в словаре __dict__.
#         # Если возможность динамически добавлять новые атрибуты
#         # не требуется, можно заранее их описать, что более
#         # эффективно с точки зрения памяти и быстродействия, что
#         # особенно важно, когда создаётся множество экземляров
#         # данного класса.
#         __slots__ = ('value', 'prev', 'next')

#         def __init__(self, value, prev=None, next=None):
#             self.value = value
#             self.prev = prev
#             self.next = next

#         def __repr__(self):
#             return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

#     class _Iterator(object):
#         """Внутренний класс итератора"""

#         def __init__(self, list_instance):
#             self._list_instance = list_instance
#             self._next_node = list_instance._head

#         def __iter__(self):
#             return self

#         def __next__(self):
#             if self._next_node is None:
#                 raise StopIteration

#             value = self._next_node.value
#             self._next_node = self._next_node.next

#             return value

#     def __init__(self, iterable=None):
#         # Длина списка
#         self._length = 0
#         # Первый элемент списка
#         self._head = None
#         # Последний элемент списка
#         self._tail = None

#         # Добавление всех переданных элементов
#         if iterable is not None:
#             for element in iterable:
#                 self.append(element)

#     def append(self, element):
#         """Добавление элемента в конец списка"""

#         # Создание элемента списка
#         node = MyList._ListNode(element)

#         if self._tail is None:
#             # Список пока пустой
#             self._head = self._tail = node
#         else:
#             # Добавление элемента
#             self._tail.next = node
#             node.prev = self._tail
#             self._tail = node

#         self._length += 1

#     def __len__(self):
#         return self._length

#     def __repr__(self):
#         # Метод join класса str принимает последовательность строк
#         # и возвращает строку, в которой все элементы этой
#         # последовательности соединены изначальной строкой.
#         # Функция map применяет заданную функцию ко всем элементам последовательности.
#         return 'MyList([{}])'.format(', '.join(map(repr, self)))

#     def __getitem__(self, index):
#         if not 0 <= index < len(self):
#             raise IndexError('list index out of range')

#         node = self._head
#         for _ in range(index):
#             node = node.next

#         return node.value

#     def __iter__(self):
#         return MyList._Iterator(self)
    
#     def clear(self):
#         '''видалення'''
#         self._head = None
#         self._tail = None
#         self._length = 0

#     def insert(self, element, index:int):
#         '''Додавання елементу в задане місце'''
#         # node = MyList._ListNode(element)
#         if 1 < index <= (self._length) :
#             index -= 1
#             node_prev = self._head
#             node_next = self._head
#             for _ in range(index-1):
#                 node_prev = node_prev.next

#             for _ in range(index):
#                 node_next = node_next.next

#             node = MyList._ListNode(element,node_prev,node_next)
#             node_next.prev = node
#             node_prev.next = node
#             self._length += 1

#         elif index == 1 and not(self._tail  is None):
#             node = MyList._ListNode(element,None,self._head)
#             self._head.prev = node
#             self._head = node
#             self._length +=1

#         elif index == self._length + 1 and not(self._tail  is None):
#             node = MyList._ListNode(element,self._tail,None)
#             self._tail.next = node
#             self._tail = node
#             self._length += 1

#         elif index == 1 and self._tail  is None:
#             node = MyList._ListNode(element,None,None)
#             self._tail = self._head = node    
#             self._length += 1      





#     # def pop(self):
#     #     '''видалення з кінца'''
#     #     self._tail.prev.next = None
#     #     result = self._tail
#     #     self.tail = self._tail.prev
#     #     self._length -= 1
#     #     return result.value


#     def pop(self, index=None):
#         if(index == None):
#             '''видалення з кінца'''
#             self._tail.prev.next = None
#             result = self._tail
#             self.tail = self._tail.prev
#             self._length -= 1
#             return result.value
    
#         '''видалення з заданого місця'''
#         node = self._head
#         for _ in range(index - 1):
#             node = node.next
            
#         if(node == self._head):
#             node.next.prev = None
#             result = node
#             self._head = node.next 
#             self._length -= 1
        
#         elif(node == self._tail):
#             node.prev.next = None
#             result = node
#             self._tail = node.prev
#             self._length -= 1
#         elif 1 < index <= self._length:
#             node.prev.next = node.next
#             node.next.prev = node.prev
#             self._length -= 1



# def main():
#     # Создание списка
#     my_list = MyList([2,3,5,6])
#     # my_list.append('4')
#     # my_list.clear()
#     my_list.insert("haha",2)
#     print(my_list)
#     my_list.pop(2)
#     print(my_list)

#     # Вывод длины списка
#     print(len(my_list))

#     # Вывод самого списка
#     print(my_list)

#     print()

#     # Обход списка
#     for element in my_list:
#         print(element)

#     print()

#     # Повторный обход списка
#     for element in my_list:
#         print(element)


# if __name__ == '__main__':
#     main()
        






#exercise 4




# class MyIter:
#     def __init__(self, mydict : dict):
#         self._my_dict = mydict

#     def __iter__(self):
#         self._index_key = 0
#         self._index_value = 0
#         return self

#     def __next__(self):
#         if self._index_key == len(self._my_dict):
#             raise StopIteration 

#         _current_key = list(self._my_dict.keys())[self._index_key]
#         _current_value = self._my_dict[_current_key][self._index_value]
         
        
#         if(self._index_value == len(self._my_dict[_current_key]) -1):
#             self._index_value = 0
#             self._index_key += 1
#         else:
#             self._index_value += 1
#         return (_current_key,_current_value)
            




# products = {
#     "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
#     "Одяг": ["Футболка", "Джинси", "Куртка"],
#     "Книги": ["Роман", "Фентезі", "Наукова література"]
# }
# for value in MyIter(products):
#     print (f"{value}")






