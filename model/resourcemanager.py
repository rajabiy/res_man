from model.load import Application
from model.resource import Resource


class ResourceManager(object):

    resources = Resource.resources
    load = Application.load
    i = 0

    def run(self):
        os = self.load['OS']
        for key in self.resources:
            print(key)
            print(self.resources[key].full_quantum(self.resources[key]))
            print(getattr(os, key))


'''
        while True:
            self.i += 1

            os = self.load['OS']

            print(self.i)

'''


res = ResourceManager()

res.run()