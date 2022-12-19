import logging

from my_class import MyClass
from other.other_class import OtherClass
from deeply.nested.package.package_class import PackageClass


def main():
    FORMAT = '%(asctime)s level---%(levelname)s module---%(module)s filename---%(filename)s lineno---%(lineno)d funcName---%(funcName)s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    my_class = MyClass()
    my_class.foo()
    my_class.foo_with_exception()

    other_class = OtherClass()
    other_class.bar()

    package_class = PackageClass()
    package_class.baz()

    my_s = my_class.stack()
    print(f"{my_s=}")
    for f in my_s:
        print(f"    {f}")
    print(f"{len(my_s)=}")
    print()

    other_s = other_class.stack()
    print(f"{other_s=}")
    for f in other_s:
        print(f"    {f}")
    print(f"{len(other_s)=}")
    print()

    my_fn = my_class.func_name()
    print(f"{my_fn=}")
    print()


if __name__ == "__main__":
    main()
