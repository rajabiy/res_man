class ResourceMount(type):

    def __init__(cls, name, bases, attrs):
        super(ResourceMount, cls).__init__(name, bases, attrs)
        if not hasattr(cls, 'resources'):
            cls.resources = dict()
        else:
            cls.register_class(cls)

    def register_class(cls, klass):
        cls.resources[klass.name] = klass()


class Resource(metaclass=ResourceMount):
    name = 'TEMP'
    quantum = 1
    measure = 'TEMP'
    count = 1
    periodical = False
    used_quantum = 0

    @property
    def full_quantum(self):
        return self.quantum * self.count

    @property
    def left_quantum(self):
        return self.quantum * self.count - self.used_quantum

    @property
    def load(self):
        return self.used_quantum / self.quantum * 100

    def realise_quantum(self, quantum=0):
        if self.periodical and quantum == 0:
            self.used_quantum = 0
        else:
            self.used_quantum -= quantum

    def get_resource(self, quantum):

        if self.left_quantum - quantum < 0:
            self.used_quantum += self.left_quantum
            return self.left_quantum
        else:
            self.used_quantum += quantum
            return quantum


class CPU(Resource):
    name = 'CPU'
    quantum = 2e9
    measure = 'FLOPS'
    count = 2
    periodical = True


class HDDIO(Resource):
    name = 'HDDIO'
    quantum = 5e5
    measure = 'IOPS'
    periodical = True


class HDD(Resource):
    name = 'HDD'
    quantum = 360000
    measure = 'MB'


class RAM(Resource):
    name = 'RAM'
    quantum = 2e3
    measure = 'MB'
    periodical = True
