from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # Okay
        pass

    def fax(self, document):
        pass     # do nothing

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan a document")


class Printer:
    @abstractmethod
    def print(self, document, *args, **kwargs):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document, *args, **kwargs):
        pass


class MyPrinter(Printer):
    def print(self, document, *args, **kwargs):
        print(document)


class PhotoCoppier(Printer, Scanner):
    def print(self, document, *args, **kwargs):
        print(document)

    def scan(self, document, *args, **kwargs):
        pass