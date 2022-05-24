a = int(input('Put number between 0 - 1000000 step 2: '))


class Solution:
    def get_list(self):
        return list(range(0, 1000000, 2))

    def get_target(self, list, target):
        self.start = 0
        self.end = len(list) - 1
        while self.start <= self.end:
            mid = self.start + (self.end - self.start) // 2

            element = list[mid]
            if element == target:
                return f'index: {mid}'
            elif target < element:
                self.end = mid - 1
            else:
                self.start = mid + 1
        return None


sol = Solution()
b = sol.get_list()
print(sol.get_target(b, a))

# написать поиск элемента по отсортированному списку
# используя алгоритм Binary Search ( Бинарный Поиск )
#
# после создать файл binary_search_docs.txt и ответить на вопросы:
#
# что такое Binary Search?
# зачем нужен Binary Search?
# принцип работы Binary Search - ….