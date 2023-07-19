class A:
    def foo(self, a: int):
        print(a)



class B(A):
    def foo(self, a: int):
        print(a + 1)
