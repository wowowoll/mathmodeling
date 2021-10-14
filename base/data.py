from models import ms
from sklearn import metrics

class DataModel:
    def __init__(self, Traindata: dict, Testdata:dict, res: dict, model: str):
        self.Models = {}
        self.modelname = model
        self.Traindata = Traindata
        self.Testdata = Testdata
        self.res = res
        self.TrainX = None
        self.TrainY = None
        self.TestX = None
        self.TestY = None
        self.PredY = None
        self.model = None
        self.__gettrainval__()
        self.__gettestval__()
        self.register_models()

    def __gettrainval__(self):
        x = []
        y = []
        for k, v in self.Traindata:
            x.append(v)
            y.append(self.res[k])
        self.TrainX = np.array(x)
        self.TrainX = np.array(y)

    def __gettestval__(self):
        x = []
        y = []
        for k, v in self.Testdata:
            x.append(v)
            y.append(self.res[k])
        self.TestX = np.array(x)
        self.TestY = np.array(y)

    def register_models(self):
        for model in ms:
            k, v = model()
            self.Models[k] = v
    
    def Run(self):
        self.model = self.Models[self.modelname]
        self.model.fit(self.TrainX, self.TrainY)
        self.PredY = self.model.predict(self.Test)

    def F1Score(self, average="macro"):
        # average: "macro" "micro" weighted" "samples"
        return metrics.f1_score(self.TestY, self.PredY, average=average)

    def AccuracyScore(self):
        return metrics.accuracy_score(self.TestY, self.PredY)
    
    def AveragePrecisionSscore(self):
        return metrics.average_precision_score(self.TestY, self.PredY)



    def Predict(self, TestData:dict)->dict:
        res = {}
        for k, v in TestData:
            res[k] = self.model.predict([v])
    
        return res

        



    