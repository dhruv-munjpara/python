def get_value():
    for i in range(5):
        yield i

val=get_value()
print(val)
# for i in val:
#     print(i)

print(next(val))
print(next(val))