# # # # grade_points =  [31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]

# # # # total_points = 0  

# # # # for grade in grade_points:
# # # #     total_points += grade


# # # # failed = 0

# # # # passed = 0


# # # # for i in grade_points:
# # # #     if i < 51:
# # # #         failed += 1
# # # #     elif i > 80:
# # # #         passed += 1


# # # # print("umumi telebelerin sayi" , len(grade_points))
# # # # print("ortalama : " , total_points / len(grade_points))
# # # # print("failed studenta : " , failed / len(grade_points) * 100 )
# # # # print("passed students : " , passed / len(grade_points) * 100 )




# # # # number = input("enter numbers")

# # # # result = []

# # # # for i in number[::-1]:
# # # #     result.append(int(i))
# # # # print(result)





# # # ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']

# # # # # print (ferma.index("keci"))
# # # # # ferma.sort()
# # # # # print(ferma)

# # # # # ferma.remove("at")

# # # # # ferma.append("toyuq")
# # # # # print(ferma)

# # # # # ferma.insert(0 , "keci")

# # # # # ferma = ferma[:len(ferma)//2]
# # # # # print(ferma)

# # # # # new_animals = ['at', 'qoyun', 'inek', 'inek', 'qoyun']

# # # # # ferma.extend(new_animals)
# # # # # print(ferma)

# # # # # print (ferma * 3 )
# # # # # print (ferma[::-1])
# # # # # ferma.clear()
# # # # # print(ferma)
# # # # inek_sayi = ferma.count("inek")

# # # # print( round(inek_sayi/len(ferma)*100, 2))
# # # # ferma2 = ferma.copy()
# # # # print(ferma2)











# # # # result = [0, 0]
# # # # numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# # # # sums_minus = 0
# # # # sum_plus = 0

# # # # for i in numbers:
# # # #     if i > 0:
# # # #         sum_plus += i
# # # #     else:
# # # #         sums_minus += i
# # # # result[0] = sum_plus
# # # # result[1] = sums_minus
# # # # print(result)


# # # # numbers = [256, 120, 2379, 135, 349, 159]

# # # # result = []

# # # # for i in numbers:
# # # #     if not ((str(i).startswith("1") or str(i).startswith("2")) and (str(i).endswith("0") or str(i).endswith("9"))):
# # # #         result.append(i)
# # # # print(result)




# # # # numbers = [3587, 2454, 19305, 17, 33, 42, 427, 317]
# # # # numbers_sums = []
# # # # for number in numbers:
    









# # # # numbers = [25, 7, 12, 58, 35, 33, 24, 14, 3, 10, 9, 11, 23, 31]
# # # # prime_numbers = []

# # # # for num in numbers:
# # # #     if num > 1:
# # # #         for i in range(2, num):
# # # #             if (num % i) == 0:
# # # #                 break
# # # #         else:
# # # #             prime_numbers.append(num)

# # # # print(prime_numbers)








# # # name_list = ['Ferid', 'Rufet', 'Zuleyxa', 'Cavad', 'Cavad', 'Zuleyxa', 'Senan', 'Rufet', 'Cavad', 'Rufet', 'Elvin', 'Reshad']
# # # # name_counts = {}

# # # # for name in name_list:
# # # #     if name in name_counts:
# # # #         name_counts[name] += 1
# # # #     else:
# # # #         name_counts[name] = 1

# # # # result = [f'{name}: {count}' for name, count in name_counts.items()]

# # # # print(result)
# # # name_counts = []

# # # for name in name_list:
# # #      name_list.count
    

# # #     name_list.count






# # # # numbers = [256, 35, 14, 48, 49, 57, 57, 65, 256, 65, 48, 2, 3, 14, 54, 56, 56, 349]

# # # # unique_numbers = list(set(numbers))


















# # # user = {
# # #     'name': 'Elnur',
# # #     'height': 179,
# # #     'phone': {
# # #         'model': 'Iphone',
# # #     },
# # #     'orders': ['book', 'mouse', 'mousepad']
# # # }

# # # user['height'] += 1



# # # user['phone']['model'] = 'Samsung'



# # # del user['name']



# # # del user['orders'][0]


# # # user['orders'].insert(0, "ball")



