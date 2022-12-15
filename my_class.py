import logging


class MyClass:
    def foo(self):
        logging.info("In MyClass.foo()", stack_info=True)
