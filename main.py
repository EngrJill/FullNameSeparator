#Remove Commas and dots in the full names
def remove_commas_dots(arr):
    NewArr = []

    for i in range(len(arr)):
        if ("." in arr[i]):
            NewArr.append(arr[i].replace(".",""))
        elif ("," in arr[i]):
            NewArr.append(arr[i].replace(",",""))
        else:
            NewArr.append(arr[i])

    return NewArr

#Convert Word to array
def String_to_Array(arr):
    arr2 = []
    for i in range(len(arr)):
        arr2.append(arr[i].split())

    return arr2

def Sentence_Case(arr):
    newArr = []
    for i in range(len (arr)):
        newArr.append(arr[i].title())

    return newArr

def Separate(arr):
    NewArr = []
    for i in range (len(arr)):
            if (len(arr[i]) == 2):
                NewArr.append([arr[i][0] +",", arr[i][1] + "\n"])

            elif (len(arr[i]) == 3):
                NewArr.append([arr[i][0] +",", arr[i][1] +",",arr[i][2] + "\n"])

            elif (len(arr[i]) == 4):
                NewArr.append([arr[i][0] + " " + arr[i][1] +",", arr[i][2] +",", arr[i][3]+ "\n"])

            elif (len(arr[i]) == 5):
                NewArr.append([arr[i][0] + " " + arr[i][1] + " " + arr[i][2] +",", arr[i][3] + ",", arr[i][4] + "\n"])

            elif (len(arr[i]) == 6):
                NewArr.append([arr[i][0]  + " " + arr[i][1]  + " " + arr[i][2] + " " + arr[i][3] +"," ,arr[i][4] +",",arr[i][5]+ "\n"])

    return NewArr

def Arr_To_String_1(arr):
    newArr = []
    names = ""
    for i in range(len(arr)):
        newArr.append(names.join(arr[i]))

    return newArr

def Arr_To_String_2(arr):
        names = ""
        return names.join(arr)



print(Arr_To_String_2(Arr_To_String_1
                      (Separate(String_to_Array(Sentence_Case(remove_commas_dots
                                                              ()))))))









