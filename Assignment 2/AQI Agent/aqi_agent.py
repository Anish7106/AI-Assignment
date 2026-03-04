"""
Team Pegasus
SE24UCSE015
SE24UCSE007
SE24UCSE092
SE24UCSE183
"""
import pandas as pd

"""
We give breakout points of each pollutant meaning : 
If pollution value is between X and Y, then AQI should be between A and B.
"""
BP = {
    "pm2_5": [(0,30,0,50),(31,60,51,100),(61,90,101,200),(91,120,201,300),(121,250,301,400),(251,10**9,401,500)],
    "pm10":  [(0,50,0,50),(51,100,51,100),(101,250,101,200),(251,350,201,300),(351,430,301,400),(431,10**9,401,500)],
    "no2":   [(0,40,0,50),(41,80,51,100),(81,180,101,200),(181,280,201,300),(281,400,301,400),(401,10**9,401,500)],
    "o3":    [(0,50,0,50),(51,100,51,100),(101,168,101,200),(169,208,201,300),(209,748,301,400),(749,10**9,401,500)],
    
    "co":    [(0.0,1.0,0,50),(1.1,2.0,51,100),(2.1,10.0,101,200),(10.1,17.0,201,300),(17.1,34.0,301,400),(34.1,10**9,401,500)],
    "so2":   [(0,40,0,50),(41,80,51,100),(81,380,101,200),(381,800,201,300),(801,1600,301,400),(1601,10**9,401,500)],
    "nh3":   [(0,200,0,50),(201,400,51,100),(401,800,101,200),(801,1200,201,300),(1201,1800,301,400),(1801,10**9,401,500)],
}
#Pre-determined AQI formula is used:
def sub_index(pollutant, c):
    if pd.isna(c):
        return None
    c = float(c)
    for c1, c2, i1, i2 in BP[pollutant]:
        if c1 <= c <= c2:
            return round((i2 - i1) / (c2 - c1) * (c - c1) + i1)
    return None
#These are the conditions that send out a message stating the quality of air : 
def category(aqi):
    if aqi <= 50: return "Good"
    if aqi <= 100: return "Satisfactory"
    if aqi <= 200: return "Moderate"
    if aqi <= 300: return "Poor"
    if aqi <= 400: return "Very Poor"
    return "Severe"


def reflex_aqi_agent(csv_path, city=None, date=None):
    df = pd.read_csv(csv_path)

   
    if city is not None:
        df = df[df["City"].astype(str).str.lower() == str(city).lower()]
    if date is not None:
       
        df = df[df["Date"].astype(str) == str(date)]

    if df.empty:
        print("No rows found for given filter.")
        return

    row = df.sample(1).iloc[0] 
    col_map = {
        "pm2_5": "PM2.5",
        "pm10": "PM10",
        "no2": "NO2",
        "nh3": "NH3",
        "co": "CO",
        "so2": "SO2",
        "o3": "O3",
    }

    subs = {}
    for key, col in col_map.items():
        if col in row.index:
            si = sub_index(key, row[col])
            if si is not None:
                subs[key] = si

    if not subs:
        print("no pollutant values available in this row to compute AQI.")
        return

    dom = max(subs, key=subs.get)
    aqi = subs[dom]

    print("City:", row.get("City"))
    print("Date:", row.get("Date"))
    print("Computed AQI:", aqi)
    print("Category:", category(aqi))
    print("Dominant pollutant is:", dom)
    print("Sub indices:", subs)


    if "AQI" in row.index and not pd.isna(row["AQI"]):
        print("Dataset AQI (given):", int(row["AQI"]))
        if "AQI_Bucket" in row.index:
            print("Dataset Bucket (given):", row["AQI_Bucket"])

#CSV file that contains dataset : 
reflex_aqi_agent("visakhapatnam_aqi.csv")
