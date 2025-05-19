###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8


y = 3.2


z = 8j + 18


a = "Hello World"


b = True


c = 23 < 22



l = [1, 2, 3, 4,"String",3.2, False]



d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}


t = ("Machine Learning", "Data Science")



s = {"Python", "Machine Learning", "Data Science","Python"}




###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."



###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
print(len(lst))

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
print(lst[0], lst[10])

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
print(lst[0:4])

# Adım 4: Sekizinci index'teki elemanı silin.
print(lst.pop(8))

# Adım 5: Yeni bir eleman ekleyin.
print(lst.append("A"))


# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
print(lst.insert(8, "N"))

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.
print(dict.keys())

# Adım 2: Value'lara erişiniz.
print(dict.values())


# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"][1] = 13


# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict["Ahmet"] = ["Turkey",24]


# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio", None)



###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

def split_odd_even(list_):
    """
        Splits the given list of integers into odd and even numbers.

        Args:
            list_ (list): A list of integers.

        Returns:
            tuple: A tuple containing two lists:
                   - The first list contains all odd numbers.
                   - The second list contains all even numbers.
        """
    odd_numbers = [x for x in list_ if x % 2 != 0]
    even_numbers = [x for x in list_ if x % 2 == 0]
    return odd_numbers, even_numbers

odd_numbers, even_numbers = split_odd_even(l)


###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]


for i, isim in enumerate(ogrenciler[:3], start=1):
    print(f"Mühendislik Fakültesi {i}. öğrenci: {isim}")

for i, isim in enumerate(ogrenciler[-3:], start=1):
    print(f"Tıp Fakültesi {i}. öğrenci: {isim}")
###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

print("Ders Bilgileri:")
for kod, kr, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kr} olan {kod} kodlu dersin kontenjanı {kont} kişidir.")

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume_karsilastir(kume1, kume2):
    """
    İki küme karşılaştırılır ve ilişkiye göre sonuç ekrana yazdırılır.

    Eğer birinci küme (kume1), ikinci kümeyi (kume2) tamamen kapsıyorsa,
    iki kümenin ortak elemanları ekrana yazdırılır.

    Eğer birinci küme, ikinci kümeyi kapsamıyorsa,
    ikinci kümede olup birinci kümede olmayan elemanlar (fark kümesi) yazdırılır.

    Args:
        kume1 (set): Birinci küme.
        kume2 (set): İkinci küme.

    Returns:
        None: Fonksiyon sadece sonucu ekrana yazdırır, bir değer döndürmez.
    """
    if kume1.issuperset(kume2):
        print(kume1.intersection(kume2))
    else:
        print(kume2.difference(kume1))

# Örnek kullanım
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

kume_karsilastir(kume1, kume2)





