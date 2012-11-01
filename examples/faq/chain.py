from disco.job import Job
from disco.worker.classic.func import chain_reader

class FirstJob(Job):
    input = ['raw://0', 'raw://0']

    @staticmethod
    def map(line, params):
        yield int(line) + 1, ""

class ChainJob(Job):
    map_reader = staticmethod(chain_reader)

    @staticmethod
    def map(key_value, params):
        yield int(key_value[0]) + 1, key_value[1]

if __name__ == "__main__":
    last = FirstJob().run()
    for i in xrange(9):
        last = ChainJob().run(input=last.wait())
    print(last.name)
