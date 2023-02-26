# SKOR LİSTESİNDEKİ 2.yüksek puanı bulma
if __name__ == '__main__':
    n = int(input()) # kaç scor girdisi olduğu
    arr = map(int, input().split()) # scor listesi
    arr_list = list(arr)
    hold = arr_list[0]
    
    for i in range(n):
        if arr_list[i] > hold:
            hold = arr_list[i]
    top_hold_counter = 0
    for i in arr_list:
        if i == hold:
            top_hold_counter+=1
            
    for i in range(top_hold_counter):
        arr_list.remove(hold)
    

    hold = arr_list[0]
    for i in range(n-top_hold_counter):
        if arr_list[i] > hold:
            hold = arr_list[i] 
    
    print(hold)