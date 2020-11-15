import pandas as pd
from datetime import timedelta, date
import matplotlib.pyplot as plt

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)



def getFileByDate(date = 'latest'):
	url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-' + date + '.csv' #20200927.csv'
	df = pd.read_csv(url, error_bad_lines=False)
	return df


#default region is Sicily
def getValue(daily, column = 'nuovi_positivi', region='Sicilia'):
	regRaw = daily.loc[daily['denominazione_regione'] == region]
	regRaw.loc[regRaw['denominazione_regione'] == region]
	return regRaw[column].to_numpy()[0]	 #regRaw.at[16, column]		#return daily.iloc[2, 17]




def getAll(column, region):
	start_date = date(2020, 2, 24)
	end_date = date(2020, 4, 10)
	end_date = date.today()


	result = []
	for single_date in daterange(start_date, end_date):
		day = single_date.strftime("%Y%m%d")
		result.append(getValue(getFileByDate(day), column, region))	

	return result



nuovi_positivi = getAll('nuovi_positivi', 'Sicilia')
#deceduti = getAll('deceduti', 'Sicilia')
#dimessi_guariti = getAll('dimessi_guariti', 'Sicilia')



nuovi_positivi = pd.Series(nuovi_positivi, index=pd.date_range('2/24/2020', periods=len(nuovi_positivi)))
#deceduti = pd.Series(deceduti, index=pd.date_range('2/24/2020', periods=len(deceduti)))
#dimessi_guariti = pd.Series(dimessi_guariti, index=pd.date_range('2/24/2020', periods=len(dimessi_guariti)))

plt.figure();
ax = nuovi_positivi.plot()
#deceduti.plot(ax=ax)
#dimessi_guariti.plot(ax=ax)
plt.show()











