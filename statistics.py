import pandas as pd
def calculateStats(numbers):
  df = pd.DataFrame(numbers, columns=['numbers'])
  df = pd.DataFrame(data)
  mean_df = df['numbers'].mean()
  max_df = df['numbers'].max()
  min_df = df['numbers'].min()
  return [mean_df,max_df,min_df]
