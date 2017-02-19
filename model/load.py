class ResourceLoad(type):

    def __init__(cls, name, bases, attrs):
        super(ResourceLoad, cls).__init__(name, bases, attrs)
        if not hasattr(cls, 'load'):
            cls.load = dict()
        else:
            cls.register_class(cls)

    def register_class(cls, klass):
        cls.load[klass.name] = klass


class Application(metaclass=ResourceLoad):
    pass


class OS(Application):
    name = 'OS'
    CPU = 400
    HDDIO = 1000
    RAM = 78
    HDD = 7000
    priority = 0


class App1(Application):
    name = 'name.exe'
    CPU = 4000
    INS_C = 60000
    HDDIO = 1000
    RAM = 78
    HDD = 7000
    priority = 1


class App2(Application):
    name = 'ppd.exe'
    CPU = 40000
    INS_C = 72500
    HDDIO = 1000
    RAM = 78
    HDD = 7000
    priority = 2