print("Merhaba, Django girls")
if 3 > 2:
    print('çalışıyor!')
if 5 > 2:
    print("5 gerçekten de 2'den büyüktür")
else:
    print("5 2'den gerçekten büyük değildir")
name = "Gözde"
if name == "Ayşe":
    print("selam Ayşe")
elif name == "ırmak":
    print("selam Irmak")
else:
    print("selam yabancı")
volume = 57
if volume < 20:
    print("çok sessiz")
elif 20 <= volume < 40:
    print("çok iyi")
elif 40 <= volume < 60:
    print("her notayı duyabiliyorum")
elif 60 <= volume < 100:
    print("parti başlasın")
else:
    print("kulaklarım ağrıyor")
#Çok yüksek ya da çok düşük olduğunda ses seviyesini değiştirme
def hi():
    print("merhaba")
    print("nasılsın")
hi()
def hi(name):
    if name == "Ayşe":
       print("merhaba ayşe")
    elif name == "Irmak":
        print("merhaba ırmak")
    else:
        print("merhaba yabancı")
hi("ayşe")
def hi(name):
    print("merhaba" + name + "!")
hi("Ayşe")
girls = {"seda", "gül", "pınar", "ayşe", "sen"}
for name in girls:
    hi(name)
    print("sıradaki kız")
for i in range(1,6):
    print(i)
