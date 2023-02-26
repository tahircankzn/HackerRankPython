# string için de string arama ve kaç tekrar olduğunu yazdırma
def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)-len(sub_string)+1):
        str1 =string[i]
        for a in range(1,len(sub_string)):
            str1 = str1 + string[i+a]
        print(str1)
        if str1 == sub_string:
            counter+=1
            
        
    return counter

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string ="CDC"

    
    count = count_substring(string, sub_string)
    print(count)

        
  