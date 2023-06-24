def sizer(cls):
    class SizedClass(cls):
        @property
        def size(self):
            try:
                return len(self)
            except TypeError:
                try:
                    return abs(self)
                except TypeError:
                    return 0

        def __len__(self):
            if isinstance(self.data, (int, float)):
                return 1
            else:
                return len(self.data)

    return SizedClass

@sizer
class MyClass:
    def __init__(self, data):
        self.data = data
my_obj = MyClass([1, 2, 3])
print(my_obj.size)  # 3

my_obj = MyClass(-1)
print(my_obj.size)  # 1

my_obj = MyClass(None)
print(my_obj.size)  # 0