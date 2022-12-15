import logging


class PackageClass:
    def baz(self):
        logging.info("In PackageClass.baz()", stack_info=True)
