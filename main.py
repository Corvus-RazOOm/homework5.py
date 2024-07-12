immutable_var = 1, 2, "apple"
print(tuple (immutable_var))
#tuple(immutable_var)[0] = 123
# кортеж - неизменяемая часть, описание ошибки буквально говорит, что "Объект «кортеж» не поддерживает назначение элементов"
mutable_list = [1, 2, 3, "apple", "meat"]
print(mutable_list)
mutable_list [2] = "cake"
print(mutable_list)


