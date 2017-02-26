from model.load import Application
from model.resource import Resource


class ResourceManager(object):

    resources = Resource.resources
    load = Application.load

    def run(self, max_steps=500):

        i = 0
        graf = dict()

        graf['machine'] = dict()

        for key in self.load:
            graf[key] = dict()

            for r_key in self.resources:
                graf['machine'][r_key] = []
                graf[key][r_key] = []

        while i < max_steps:

            i += 1
            os = self.load['OS']

            for key in self.resources:
                self.resources[key].realise_quantum()
                need = os.need(key)
                self.resources[key].get_resource(need)
                graf['OS'][key].append((i, need))

            for (load_key, load) in self.load.items():
                if load_key != 'OS':
                    for resource_key in self.resources:
                        need = load.need(resource_key)
                        if self.resources[resource_key].left_quantum < need:
                            #ресурсы закончились простой
                            pass
                        else:
                            self.resources[resource_key].get_resource(need)

                        graf[load_key][resource_key].append((i, need))

            for key in self.resources:
                graf['machine'][key].append((i, self.resources[key].load))

        return graf
