import inspect
import logging


class MyClass:
    def foo(self):
        logging.info("In MyClass.foo()", stack_info=True)

    def foo_with_exception(self):
        try:
            raise Exception("throwing in MyClass.foo_with_exception")
        except Exception as ex:
            logging.exception("In MyClass.foo_with_exception()", stack_info=True)

    def stack(self):
        return inspect.stack()

    def func_name(self):
        return logging.getLogger().makeRecord('root', logging.INFO, 'this is fn', 123, 'this is the message', None, None, func="explicit func_name").funcName
