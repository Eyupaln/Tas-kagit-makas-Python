import random
print("Taş , Kağıt , Makas OYUNUNA HOŞGELDİNİZ ")
oyuncuSkor=0
bilgisayarskor=0
turSayisi = int(input("Kaç Tur oynamak istiyorsunuz :"))

tas = "taş 1 "
kagit = "kagit 2"
makas="makas 3 "




for tur in range(turSayisi):
    print(f"\nTur {tur+1}")
    print("Lütfen Seçiminizi yapın :")
    print(tas)
    print(kagit)
    print(makas)

    oyuncuSecimi = input("Değer giriniz :")
    bilgisayar = random.choice(["1", "2", "3"])

    match oyuncuSecimi:
        case "1":
            match bilgisayar:
                case "1":
                    print("Bilgisayar Taşı Seçti  ")
                    print("Berabere")

                    bilgisayarskor +=1
                    oyuncuSkor+=1
                case "2":
                    print("Bilgisayar Kağıtı Seçti ")
                    print("Bilgisayar Kazandı")

                    bilgisayarskor+=1
                case "3":
                    print("Bilgisayar Makası Seçti")
                    print("Sen Kazandın")

                    oyuncuSkor+=1
        case "2":
            match bilgisayar:
                case "1":
                    print("Bilgisayar Taşı Seçti  ")
                    print("Sen Kazandın")

                    oyuncuSkor+=1
                case "2":
                    print("Bilgisayar Kağıtı Seçti  ")
                    print("Berabere")

                case "3":
                    print("Bilgisayar Makası Seçti  ")
                    print("Bilgisayar kazandı")

                    bilgisayarskor+=1
        case "3":
            match bilgisayar:
                case "1":
                    print("Bilgisayar Taşı Seçti  ")
                    print("Bilgisayar Kazandı ")

                    bilgisayarskor+=1
                case "2":
                    print("Bilgisayar Kağıtı Seçti  ")
                    print("Sen Kazandın ")

                    oyuncuSkor+=1
                case "3":
                    print("Bilgisayar Makası Seçti  ")
                    print("Berabere")


        case _:
            print("Geçersiz değer girdiniz!")

    if oyuncuSkor > bilgisayarskor:
        print("Oyuncu Skoru:", oyuncuSkor, "bilgisayar skor : ", bilgisayarskor)
        print("Oyuncu kazandı")
    elif oyuncuSkor < bilgisayarskor:
        print("bilgisayar Skoru:", bilgisayarskor, "oyuncu Skor :", oyuncuSkor)
        print("Bilgisayar Kazandı")