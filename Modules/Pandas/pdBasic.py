#https://github.com/pandas-dev/pandas
import pandas as pd

def Ex1():
  mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
  }

  df = pd.DataFrame(mydataset) # on tabular
  ds = pd.Series(zip(mydataset['cars'], mydataset['passings'])) # on array
  print(df)
  print(df.loc[1]) # locate row
  print(ds)

#Ex1()

def ReadFile():
  df = pd.read_csv('data.csv')
  print(df)
  #Tip: use df.to_string() to print the entire DataFrame.
  #If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
  #pd.options.display.max_rows to set or get max display rows default 60

  #df.to_json('data.json', orient='records', indent=4) # orient is interesting
  
  #jdf = pd.read_json('data.json')
  #print(jdf)

  #jdf.to_html('data.html')

  df.drop_duplicates(inplace = True)
  x = df["Calories"].mean() # get mean, median or fixed value and fill against empty column
  df["Calories"].fillna(x, inplace = True)
  df.dropna(inplace = True) # remove empty fileds record
  # df['Date'] = pd.to_datetime(df['Date']) # fixing format
  # loop through to fix out of range values :( not the bes option btw
  print(df)
  print(df.corr()) # -1~0~1 0 is bad, 1 is good, -1 is inverse corr
ReadFile()