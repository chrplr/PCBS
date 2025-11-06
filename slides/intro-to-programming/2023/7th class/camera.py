import datetime

def camPerArrondissement(text):
  dict_Arrondissements = {}
  for l in text:
    #print(l)
    w=l.split(';')
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


# Function that lists the number of line in the file, therefore the number of cameras
def numberCam(data):
  #print(len(data))
  return len(data)

# Function that return a dictionnary with 
def numberCamAndDate(text):
  dict_num_date = {}
  for l in text:
    #print(l)
    w=l.split(';')
    print(w[-1], type(w[-1]), w[-1]=="#N/A")
    if w[-1] == "inconnue\n": 
      continue
    elif "#" in w[-1]:
      continue
    elif len(w[-1].split(" "))>1:
      y = w[-1].split(" ")[-1]
      m = d = 1
      w[-1] = datetime.datetime(int(y),int(m),int(d))
      
    else:
      d,m,y = w[-1].split('/')
      w[-1] = datetime.datetime(2000+int(y),int(m),int(d))
    #print(m,int(d),y)
    #m,d,y = w[-1].strip().split('/')
    
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
  

# Function that list the number of camera in one arrondissement
def numberOfCameraInArr(doc,arr):
  listCamArr = []
  print(arr + 75000)
  
  for l in text:
    #print(l)
    w=l.strip().split(';') # Because ',' are used in the doc the separator is a ";" now. So the split() has to be notified.
    if arr +75000 < 75010: # if the Arrondissement is lower than 10 we only have to concentrate on the last digit of the column Code Postal
      if (int(w[0][-1]) == arr and int(w[0][-2]) == 0):
        listCamArr.append(l)
    else: # else the arrondissement is greater than 10 so we have to compare the 2 last digit of the code postal.
      if (int(str(w[0][-2])+str(w[0][-1])) == arr):
        listCamArr.append(l)

  return list(listCamArr)



def mostCamArr(dict_arr):
  max_cam = 0
  for arrondissement in dict_arr:
    if dict_arr[arrondissement] >max_cam:
      max_cam = dict_arr[arrondissement]
      max_arr = arrondissement
  return max_arr, max_cam  



if __name__ == "__main__":
  with open('camera.csv', 'r', encoding="utf-8",) as MyTestFile:
    text = MyTestFile.readlines()[1:] # To avoid the first line with the headers for every column
    #print(text)


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

    print("\nDate of first camera installed in paris:")
    dict_num_date = numberCamAndDate(text)
    [numero_first_camera,date_first_camera] = firstInstalledCam(dict_num_date)
    print(date_first_camera)

    print("\nNumber of all the camera installed the first date:")
    list_num_for_date = number0fCameraForDate(date_first_camera)
    print(list_num_for_date)