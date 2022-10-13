
def calculateStats(numbers):
  mean_df = sum(numbers)/len(numbers)
  max_df = max(numbers)
  min_df = min(numbers)
  return [mean_df,max_df,min_df]
