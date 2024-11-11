
with open("client_import.csv", 'r', encoding="utf-8") as file:
    arr = file.readlines()
    # print(arr)   # список строк из данных каждой строки

    for i in range(1, len(arr)):
        result = []
        data = arr[i].strip()
        # print(data)         #строка из файла
        data_arr = (data.split(";"))
        # print(data_arr)  # список из данных одной строки

        last_name = data_arr[0].strip()  # фамилия - первый столбец
        # print(last_name)

        fio = last_name.split()
        if len(fio) > 1:
            data_arr[0] = fio[0]  # фамилия
            data_arr[1] = fio[1]  # имя
            data_arr[2] = fio[2]  # отчество
        last_name = data_arr[0].strip()     #фамилия
        first_name = data_arr[1].strip()  # имя
        sur_name = data_arr[2].strip()  # отчество
        gender = data_arr[3].strip()
        if gender == "женский" or gender == "ж":
            gender = 2
        if gender == "мужской" or gender == "м":
            gender = 1
        phone = data_arr[4].strip().replace("(", "").replace(")", "").replace("-", "")

        avatar = data_arr[5].strip().split("\\")[1]
        birthday = data_arr[6].strip()
        email = data_arr[7].strip()
        date_reg = data_arr[8].strip()

        result.append(i)                #result[0]
        result.append(last_name)        #result[1]
        result.append(first_name)
        result.append(sur_name)
        result.append(gender)
        result.append(phone)
        result.append(avatar)
        result.append(birthday)
        result.append(email)
        result.append(date_reg)

        print(result)

with open("clientservice_s_import.csv", 'r', encoding="utf-8") as f:
    orr = f.readlines()
    for i in range(1, len(orr)):
        result1 = []

        data1 = orr[i].strip()

        data_orr = (data1.split(";")) #массив из данных файла

        str=data_orr[1].split() #дата/время
        l_name=data_orr[0].split() #фамилия

        result1.append(i)
        result1.append(str[0])
        result1.append(str[1])
        result1.append(data_orr[2])

        print(result1)







