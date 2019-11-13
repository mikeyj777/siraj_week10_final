from sklearn.svm import SVR
import joblib
import numpy as np
from datetime import datetime
from datetime import date
import dateutil.parser

class fxpredict:
    def __init__(self, datestr, currfrom, currto):
        self.currfrom = str(currfrom).upper()
        self.currto = str(currto).upper()
        self.datestr = datestr
        self.validcurrencies = ['USD', 'AUD', 'BGN', 'BRL', 'CHF', 'CNY', 'DKK', 'HRK', 'MYR', 'NOK', 'NZD', 'PLN', 'RON']
        self.convertdate()
        self.getprediction()
        
        
    def convertdate(self):
        tempdate = dateutil.parser.parse(self.datestr)
        dto = datetime.strptime(str(tempdate),'%Y-%m-%d  %H:%M:%S')
        self.datestr = dto.strftime('%Y-%m-%d')

        date_format = '%Y-%m-%d'
        a = datetime.strptime(self.datestr, date_format)
        b = datetime.strptime('1899-12-30', date_format)
        datediff = a - b
        self.thedate = datediff.days
    
    def getprediction(self):
        
        self.predicted = 0
        if self.currfrom in self.validcurrencies and self.currto in self.validcurrencies:
        
            filefrom = 'sav/fxpredsklearn_SVR_USD_' + self.currfrom + '.sav'
            fileto = 'sav/fxpredsklearn_SVR_USD_' + self.currto + '.sav'

            
            predfrom = 1
            if self.currfrom != 'USD':
                clffrom = joblib.load(filefrom)
                predfrom = clffrom.predict(np.asarray([self.thedate]).reshape(-1, 1))
                predfrom = predfrom[0]

            predto = 1
            if self.currto != 'USD':
                clfto = joblib.load(fileto)
                predto = clfto.predict(np.asarray([self.thedate]).reshape(-1, 1))
                predto = predto[0]


            exrate = predto / predfrom
            self.predicted = exrate
        self.predicted = '%.4g' % (self.predicted)


testdate = '2011-08-01'
testvalidcurrencies = ['USD', 'AUD', 'BGN', 'BRL', 'CHF', 'CNY', 'DKK', 'HRK', 'MYR', 'NOK', 'NZD', 'PLN', 'RON']

for currfrom in testvalidcurrencies:
    for currto in testvalidcurrencies:
        if currfrom != currto:
            fxpred = fxpredict(testdate, currfrom, currto)

            print('the value of 1 ' + fxpred.currfrom + ' is equal to ' + \
                str(fxpred.predicted) + ' in ' + fxpred.currto + \
                ' as predicted for ' +  str(fxpred.datestr))
