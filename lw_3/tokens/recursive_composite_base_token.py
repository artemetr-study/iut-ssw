from lw_3.tokens.composite_base_token import CompositeBaseToken

CLS = 'cls'


class RecursiveCompositeBaseToken(CompositeBaseToken):
    @classmethod
    def subclasses(cls):
        return cls.__subclasses__()
