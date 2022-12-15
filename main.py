import logging

from my_class import MyClass
from other.other_class import OtherClass


def main():
    FORMAT = '%(asctime)s level---%(levelname)s module---%(module)s filename---%(filename)s lineno---%(lineno)d funcName---%(funcName)s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    my_class = MyClass()
    my_class.foo()

    other_class = OtherClass()
    other_class.bar()


if __name__ == "__main__":
    main()
