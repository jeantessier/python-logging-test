import inspect
import logging


class OtherClass:
    def bar(self):
        logging.info("In OtherClass.bar()", stack_info=True)

    def stack(self):
        return inspect.stack()
