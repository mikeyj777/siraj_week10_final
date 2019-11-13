# siraj_week10_final

"training_forex_model.ipynb" - notebook detailing method for training each pair of currencies using an sci-kit's regression SVM.

"fx.py"
 - contains the class for performing prediction.  
 - instantiate fxpredict with initial arguments date, currency from, and currency to.  
 - the class's 'predicted' property is calculated automatically upon instantiating the object.  this is the predited currency exchange rate on the specified date.
 - valid currencies are in the 'validcurrencies' property.  the object will test if the from/to currency is in the list, and will set 'predicted' to 0 if not.