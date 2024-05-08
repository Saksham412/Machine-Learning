
def simpleFormulaeBasedLR():
    
    def __init__(self):
        self.m = None
        self.b = None
    
    def fit(self, x_train, y_train):
        num = 0
        den = 0
        
        for i in range(x_train.shape[0]):
            num = num + ((x_train[0] - x_train.mean())*(y_train[0]-y_train.mean()))
            den = den + (x_train[0] - x_train.mean())**2
        
        self.m = num / den
        self.b = y_train.mean() - self.m * x_train.mean()
        # print(self.m)
        # print(self.b)
    
    def predict(self, x_test):
        return self.m * x_test + self.b