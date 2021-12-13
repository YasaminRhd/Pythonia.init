import pickle

class FileDict(dict):
    esm = ""
    def __Load(self,esm):
        try:
            with open(esm+'.pkl', 'rb') as f:
                data = pickle.load(f)
                for key in data:
                    setattr(self, key, data[key])
                return True
        except:
            return False

    def __init__(self, esm):
        super().__init__()
        self.esm = esm
        if self.__Load(esm) == False :
            pass

    def __getitem__(self,key):
        try :
            return getattr(self,key)
        except:
            return "none"

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __repr__(self):
        return repr(self.__dict__)

    def __del__(self):
        with open(self.esm + ".pkl", 'wb') as handle:
            pickle.dump(self.__dict__, handle, protocol=pickle.HIGHEST_PROTOCOL)






