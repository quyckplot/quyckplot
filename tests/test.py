class Test():
    def method_builder(f):
        def method():
            print("method")
            f()
        return method

    def test():
        print("test")

    # build a class method from test
    new_test = classmethod(method_builder(test))

# def test():
#     print("test")

# a = Test.method_builder(test)
Test.new_test()