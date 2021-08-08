import view
import model

def giris():
    view.baslangic()
    while True:
        x = input()
        if x=="1":
            view.soru()
            break
        elif x=="2":
            view.son()
            break
        else:
            print("lütfen geçerli bir sayı giriniz")

if __name__ == '__main__':
    giris()
