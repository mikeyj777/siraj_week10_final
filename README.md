# Foreign Exchange Rate Prediction Model

"training_forex_model.ipynb" - Jupyter Notebook detailing method for training the model for each pair of currencies
 - Uses Sci-Kit's regression SVM.

"fx.py" - Contains the class for performing prediction.  
 - Instantiate fxpredict with initial arguments date, currency from, and currency to.  
 - The class's 'predicted' property is calculated automatically upon instantiating the object.  this is the predited currency exchange rate on the specified date.
 - Valid currencies are in the 'validcurrencies' property.  the object will test if the from/to currency is in the list, and will set 'predicted' to 0 if not.

 "data/fxdata.csv" - Training dataset (date and exchange rate)

 "sav/*.sav" - Trained models from USD to each valid currency.  
  - Saved using 'joblib'.
  - USD is the internal currency, and the from/to exchange rates are converted on its basis.
  - The 'sav' files for the to and from currency targets are loaded by the prediction class in fx.py. 