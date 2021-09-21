# Prediction of Drought Levels

## Introduction

In the last years, climate change has become a more popular topic in the worldwide news. It affects our lives in multiple areas. One popular effect that it has is global warming. It is the effect that, due to human-induced greenhouse gas emissions, the average temperature will rise in the lower levels of the atmosphere. (Zitat Wikipedia)  
With the rise of the average temperature drought periods will happen more often. This is especially problematic for countries whose average temperature is already higher than the average temperature in Germany.  
The effect is particularly bad for agriculture.  
The weather forecast is often only accurate for the next few days. What if there was a method to predict the rough drought level for a longer timespan? This is where our project comes into play.

## Dataset

We used a Dataset from Kaggle.com which contained weather data from the US from the years 2000 until 2020. In the dataset, the feature variable was a score ranging from 0 (no drought) to 5 (D4). D4 is the highest level of drought. There are six levels of drought possible. (Bild einfügen) This dataset was constructed with data from the US Drought Monitor and the NASA POWER Project.  
The U.S. Drought Monitor is a map released every Thursday, showing parts of the U.S. that are in drought. The map uses five classifications:  
abnormally dry (D0), showing areas that may be going into or are coming out of drought, and four levels of drought: moderate (D1), severe (D2),  
extreme (D3) and exceptional (D4). The NASA POWER Project provides solar and meteorological data sets from NASA research for support of renewable energy, building energy efficiency and agricultural needs.

## Method

**_Exploratory data analysis_**  
In the Kaggle dataset, we were given a "train time series" which contains roughly 16 years of data. Due to the sheer size of this time series, we decided to cut the dataset down to 2 years for our first explorations and the first model testings. So we did all the following explorations with the years 2000 until 2002.  
The dataset contains 21 different columns, with one of them being a date column, which we used as the index column in our exploration.  
The columns contain the following information:

| Indicator   | Description                           |
| ----------- | ------------------------------------- |
| WS10M_MIN   | Minimum Wind Speed at 10 Meters (m/s) |
| QV2M        | Specific Humidity at 2 Meters (g/kg)  |
| T2M_RANGE   | Temperature Range at 2 Meters (C)     |
| WS10M       | Wind Speed at 10 Meters (m/s)         |
| T2M         | Temperature at 2 Meters (C)           |
| WS50M_MIN   | Minimum Wind Speed at 50Meters (m/s)  |
| T2M_MAX     | Maximum Temperature at 2 Meters (C)   |
| WS50M       | Wind Speed at 50 Meters (m/s)         |
| TS          | Earth Skin Temperature (C)            |
| WS50M_RANGE | Wind Speed Range at 50 Meters (m/s)   |
| WS50M_MAX   | Maximum Wind Speed at 50 Meters (m/s) |
| WS10M_MAX   | Maximum Wind Speed at 10 Meters (m/s) |
| WS10M_RANGE | Wind Speed Range at 10 Meters (m/s)   |
| PS          | Surface Pressure (kPa)                |
| T2MDEW      | Dew/Frost Point at 2 Meters (C)       |
| T2M_MIN     | Minimum Temperature at 2 Meters (C)   |
| T2MWET      | Wet Bulb Temperature at 2 Meters (C)  |
| PRECTOT     | Precipitation (mm day-1)              |


Plus, three additional columns contain non-meteorological data:


| Indicator | Description                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| date      | Date of the measurement (Format YYYY-MM-DD)                                                                |
| fips      | US county FIPS code. see: https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_0136 |
| score     | Measure of drought ranging from 0 (no drought) to 5 (D4, see description)                                  |

But first, let's take a look at the score variable and its description.
There are six levels of drought according to the U.S. Drought Monitor[QUELLE DROUGHT MONITOR].

In the dataset, these levels are a numerical feature. So 1=D0, 2=D1, etc..
The plotted feature (over 3 years 2000-2002) looks like this:
[FIGURE 1]  
If we take a look at a smaller period we notice a problem, we have missing values in our data.
[FIGURE 2] 

**_Missing values_**

The missing values 

_Models and results_

## Project Results

## Conclusion

## References
