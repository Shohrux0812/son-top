import random as r
# son=r.sample(range(0,11),10)
# print(son)
# son1=list(map(lambda x:x,son))
# print(son1)

def son_top(n=10):
    print(f"1 dan {n} gacha son o'yladim topa olasizmi sonni kiriting")
    son = r.randint(1, n)
    taxmin=0
    while True:
        sonlar=int(input('>>>'))
        taxmin+=1
        # print(son)
        if son<sonlar:
            print(f"Men o'ylagan son {sonlar} bu sondan kichik")
        elif son>sonlar:
            print(f"Men o'ylagan son {sonlar} bu sondan katta")
        else:
            break

    print(f"Men  {taxmin} ta urunishda topdim endi men son o'ylayman siz toping" )
    return taxmin



def sones(n=10):
    input(f"Siz 1 dan {n} gacha son ichidan siz o'ylagan sondi topish uchun istalgan narsani bosing >>>")
    quyi=1
    yuqori=n
    taxminlar=0
    while True:
        taxminlar+=1
        if quyi!=yuqori:
            taxmin = r.randint(quyi, yuqori)
        else:
            taxmin=yuqori
        javob=input(f"Siz {taxmin} sondi o'yladingiz to'g'ri bo'lsa (t yoki istalgan tugmani bosing )" 
                  f"agar bu sondan katta bo'lsa (+) kichik bo'lsa (-)".lower())
        if javob=="-":
            yuqori=taxmin-1
        elif javob=="+":
            quyi=taxmin+1
        else:
            break
    print(f"Men {taxminlar} ta urunishda ")
    return taxminlar


def play(n=10):
    yana=True
    while yana:
       taxminlar_user=son_top(n)
       taxminlar_pc=sones(n)
       if taxminlar_user>taxminlar_pc:
           print('Men yutdim')
       elif taxminlar_user<taxminlar_pc:
           print('Siz yutingiz')
       else:
           print('Durang')
       yana=int(input("Yana o'ynaysizmi? ha (1)/yo'q(0):"))
    return print("GAME OVER")


print(play(5))