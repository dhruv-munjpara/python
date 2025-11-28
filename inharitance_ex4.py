class base_class:
    varA="hello this is A class"

class derive_class1:
    varB="hello this is b class"

class derive_class2(base_class,derive_class1):
    varC="hello thid is C class"

derive_class_2=derive_class2()
print(derive_class2.varC)
print(derive_class2.varB)
print(derive_class2.varA)
