class BaseToken:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'<[{self.__class__.__name__}](value=`{self.value}`)>'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and self.value == other.value

    @classmethod
    def parse(cls, symbol):
        pass

    @classmethod
    def subclasses(cls):
        return cls.__subclasses__()