# # # user['orders'].append('headphones')



# # # print(user)










# # # numbers = [2384, 12385, 13226, 653, 12362423]
# # # number_dict = {}

# # # for number in numbers:
# # #     digit_count = len(str(number))
# # #     number_dict[number] = digit_count

# # # print(number_dict)




# # # user_info = {
# # #     'firstname': 'Elvin',
# # #     'lastname': 'Huseynov',
# # #     'username': 'elivin_h_ov',
# # #     'password': '12345',
# # #     'birthday': '19-08-1997'
# # # }

# # # new_info =  "firstname Elcin, username elchina, birthday 18-08-2000"

# # # new_info_splited = new_info.split()
# # # print(new_info_splited)








# # # numbers = [58, -78, 96, -33, -25, 29, 12, 46]

# # # new_numbers = {}

# # # for i in numbers:
# # #     if i > 0:
# # #         new_numbers[i] = "musbet"
# # #     else:
# # #         new_numbers[i] = "menfi"
# # # print(new_numbers)









# # # shop = {
# # #         "t-shirt" : 59.00,
# # # 		"jeans" : 75.00,
# # # 		"sweatshirt" : 60.00, 
# # # 		"shoe" : 124.99, 
# # # 		"jacket" : 154.90}
		

# # # product = input("mehsulun adini daxil edin")

# # # if product not in shop.keys():
# # #     print(None)
# # # else:
# # #     print(shop[product])














# # users = [
# #     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
# #     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
# #     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# # ]


# # username = input("İstifadəçi adını daxil edin: ")

# # found_user = None
# # for user in users:
# #     if user['username'] == username:
# #         found_user = user
    
# # if not found_user:
# #     print("bele istifadeci yoxdur")
# #     exit()

# # password = input("Şifrəni daxil edin: ")

# # if password == found_user["password"]:
# #     if found_user["blocked"] == False:
# #         print("daxil oldudunuz" ,found_user["name"] )  
# #     else:
# #         print("siz blok olunmusuz")
# # else:
# #     print("yanlis sifre")

# # if found_user:
# #     if found_user['blocked']:
# #         print("Siz daxil ola bilməzsiniz")
# #     elif found_user['password'] == password:
# #         print(f"{found_user['name']}, giriş etdiniz")
# #     else:
# #         print("Şifrəniz yanlışdır")
# # else:
# #     print("Belə bir istifadəçi yoxdur")









# # def cat_age(human_age):
# #     if human_age == 1:
# #         cat_age = 15
# #     elif human_age == 2:
# #         cat_age = 24
# #     else:
# #         cat_age = 24 + (human_age - 2) * 4
# #     return cat_age

# # age = int(input("İnsan yaşını daxil edin: "))


# # print(cat_age(age))














    

# # # mehsullar = [["Samsung A7", 55], ["Iphone 5"], ["Xiaomi 5879", 158], ["Iphone 13", 98], ["Iphone 14", 0]]

# # # products = {}

# # # for i in mehsullar:
# # #     if len(i) != 2:
# # #         products[i[0]] = None
# # #     else:
# # #         products[i[0]] = i[1]
# # # print(products)















# # # def create_hashtag(string):
# # #     conversion_dict = {
# # #         'ı': 'i', 'ö': 'o', 'ü': 'u', 'ə': 'e', 'ğ': 'g', 'ç': 'c', 'ş': 's',
# # #         'I': 'i', 'Ö': 'o', 'Ü': 'u', 'Ə': 'e', 'Ğ': 'g', 'Ç': 'c', 'Ş': 's'
# # #     }

# # #     converted_string = ''.join(conversion_dict.get(char, char) for char in string.lower().replace(' ', ''))

# # #     hashtag = '#' + converted_string.capitalize()

# # #     return hashtag


# # # string = 'İnsan hüquqları və gender bərabərliyi'
# # # hashtag = create_hashtag(string)
# # # print(hashtag)  



























