# öğrenci puanlarının en düşük 2. puana sahip olanların isimlerini alfabetik sıralama
if __name__ == '__main__':
    class student():
        def __init__(self,name,score):
            self.name = name
            self.score = score
    liste = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        liste.append(student(name,score))
    
    hold = 10000
    for i in liste:
        if i.score <= hold:
            hold = i.score
    listeson = []
    for i in liste:
        if i.score != hold:
            listeson.append(i)
    
    hold = 10000
    for i in listeson:
        if i.score <= hold:
            hold = i.score
    
    liste1 = []
    for i in liste:
        if i.score == hold:
            liste1.append(i.name)
    liste1.sort()
    for i in range(len(liste1)):
        print(liste1[i])

   
