import datetime

def camPerArrondissement(text):
	dict_Arrondissements = {}
	for l in text:
		#print(l)
		w=l.strip().split(',')
		if w[0] in dict_Arrondissements:
			
			dict_Arrondissements[w[0]] +=1
		else:
			dict_Arrondissements[w[0]] = 1
	return dict_Arrondissements

def firstInstalledCam(dict_num_date):
	min_date = datetime.datetime(2022,11,7)
	for num in dict_num_date:
		if dict_num_date[num] < min_date:
			min_date = dict_num_date[num]
			num_cam = num
	return num_cam,min_date

def mostCamArr(dict_arr):
	max_cam = 0
	for arrondissement in dict_arr:
		if dict_arr[arrondissement] >max_cam:
			max_cam = dict_arr[arrondissement]
			max_arr = arrondissement
	
	return max_arr, max_cam

def numberCam(data):
	#print(len(data))
	return len(data)

def numberCamAndDate(text):
	dict_num_date = {}
	for l in text:
		#print(l)
		w=l.strip().split(',')
		if len(w[-1].strip().split(" "))>1:
			y = w[-1].strip().split(" ")[-1]
			m = d = 1
			#print(y,m,d)
		else:
			m,d,y = w[-1].strip().split('/')
		
		#m,d,y = w[-1].strip().split('/')
		w[-1] = datetime.datetime(int(y),int(m),int(d))
		#print(w[1])
		if w[1] in dict_num_date:
			print("Error")
		else:
			dict_num_date[w[1]] = w[-1]

		#print(type(w[-1]))
	return dict_num_date

def number0fCameraForDate(date):
	list_num = []
	for num in dict_num_date:
		if dict_num_date[num] == date:
			#print(num)
			list_num.append(num)
	return list_num

def numberOfCameraInArr(doc,arr):
	listCamArr = []
	for l in text:
		#print(l)
		w=l.strip().split(',')
		#print(w[1])
		if arr <10:
			#print(w[0][-1])
			if (int(w[0][-1]) == arr and int(w[0][-2]) == 0):
				listCamArr.append(l)
				
	return list(listCamArr)



with open('2018-11-14-liste-cameras-pvpp-sur-paris-site-internet.csv', 'r', encoding="utf-8",) as MyTestFile:
	text = MyTestFile.readlines()[1:]
	
	print("Number of camera in paris in November 2018:")
	num = numberCam(text)
	print(num)

	print("\nPrint all information about cameras in the 5th arrondissement:")
	resultNumCarArr = numberOfCameraInArr(text,5)
	print(resultNumCarArr)

	print("\nNumber of cameras in each arrondissement:")
	arr = camPerArrondissement(text)
	print(arr)

	print("\nArrondissement with the highest number of camera:")
	[max_cam_arr, max_cam] = mostCamArr(arr)
	print(max_cam_arr, max_cam)

	print("\nDate of fisrt camera installed in paris:")
	dict_num_date = numberCamAndDate(text)
	
	[numero_first_camera,date_first_camera] = firstInstalledCam(dict_num_date)
	print(date_first_camera)


	print("\nNumber of all the camera installed the first date:")
	list_num_for_date = number0fCameraForDate(date_first_camera)
	print(list_num_for_date)