# # employees = {
# #     'Ali Aliyev': {
# #         'position': 'front-end developer',
# #         'salary': '1800 AZN',
# #         'work experience': '2 years', 
# #         'working hours': 30
# #     },
# #     'Gunel Rzayeva': {
# #         'position': 'front-end developer',
# #         'salary': '900 AZN',
# #         'work experience': '3 months', 
# #         'working hours': 25 
# #     },
# #     'Nargiz Mahmudova': {
# #         'position': 'back-end developer',
# #         'salary': '2300 AZN',
# #         'work experience': '3 years', 
# #         'working hours': 40
# #     },
# #     'Ruslan Aghayev': {
# #         'position': 'back-end developer',
# #         'salary': '2000 AZN',
# #         'work experience': '2 years', 
# #         'working hours': 40
# #     },
# #     'Aslan Mammadov': {
# #         'position': 'UI/UX designer',
# #         'salary': '800 AZN',
# #         'work experience': '6 months', 
# #         'working hours': 30
# #     },
# #     'Rena Qasimova': {
# #         'position': 'UI/UX designer',
# #         'salary': '1100 AZN',
# #         'work experience': '1 years', 
# #         'working hours': 30
# #     }
# # }


# # # for employee, details in employees.items():
# # #     if details['position'] == 'front-end developer':
# # #         details['working hours'] += 5


# # # for employee, details in employees.items():
# # #     if 'years' in details['work experience']:
# # #         experience_years = int(details['work experience'].split()[0])
# # #         if experience_years >= 2:
# # #             salary = float(details['salary'].split()[0])
# # #             details['salary'] = f"{salary * 1.1:.2f} AZN"

# # # # Back-end developerların maaşını 12% artırm
# # # for employee, details in employees.items():
# # #     if details['position'] == 'back-end developer':
# # #         salary = float(details['salary'].split()[0])
# # #         details['salary'] = f"{salary * 1.12:.2f} AZN"

# # # # İ 5% artırma
# # # for employee, details in employees.items():
# # #     if 'years' in details['work experience']:
# # #         experience_years = int(details['work experience'].split()[0])
# # #         if experience_years >= 1 and details['position'] == 'UI/UX designer':
# # #             salary = float(details['salary'].split()[0])
# # #             details['salary'] = f"{salary * 1.05:.2f} AZN"


# # # developers = [employee for employee, details in employees.items() if 'developer' in details['position']]
# # # average_salary = sum(float(details['salary'].split()[0]) for employee, details in employees.items() if employee in developers) / len(developers)

# # result = {
# #     'employees': developers,
# #     'average_salary': average_salary
# # }

# # print(result)

















# # # # info = ["Resul", "Serifov", 35]
    
# # # # name, surname, age = info
# # # # name_surname = name + "  " + surname
# # # # age -= 10
# # # # new_info = [name_surname , age]
# # # # print(new_info)



# # # # numbers = [2384, 12385, 13226, 653, 12362423]

# # # # new_number = {i: len(str(i)) for i in numbers}
# # # # print(new_number)








# # # def salam_repeated(phrase):
# # #     parts = phrase.split()
# # #     if len(parts) != 2:
# # #         return "Düzgün formatda daxil edin. Əsasən 'n salam' şəklində olmalıdır."

# # #     try:
# # #         repeat_count = int(parts[0])
# # #         word = parts[1]
# # #         separator = parts[2]
# # #     except ValueError:
# # #         return "Rəqəm olmalıdır."

# # #     if repeat_count <= 0:
# # #         return "Ədəd müvafiq deyil. Ən azı 1 olmalıdır."

# # #     result = (word + separator) * repeat_count
# # #     return result.strip(separator)

# # # input_str = input("Ədədi daxil edin (n salam): ")
# # # output = salam_repeated(input_str)
# # # print(output)








# # # result_list = [num * 3 for num in range(-100, 101) if num % 7 == 0 and num != 0]
# # # print(result_list)











# # # def calculate_sum(x):
# # #     if x <= 0:
# # #         return "Ədəd pozitiv və böyük olmalıdır."
# # #     total_sum = 0
# # #     for i in range(x):
# # #         total_sum += 1 / (1 + 3 * i)
      
# # #     # total_sum = sum(1 / (1 + 3 * i) for i in range(x))
# # #     return total_sum

# # # user_input = int(input("Ədəd daxil edin: "))
# # # result = calculate_sum(user_input)
# # # print(result)














# # # def calculate_sum(x):
# # #     if x <= 0:
# # #         return "Ədəd pozitiv və böyük olmalıdır."

