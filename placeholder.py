import matplotlib.pyplot as plt
import pandas as pd
import json

def load_waveform(filepath):
    with open(filepath) as dataFile:
        data = dataFile.read()
        obj = data[data.find('{') : data.rfind('}')+1]
        jsonObj = json.loads(obj)
        
        if jsonObj['data']:
            waveform_data = pd.DataFrame(jsonObj['data'])    
            return waveform_data
    return []

filepaths = []

filepaths.append("1001263.js") #negative
filepaths.append("1011083.js") #negative
filepaths.append("1054130.js") #positive

for filepath in filepaths:
  waveform = load_waveform(filepath)

  fig = plt.figure()
  fig.set_figwidth(20)     

  plt_1 = plt.subplot(1, 2, 1)    
  plt.plot(waveform[2], waveform[0], 'o')

  def show_waveform_head(filepath):
    waveform_data = load_waveform(filepath)
    if not waveform_data.empty:
        print(waveform_data.head())
    else:
        print("Error: No waveform data found.")

show_waveform_head("waveform.json")
