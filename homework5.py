tuple_ = 7, 'table', '9', False
immutable_var = tuple_
print(type(immutable_var))
print(immutable_var)
print(tuple_[1])
#tuple_[1] = '8' при попытке изменить значение выходит ошибка, следовательно изменить значение нельзя.
mutable_list = ['work', 29, True, 'Diana']
print(mutable_list)
print(type(mutable_list))
print(mutable_list[3])
mutable_list[3] = 'hot'
print(mutable_list)