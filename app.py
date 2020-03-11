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


# vezirin çarprazlarının listesi bulur
def get_cross_list(x, y):
    def right_top(a, b): return {x: a+1, y: b+1}
    def left_top(a, b): return {x: a-1, y: b+1}
    def right_bottom(a, b): return {x: a+1, y: b-1}
    def left_bottom(a, b): return {x: a-1, y: b-1}

    check_list = {}

    # TODO çakışmları kümeye ekle sonrasında cevap olarak kümeyi döndür

    return check_list


# kontrol fonksiyonları

# yatayda kontrol et


def horizantal_check(arr):
    count = 0
    for index in range(len(arr) - 1):
        print("index", index)
        for t in range(index + 1, len(arr)):
            print("t: ", t)
            if(arr[index] == arr[t]):
                count = count + 1
    return count

# dikeyde kontrol edilebilmesi için matris kullanışmış olması lazım. Bizim problemimizde bununla ilgilenmiyoruz. Vezirleri sütunlara dağıtıldığı varsayılıyor


def vertical_check():
    return 0


def cross_check(arr):

    for x in range(len(arr)):
        c_check_list = get_cross_list(x, arr[x])

    return len(c_check_list)
