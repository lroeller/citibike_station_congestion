from urllib.request import urlopen
import json
import pandas as pd

# returnd pandas dataframe with all citibike data
def get_citibike_data():
  gbfs_url_source = json.loads(urlopen("http://gbfs.citibikenyc.com/gbfs/gbfs.json").read().decode("utf-8"))
  return pd.DataFrame(gbfs_url_source['data']['en']['feeds'])

#function used to create data column
def get_citibike_dataframes(row):
  return json.loads(urlopen(row['url']).read().decode("utf-8"))['data']

def main():
  data = get_citibike_data()
  data['df'] = data.apply (lambda row: get_citibike_dataframes(row),axis=1)
  data['keys'] = data.apply (lambda row: row['df'].keys(),axis=1)
  return data

def get_work_stations(df):
  stations = df.ix[1,'df']['stations']
  keys = [t['station_id'] for t in stations if (40.756040>=t['lat']>=40.752034)&(-73.967859>=t['lon']>-73.978787)]
  return [station for station in stations if station['station_id'] in keys]