# # #     total_sum = 0
# # #     denominator = 1

# # #     for i in range(x):
# # #         total_sum += 1 / denominator
# # #         denominator += 3

# # #     return total_sum

# # # user_input = int(input("Ədəd daxil edin: "))
# # # result = calculate_sum(user_input)
# # # print(result)





# # def ters_cevir(number):
   
# #     num_str = str(number)
   
# #     num_ters_str = num_str[::-1]

# #     return int(num_ters_str)



# # x = 124
# # y = 651

# # x_ters = ters_cevir(x)
# # y_ters = ters_cevir(y)

# # print("x_ters:", x_ters)
# # print("y_ters:", y_ters)


# # cem = x_ters + y_ters
# # print("Cəm:", cem)

# # if int(str(cem)[0]) % 2 != 0:
# #     print( int(str(cem)[1:]))
# # else:
# #     print(cem*2)  



# # number_floor = round(256.91872, 2)

# # number_ceil = round(2456.91872, -2)

# # print("Nöqtədən sonrakı 2-ci ədədə qədər aşağı yuvarlaqlaşdırma:", number_floor)
# # print("Nöqtədən sonrakı 2-ci ədədə qədər yuxarı yuvarlaqlaşdırma:", number_ceil)








# def print_numbers():
#     for num in range(1, 101 , ):
#         if num % 3 == 1 and num % 5 == 4:
#             print(num, end=", ")

# print_numbers()






# def generate_numbers(num, rep):
#     numbers = []
#     current_number = num

#     for i in range(rep):
#         numbers.append(current_number)
#         current_number = current_number * 10 + num

#     return numbers

# def calculate_and_print():
#     try:
#         num = int(input("Zəhmət olmasa bir ədəd daxil edin: "))
#         rep = int(input("Zəhmət olmasa bir rəqəm daxil edin: "))

#         numbers = generate_numbers(num, rep)
#         result = sum(numbers)
        
#         print(" + ".join(map(str, numbers)), f"= {result}")
#     except ValueError:
#         print("Xəta! Ədəd və rəqəm yalnız tam ədədlərdən ibarət olmalıdır.")

# calculate_and_print()

# def check_user_id(user_id):
#     if len(user_id) == 10:
#         country_code = user_id[:3]
#         numeric_part = user_id[3:]
#         if country_code.isupper() and country_code.isalpha() and numeric_part.isdigit():
#             return True
#     return False

# sample_user_id = input("İstifadəçi ID nömrəsini daxil edin: ")

# # if check_user_id(sample_user_id):
# #     print("Daxil etdiyiniz ID nömrəsi tələblərə uyğundur.")
# # else:
# #     print("Daxil etdiyiniz ID nömrəsi tələblərə uyğun deyil.")



# if len(sample_user_id) == 10:
#     if sample_user_id[:3].isalpha():
#         if sample_user_id[:3].isupper():
#             if sample_user_id[:3].isascii():
#                 if sample_user_id[3:].isnumeric():
#                     print("Daxil etdiyiniz ID nömrəsi tələblərə uyğundur.")
#                 else:
#                     print("son yeddi simvol yanliz reqemlerden ibaret olmalidir")
#             else:
#                 print("yalniz ingiliz herfleri")
#         else:
#             print("boyuk herflerden ibaret olmalidir")
#     else:
#         print("ilk uc simvol herflerden ibaret olmaalidir")
# else:
#     print("simvollarin sayi 10-a beraber olmalidir")




# dictionary = {
#   'ə': 'e',
#   'ı': 'i',
#   'ö': 'o',
#   'ü': 'u',
#   'ş': 's',
#   'ç': 'c',
#   'ğ': 'g'
# }

# result_list = list(dictionary.items())
# print(result_list)







# ürünler = (("Samsung A7", 55), ("Iphone 5",), ("Xiaomi 5879", 158), ("Iphone 13", 98), ("Iphone 14", 0))


# urunler_bos = {}

# for i in ürünler:
#     if len(i) == 2:
#         urunler_bos[i[0]] = i[1]
#     elif len(i) == 1:
#         urunler_bos[i[0]] = None
# print(urunler_bos)
