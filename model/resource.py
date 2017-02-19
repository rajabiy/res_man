class ResourceMount(type):

    def __init__(cls, name, bases, attrs):
        super(ResourceMount, cls).__init__(name, bases, attrs)
        if not hasattr(cls, 'resources'):
            cls.resources = dict()
        else:
            cls.register_class(cls)

    def register_class(cls, klass):
        cls.resources[klass.name] = klass


class Resource(metaclass=ResourceMount):
    name = 'TEMP'
    quantum = 1
    measure = 'TEMP'
    count = 1
    periodical = False

    def full_quantum(self):
        return self.quantum * self.count


class CPU(Resource):
    name = 'CPU'
    quantum = 1000
    measure = 'FLOPS'
    count = 2
    periodical = True

    def full_quantum(self):
        return self.quantum * self.count


class HDDIO(Resource):
    name = 'HDDIO'
    quantum = 1000
    measure = 'IOPS'
    periodical = True

    def full_quantum(self):
        return self.quantum * self.count


class HDD(Resource):
    name = 'HDD'
    quantum = 360000
    measure = 'MB'

    def full_quantum(self):
        return self.quantum * self.count


class RAM(Resource):
    name = 'RAM'
    quantum = '256'
    measure = 'MB'

    def full_quantum(self):
        return self.quantum * self.count
