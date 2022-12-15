import logging


class MyClass:
    def foo(self):
        logging.info("In MyClass.foo()", stack_info=True)

    def foo_with_exception(self):
        try:
            raise Exception("throwing in MyClass.foo_with_exception")
        except Exception as ex:
            logging.exception("In MyClass.foo_with_exception()", stack_info=True)
