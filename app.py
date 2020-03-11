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

# [5, 2, 4, 7, 3, 0, 6, 1] local optima örneği

# imports
from pprint import pprint


# Y
# ↑
# 0 → → x
MAX_X_CORD = 8
MAX_Y_CORD = 8

TRY_COUNT = 20


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

    # bütün hamlelerin listesi
    # min_list = []

    # min maliyete sahip olanlar burada
    min_cost_list = []
    # TODO min değerinin her bir vezirin yanında vermek veri tekrarına yol açıyor. Daha etkin bir yol bulunabilir.
    # min_cost = False
    for x_cor in range(MAX_X_CORD):
        temp_list = []
        check_array = arr[:]
        for y_cor in range(MAX_Y_CORD):
            check_array[x_cor] = y_cor
            # print("c: " ,check_array)
            cost = horizantal_check(check_array) + cross_check(check_array)
            temp_list.append(cost)
            if(len(min_cost_list) > 0 and cost == min_cost_list[0]["cost"]):
                min_cost_list.append({"x": x_cor, "y": y_cor, "cost": cost})
            if(len(min_cost_list) == 0 or cost < min_cost_list[0]["cost"]):
                min_cost_list = [{"x": x_cor, "y": y_cor, "cost": cost}]
        # min_list.append(temp_list)
    
    # pprint(min_list)
    return min_cost_list

# random restart x koordinati kadar ve y koordinat değer aralığında (0 ile arasında kalan, 0 dahil) değerler dizisi döndürür.


def random_pos_generator():
    import random
    def random_in_range(): return random.randint(0, MAX_Y_CORD - 1)
    return [random_in_range() for x in range(MAX_X_CORD)]

# main fonksiyon


def main():
    import random

    # initial_state = random_pos_generator()
    initial_state = [5, 2, 4, 7, 3, 0, 6, 1]

    print("initial state: ", initial_state)

    try_results = []
    last_cost = 9999
    
    while last_cost != 0:
        try_results.append(initial_state)

        min_list = check_min_move(initial_state)

        random_pick = random.randint(0, len(min_list) - 1)

        initial_state[min_list[random_pick]["x"]] = min_list[random_pick]["y"]
        print(initial_state)

        last_cost = min_list[0]["cost"]

        print("last_cost: ", last_cost)

    pprint(check_min_move(initial_state))


# if running current
if __name__ == "__main__":
    main()
