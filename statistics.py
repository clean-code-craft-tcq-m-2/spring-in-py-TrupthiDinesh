
def calculateStats(numbers):
  computedStats = {}
  if len(numbers) == 0:
    computedStats["avg"] = nan
    computedStats["max"] = nan
    computedStats["min"] = nan
  
  computedStats["avg"] = sum(numbers)/len(numbers)
  computedStats["max"] = max(numbers)
  computedStats["min"] = min(numbers)
  return computedStats
