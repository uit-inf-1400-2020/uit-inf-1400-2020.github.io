class CsvReader:
    def __init__(self, filename):
        self.f = filename

    def read(self):
        '''
        Reads data from file into this class
        returns: nothing
        '''
        f = open(self.f)
        self.data = f.readlines()
        f.close()

    def parse(self):
        '''
        Parses already-read data
        returns: dictionary of keys and values from file
        throws: NameError if no data has been read
        '''
        result = {}
        for l in self.data:
            key, data = l.split(",")
            result[key] = data
        return result

class TextReader(CsvReader):
    def parse():


if filename[-4:-1] == "txt":
    r = TextReader()
else:
    r = CsvReader()
r.read()
data = r.parse()
