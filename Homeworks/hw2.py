"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
#user_input = '1,2,3,4,5,6,7'

user_input = input('Введите список элементов через запятую! \n')
work_list = user_input.split(',')
finish_index = (len(work_list) - 1)
temp_index = 0
while temp_index != finish_index:
    work_list[temp_index], work_list[temp_index + 1] = work_list[temp_index + 1], work_list[temp_index]
    temp_index += 2
print(work_list)
