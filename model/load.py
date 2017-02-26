from random import randint


class ResourceLoad(type):

    def __init__(cls, name, bases, attrs):
        super(ResourceLoad, cls).__init__(name, bases, attrs)
        if not hasattr(cls, 'load'):
            cls.load = dict()
        else:
            cls.register_class(cls)

    def register_class(cls, klass):
        cls.load[klass.job.get('name')] = klass()


class Application(metaclass=ResourceLoad):
    job = dict(name='TEMP', CPU=0, HDDIO=0,
               RAM=0, HDD=0, priority=0)

    def need(self, resource):
        return randint(0, self.job.get(resource, 0))


class OS(Application):
    job = dict(name='OS', CPU=4e8, HDDIO=2e3,
               RAM=7e2, HDD=7e3, priority=0)


class App1(Application):
    job = dict(name='app1.exe', CPU=4e8, HDDIO=2e3,
               RAM=4e2, HDD=1e3, priority=1)


class App2(Application):
    job = dict(name='app2.exe', CPU=2e8, HDDIO=2e2,
               RAM=6e2, HDD=1e3, priority=1)