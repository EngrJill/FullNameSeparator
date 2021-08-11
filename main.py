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
            if (len(arr[i]) == 3):
                NewArr.append(["First Name: " + arr[i][0], "Middle Name: " + arr[i][1], "Last Name: " + arr[i][2]])

    return NewArr



# print(String_to_Array(Sentence_Case(remove_commas_dots(["JOSEPH sales ORtiZ","Joanna Denise Flores Dela Cruz",
#                                         "Shiela Mae Broñosa Reodique","Zabdiel Abarquez Agsunod",
#                                         "Kenneth John Bejo","Francia Guzman Monforte","Carla Salanguste Epino",
#                                         "Ranneil Ariban Rivera","Joanna Denise Flores Dela Cruz",
#                                         "Joseph Sales Ortiz","Raymart Gullem Fulo","Leamae, De Lemios, Germo",
#                                         "Sheana May Palma Bunao","Clayton Lawrence Buarao Beato",
#                                         "Mark Guadalupe Advincula","Kenneth Francis, Del Rosario, Felices",
#                                         "Ranier Abe Mirabueno. frial","Cyril Audrey Ambrocio Relato",
#                                         "Rose Antonette Estrella Paez","Kim John Sario Atento",
#                                         "Ma. Fe Anthonette A. Castro","Kimberly Loria Lovendino",
#                                         "Russel, Cañete, Bitancur","Mary Grace Cornel Oprecio",
#                                         "Ivan Cris Bonita Montealegre","John Dave R. Marbella",
#                                         "Joshua, Nipa, Anobling","Marc Lenray, Nacion, Magdaraog",
#                                         "Jazpher Jhay, Flores, Salazar","Jemuel Jireh Lanuzo Berunio",
#                                         "Lorraine Velasco Abache","Danielle Marie Igay","Kim John Sario Atento",
#                                         "Rose Antonette E. Paez","Carla Salanguste Epino",
#                                         "Lorraine Velasco Abache","Daniel Aclan Soriano II"]))))

print(Separate(String_to_Array(Sentence_Case(remove_commas_dots(["joseph ortis sdads", "joasdn asdha asdhads"])))))




