def getAllCrimesAllBorough(dataframe, index = 3):
	dictCrimesBorough = {}
	for l in dataframe[1:]:
		w=l.strip().split(',')
		if w[2] in dictCrimesBorough:
			dictCrimesBorough[w[2]] += int(w[index])
		else:
			dictCrimesBorough[w[2]] = int(w[index])
	return dictCrimesBorough


def getIndexOfMonth(dataframe, month):
	w=dataframe.strip().split(',')
	for col in w:
		if col == month:
			colIndex = w.index(col)
	
	return colIndex

def getListOfMonths(dataframe):
	listMonths=dataframe.strip().split(',')
	return(listMonths[3:])


if __name__ == "__main__":

	with open('MPS Borough Level Crime (most recent 24 months).csv', 'r', encoding="utf-8",) as LondonCrimes:
		dataset = LondonCrimes.readlines()[0:]
		#print(dataset)

		print("\nTotal number of crimes across all boroughs in '202011' ")
		numCrimes = getAllCrimesAllBorough(dataset)
		print(numCrimes)

		print("\nList of all months available in the dataset")
		listOfMonths = getListOfMonths(dataset[0])
		print(listOfMonths)


		print("\nIndex of month and all crimes for that month")
		print("\nWhich month do you want to query ?")
		indexOfCol = getIndexOfMonth(dataset, listOfMonths[1])
		print(indexOfCol)

		print("\nTotal number of crimes across all boroughs in a specific month")
		numCrimesMonth = getAllCrimesAllBorough(dataset, indexOfCol)
		print(numCrimesMonth)