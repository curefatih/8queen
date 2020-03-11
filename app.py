# hill climb -> 8 queen problem --> ref. slatylarda 79 sayfa

# taşların kontrolü için - en iyi hamleyi bulmak için

# her bir taş için hesapla
# taşın alabilececği değer için (bütün sütun için) tek tek hesapla
# taşlar => [...n] 8 elemanlı liste taşların sütunlarda konumlarını gösteriyor.
# 1. Set oluştur
# taşlar listesini sırayla dolaş
# __ çapraz
# __ yatay
# __ dikey
# __ kontrol ederek açkışma varsa Set içerisine at
# __ set eleman sayısını döndür.
# eleman sayısı en küçük olan hamleyi tut
# döngü sonunda bir sonraki hamleyi en iyi hamle ile değiştir.


# Y
# ↑
# 0 → → x
MAX_X_CORD = 8
MAX_Y_CORD = 8


# kontrol fonksiyonları

# yatayda çakışma sayısını verir
def horizantal_check(arr):
    """
    arr: [int]
    """
    count = 0
    for index in range(len(arr) - 1):
        # print("index", index)
        for t in range(index + 1, len(arr)):
            # print("t: ", t)
            if(arr[index] == arr[t]):
                count = count + 1
    return count

# dikeyde kontrol edilebilmesi için matris kullanışmış olması lazım. Bizim problemimizde bununla ilgilenmiyoruz. Vezirleri sütunlara dağıtıldığı varsayılıyor


def vertical_check():
    """
    arr: [int]
    """
    return 0

# vezirin çarprazlarının sayısını bulur


def cross_check(arr):
    """
     arr: [int]
    """
    total_conflict = 0
    # her bir sütun için kontrol ediyoruz
    for index in range(len(arr) - 1):
        for check in range(index + 1, len(arr)):
            # iki index arasındaki fark
            distance = check - index
            # print("index ", index, " - current ", check, " --- distance",
            #       distance, "---plus : ", arr[index] + distance, " eq: ", arr[check])
            if(arr[index] + distance == arr[check] or arr[index] - distance == arr[check]):
                total_conflict = total_conflict + 1  # çakışma varsa sayıyı bir artır
        # print("_______________")

    return total_conflict

# bütün hamlelerin -her sütun diğerleri değişmemiş gibi hesaplanır- çakışma sayılarını bulur
def check_min_move(arr):
     """
     arr: [int]
    """
    # arr = [...8]
    for x_cor in range(MAX_X_CORD):
        check_array = arr[:]
        for y_cor in range(MAX_Y_CORD):
            check_array[x_cor] = y_cor
            # print("c: " ,check_array)
            cost = horizantal_check(check_array) + cross_check(check_array)
            print("index", x_cor, " and current index for cost: ",
                  y_cor, " , cost: ", cost)
        print("____")

# random restart x kordinati kadar ve y koordinat değer aralığında (0 ile arasında kalan, 0 dahil) değerler dizisi döndürür.
def random_restart():
    import random
    def random_in_range(): return random.randint(0, MAX_Y_CORD - 1)
    state = [random_in_range() for x in range(MAX_X_CORD)]
    return state
    
