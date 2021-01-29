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
def horizontal_check(arr):
    """
    params: 
        arr: [int]
    yatayda bulunan çakışma saıyısını döndürür.
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
    params:
        arr: [int]
    çaprazda bulunan çakışma sayısını döndürür.
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
    params:
        arr: [int]
    min hamlelerin listesini döndürür. çıktı listesi içerisinde bulunanan dictionary örneği:
    [{ 
        "x": 0, 
        "y": 0,
        "cost" : 12
    }] -> ifade olarak x ve y koordinatları 0,0 noktasına vezir çekilirse toplamda 12 çakışma olacağını belirtir.
    """

    # bütün hamlelerin listesi
    # min_list = []

    # min maliyete sahip olanlar burada
    min_cost_list = []
    # min_cost = False
    for x_cor in range(MAX_X_CORD):
        temp_list = []
        check_array = arr[:]
        for y_cor in range(MAX_Y_CORD):
            check_array[x_cor] = y_cor
            # print("c: " ,check_array)
            cost = horizontal_check(check_array) + cross_check(check_array)
            temp_list.append(cost)
            if(len(min_cost_list) > 0 and cost == min_cost_list[0]["cost"] and arr[x_cor] != y_cor):
                min_cost_list.append({"x": x_cor, "y": y_cor, "cost": cost})
            if((len(min_cost_list) == 0 or cost < min_cost_list[0]["cost"]) and arr[x_cor] != y_cor):
                min_cost_list = [{"x": x_cor, "y": y_cor, "cost": cost}]
        # min_list.append(temp_list)

    # pprint(min_list)
    return min_cost_list

# random restart x koordinati kadar ve y koordinat değer aralığında (0 ile arasında kalan, 0 dahil) değerler dizisi döndürür.


def random_pos_generator():
    """
    random olarak MAX_X_CORD ve MAX_Y_CORD dikkate alarak değerler dizisi döndürür.
    """
    import random
    def random_in_range(): return random.randint(0, MAX_Y_CORD - 1)
    return [random_in_range() for x in range(MAX_X_CORD)]


# local optima durumunu kontrol eder
def check_local_optima(state, min_moves):
    """
    params:
        state: [int]
        min_moves: [{"x", int, "y": int, "cost": int}...]
    state'in local optimada sıkışıp sıkışmadığını döndürür.
    """
    for move in min_moves:
        if(state[move["x"]] != move["y"]):
            return False
    return True


def check_shoulder(state, min_moves):
    # try all possible moves
    check_results = []
    for move in min_moves:
        c_state = state[:]
        c_state[move["x"]] = move["y"]
        c_state_min_moves = check_min_move(c_state)
        c_state_min_moves.append(move)
        check_results.append(c_state_min_moves)

    # check the results are same or not
    for r in range(len(check_results)):
        for l in range(r + 1, len(check_results)):
            # print("cheecking for :", check_results[r], "\n", check_results[l])
            if(len(check_results[r]) != len(check_results[l])):
                return False
            pairs = zip(check_results[r], check_results[l])
            if(any(x == y for x, y in pairs)):
                return True
    return False  # there is no shoulder


# main fonksiyon
def main():
    import random
    import time

    try_results = []

    for _ in range(TRY_COUNT):
        initial_state = random_pos_generator()
        print("Initial state: ", initial_state)

        last_cost = 9999
        random_restart_count = 0
        move_count = 0
        process_time = 0
        start = time.time()
        while last_cost != 0:
            # try_results.append(initial_state)

            min_list = check_min_move(initial_state)
            if(check_local_optima(initial_state, min_list) or check_shoulder(initial_state, min_list)):
                random_restart_count = random_restart_count + 1
                initial_state = random_pos_generator()
                continue

            random_pick = random.randint(0, (len(min_list) - 1))

            initial_state[min_list[random_pick]
                          ["x"]] = min_list[random_pick]["y"]

            move_count = move_count + 1
            last_cost = min_list[0]["cost"]

        end = time.time()
        process_time = end - start
        print("Goal state:", initial_state)
        print("move_count: ", move_count, " random_restart_count: ",
              random_restart_count, " process_time: ", process_time)
        input()
        try_results.append([move_count, random_restart_count, process_time])
        # pprint(check_min_move(initial_state))
    print("Total output: ")

    means = [0 for x in try_results[0]]
    row_count = len(try_results)
    for t in range(row_count):
        for tc in range(len(try_results[t])):
            means[tc] = means[tc] + try_results[t][tc]
    
    for m in range(len(means)):
        means[m] = means[m] / row_count
    try_results.append(means)
    pprint(try_results)


# if running current
if __name__ == "__main__":
    main()
