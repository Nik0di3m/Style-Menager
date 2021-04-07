import os 
from PIL import Image
import psutil
import pandas as pd
import time

class Product:


    def __init__(self):
        self.style = []
        self.img = []
        self.files = []
        self.procces_list = []
        self.style = []
        self.room = []


    def add_image(self):
        self.files = os.listdir("./zdjecia/")
        os.chdir("./zdjecia")

    def procList(self):
        for proc in psutil.process_iter():
            self.process_list.append(proc)

    def image_show(self, img):
        for i in img:
            if ".jpg" in i:
                
                print(i)
                im = Image.open(r"%s" %i)
                i = str(i)
                i = i.replace(".jpg", "")
                self.img.append(i)
                process_list = []
                for proc in psutil.process_iter():
                    process_list.append(proc)

                im.show()
                time.sleep(0.7)
                self.printStyleOptions()
                add_style = self.styleHandler()
                self.style.append(add_style)
                for proc in psutil.process_iter():
                    if not proc in process_list:
                        proc.kill()
                

    def make_csv(self):
        df = pd.DataFrame(list(zip(self.img, self.style)), 
               columns =['EAN', 'Style']) 
        df.to_csv('style.csv', index=False, sep=";")

    def stringConte(self,str1, str2):
        try:
            add_room = str1 + "/" + str2
            return add_room
        except:
            pass

    def styleHandler(self):
        x = input()

        style = ["",
        "Nowoczesny",
        "Klasyczny",
        "Loft"]
        try:
            return style[int(x)]
            
        except:
            pass

    def roomHandler(self):
        x = input()

        room = ["",
        "Salon/jadalnia",
        "Sypialnia",
        "Kuchnia",
        "Łazienka",
        "Przedpokój",
        "Biuro",
        "Pokój dziecięcy"]
        try:
            return room[int(x)]

        except:
            pass


    def fileExist(self):
        if os.path.isfile("./zdjecia/style.csv"):
            print("Plik style.csv istnieje uważaj!")
        else:
            pass


    def printOptions(self):
        print("""0 POMIŃ Wybierz pokój: 1.Salon/jadalnia 2.Sypialnia 3.Kuchnia 4.Łazienka 5.Przedpokój 6.Biuro 7.Pokój dziecięcy""")

    def printStyleOptions(self):
        print("""0 POMIŃ
Wybierz styl: 1.Nowoczesny 2.Klasyczny 3.Loft""")


    

def main():
    x = Product()
    if (os.path.exists("./zdjecia") != False):
        x.fileExist()
        x.add_image()
        x.image_show(x.files)
        x.make_csv()
    else:
        print("Utwórz folder zdjecia")

if __name__ == "__main__":
    main()