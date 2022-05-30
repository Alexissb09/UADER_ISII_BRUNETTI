class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonPersonal(metaclass=SingletonMeta):
    def getCuit(self):
        return 'cuit-personal'
    def getid(self):
        return "Personal"

class SingletonVideoDigital(metaclass=SingletonMeta):
    def getCuit(self):
        return 'cuit-video_digital'
    def getid(self):
        return "Video_Digital"

if __name__ == "__main__":
    # The client code.

    s1 = SingletonPersonal()
    s2 = SingletonPersonal()

    s3 = SingletonVideoDigital
    s4 = SingletonVideoDigital

    if id(s1) == id(s2):     # ID retorna la identidad, si son la misma 
        print('El singleton funciona, contienen la misma instancia')
    else:
        print('El singleton no funciona, contienen diferente instancia')
