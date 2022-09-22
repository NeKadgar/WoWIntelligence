
class GameInfo:
    """Singleton class

    Get instance only throw instance method!!!
    """

    _instance = None

    def __init__(self, x, y):
        self.x = None
        self.y = None
        self.facing = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls(1, 2)
        return cls._instance
