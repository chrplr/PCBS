# Function that lists the number of line in the file, therefore the number of cameras
def numberCam(data):
  #print(len(data))
  return len(data)

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