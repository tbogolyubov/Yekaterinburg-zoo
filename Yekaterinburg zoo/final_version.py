from tkinter import *
from tkinter import messagebox
import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

W1 = Tk()
W1.title("ЕКАТЕРИНБУРГСКИЙ ЗООПАРК")
W1.config(width=1300, height=790)
W1.resizable(False, False)
background_img = PhotoImage(file ="giraf_3.png")
L0 = Label(W1, image=background_img)
L0.place(x=0, y=0, width=1300, height=790)

but1_img = PhotoImage(file="svetloe.png")
but1_enter = PhotoImage(file="temnoe.png")
zgivotnoe = PhotoImage(file="raznoobrasie.png")
but2_img = PhotoImage(file="svetloe1.png")
but2_enter = PhotoImage(file="temnoe1.png")
but3_img = PhotoImage(file = "svetloe2.png")
but3_enter = PhotoImage(file= "temnoe2.png")
but4_img = PhotoImage(file = "svetloe33.png")
but4_enter = PhotoImage(file = "temnoe33.png")
but5_img = PhotoImage(file = "svetloe4.png")
but5_enter = PhotoImage(file = "temnoe4.png")
Karta = PhotoImage(file="Karta1_caps.png")
collage = PhotoImage(file="collage.png")
logo = PhotoImage(file = "logo_zoo_2.png")

LL = Label(W1, image = logo)
LL.place(x = 340, y = 223, width = 282, height = 304)
def but1():
    W2 = Toplevel(W1) # окно животные
    W2.title("ОБИТАТЕЛИ ЗООПАРКА")
    W2.grab_set()
    W2.resizable(False, False)
    W2.config(width=1250, height=790)
    L2 = Label(W2, image=collage)
    L2.place(x=0 , y= 160, width=1250, height=622)
    LABEL_A = ttk.Label(W2, anchor=CENTER, font=('Calibri', '20', 'bold'),
                        text='В Екатеринбургском зоопарке живёт более 1200 особей 360 видов животных со всех уголков Земли. ',
                        foreground='black', background='white')
    LABEL_A.place(x=30, y=70)
    LABEL_B = ttk.Label(W2, anchor=CENTER, font=('Calibri', '20', 'bold'),
                        text='Вот лишь некоторые из видов, с жизнью которых вы сможете ознакомиться у нас.',
                        foreground='black', background='white')
    LABEL_B.place(x=30, y=105)
    LABEL_C = ttk.Label(W2, anchor=CENTER, font=('Calibri', '24', 'bold'),
                        text='Животные зоопарка',
                        foreground='black', background='white')
    LABEL_C.place(x=30, y=10)

    W2.mainloop()

def but1_enter1(a):
    But1['image'] = but1_enter
    But1.config(activebackground='gray')
def but1_img1(a):
    But1['image'] = but1_img

But1 = Button(W1, image=but1_img, command=but1, borderwidth=0, activebackground='white')
But1.place(x=32, y=194, width=299, height=284)
But1.bind("<Enter>", but1_enter1)
But1.bind("<Leave>", but1_img1)

def but2():
    W3 = Toplevel(W1) # окно карта зоопарка
    W3.resizable(False, False)
    W3.grab_set()
    W3.title("КАРТА ЗООПАРКА")
    W3.config(width=878, height=790)
    L3 = Label(W3, image=Karta)
    L3.place(x=0, y=0, width=878, height=790)

    # ДЛЯ СЛОНА
    slon_icon = PhotoImage(file="slon_icon.png")
    slon_icon_dark = PhotoImage(file="slon_icon_dark.png")
    slon_fotka = PhotoImage(file="slon_fotka.png")

    def button_slon_enter(a):
        Button_slon['image'] = slon_icon_dark
        Button_slon.config(activebackground='white')
    def button_slon_leave(a):
        Button_slon['image'] = slon_icon
    def fotka_slona():
        Okno_slona = Toplevel(W3)
        Okno_slona.grab_set()
        Okno_slona.resizable(False, False)
        Okno_slona.title("ПАВИЛЬОН СЛОНА")
        Okno_slona.config(width=600, height=600)
        Photo_slona = Label(Okno_slona, image=slon_fotka)
        Photo_slona.place(x=0,y=0, width=600, height=600)
        Okno_slona.mainloop()

    Button_slon = Button(W3, image=slon_icon, command=fotka_slona ,borderwidth=0, activebackground='white')
    Button_slon.place(x=695, y=244, width=87, height=87)
    Button_slon.bind("<Enter>", button_slon_enter)
    Button_slon.bind("<Leave>", button_slon_leave)


    # ДЛЯ БЕГЕМОТА
    begemot_icon = PhotoImage(file="begemot_icon.png")
    begemot_icon_dark = PhotoImage(file="begemot_icon_dark.png")
    begemot_fotka = PhotoImage(file="begemot_fotka.png")

    def button_begemot_enter(a):
        Button_begemot['image'] = begemot_icon_dark
        Button_begemot.config(activebackground='white')
    def button_begemot_leave(a):
        Button_begemot['image'] = begemot_icon
    def fotka_slona():
        Okno_begemota = Toplevel(W3)
        Okno_begemota.grab_set()
        Okno_begemota.resizable(False, False)
        Okno_begemota.title('ПАВИЛЬОН "ЭКЗОТИЧЕСКИЕ ХИЩНИКИ"')
        Okno_begemota.config(width=600, height=600)
        Photo_begemota = Label(Okno_begemota, image=begemot_fotka)
        Photo_begemota.place(x=0,y=0, width=600, height=600)
        Okno_begemota.mainloop()

    Button_begemot = Button(W3, image=begemot_icon, command=fotka_slona ,borderwidth=0, activebackground='white')
    Button_begemot.place(x=609, y=158, width=88, height=87)
    Button_begemot.bind("<Enter>", button_begemot_enter)
    Button_begemot.bind("<Leave>", button_begemot_leave)


    # ДЛЯ КРОКОДИЛА
    krok_icon = PhotoImage(file="krok_icon.png")
    krok_icon_dark = PhotoImage(file="krok_icon_dark.png")
    krok_fotka = PhotoImage(file="krok_fotka.png")

    def button_krok_enter(a):
        Button_krok['image'] = krok_icon_dark
        Button_krok.config(activebackground='white')
    def button_krok_leave(a):
        Button_krok['image'] = krok_icon
    def fotka_kroka():
        Okno_kroka = Toplevel(W3)
        Okno_kroka.grab_set()
        Okno_kroka.resizable(False, False)
        Okno_kroka.title('ПАВИЛЬОН "ЭКЗОТЕРРАРИУМ"')
        Okno_kroka.config(width=600, height=600)
        Photo_kroka = Label(Okno_kroka, image=krok_fotka)
        Photo_kroka.place(x=0, y=0, width=600, height=600)
        Okno_kroka.mainloop()

    Button_krok = Button(W3, image=krok_icon, command=fotka_kroka, borderwidth=0, activebackground='white')
    Button_krok.place(x=521, y=74, width=88, height=87)
    Button_krok.bind("<Enter>", button_krok_enter)
    Button_krok.bind("<Leave>", button_krok_leave)


    # ДЛЯ ПТИЦ
    bird_icon = PhotoImage(file="bird_icon.png")
    bird_icon_dark = PhotoImage(file="bird_icon_dark.png")
    bird_fotka = PhotoImage(file="bird_fotka.png")

    def button_bird_enter(a):
        Button_bird['image'] = bird_icon_dark
        Button_bird.config(activebackground='white')
    def button_bird_leave(a):
        Button_bird['image'] = bird_icon
    def fotka_bird():
        Okno_bird = Toplevel(W3)
        Okno_bird.grab_set()
        Okno_bird.resizable(False, False)
        Okno_bird.title("КОМПЛЕКС ВОЛЬЕР ДЛЯ ХИЩНЫХ ПТИЦ")
        Okno_bird.config(width=600, height=600)
        Photo_bird = Label(Okno_bird, image=bird_fotka)
        Photo_bird.place(x=0, y=0, width=600, height=600)
        Okno_bird.mainloop()

    Button_bird = Button(W3, image=bird_icon, command=fotka_bird, borderwidth=0, activebackground='white')
    Button_bird.place(x=348, y=73, width=88, height=87)
    Button_bird.bind("<Enter>", button_bird_enter)
    Button_bird.bind("<Leave>", button_bird_leave)


    # ДЛЯ МЕДВЕДЯ
    bear_icon = PhotoImage(file="bear_icon.png")
    bear_icon_dark = PhotoImage(file="bear_icon_dark.png")
    bear_fotka = PhotoImage(file="bear_fotka.png")
    bear_fotka2 = PhotoImage(file="bear_fotka2.png")

    def button_bear_enter(a):
        Button_bear['image'] = bear_icon_dark
        Button_bear.config(activebackground='white')
    def button_bear_leave(a):
        Button_bear['image'] = bear_icon
    def fotka_bear():
        Okno_bear = Toplevel(W3)
        Okno_bear.grab_set()
        Okno_bear.resizable(False, False)
        Okno_bear.title("ВОЛЬЕРЫ МЕДВЕДЕЙ")
        Okno_bear.config(width=1200, height=600)
        Photo_bear = Label(Okno_bear, image=bear_fotka)
        Photo_bear.place(x=0, y=0, width=600, height=600)
        Photo_bear2 = Label(Okno_bear, image=bear_fotka2)
        Photo_bear2.place(x=601, y=0, width=600, height=600)
        Okno_bear.mainloop()

    Button_bear = Button(W3, image=bear_icon, command=fotka_bear, borderwidth=0, activebackground='white')
    Button_bear.place(x=522, y=673, width=88, height=87)
    Button_bear.bind("<Enter>", button_bear_enter)
    Button_bear.bind("<Leave>", button_bear_leave)


    # ДЛЯ ОБЕЗЬЯН
    monkey_icon = PhotoImage(file="monkey_icon.png")
    monkey_icon_dark = PhotoImage(file="monkey_icon_dark.png")
    monkey_fotka = PhotoImage(file="monkey_fotka.png")

    def button_monkey_enter(a):
        Button_monkey['image'] = monkey_icon_dark
        Button_monkey.config(activebackground='white')
    def button_monkey_leave(a):
        Button_monkey['image'] = monkey_icon
    def fotka_monkey():
        Okno_monkey = Toplevel(W3)
        Okno_monkey.grab_set()
        Okno_monkey.resizable(False, False)
        Okno_monkey.title("ПАВИЛЬОН ДЛЯ ОБЕЗЬЯН")
        Okno_monkey.config(width=600, height=600)
        Photo_monkey = Label(Okno_monkey, image=monkey_fotka)
        Photo_monkey.place(x=0, y=0, width=600, height=600)
        Okno_monkey.mainloop()

    Button_monkey = Button(W3, image=monkey_icon, command=fotka_monkey, borderwidth=0, activebackground='white')
    Button_monkey.place(x=610, y=589, width=88, height=88)
    Button_monkey.bind("<Enter>", button_monkey_enter)
    Button_monkey.bind("<Leave>", button_monkey_leave)


    # ДЛЯ ХИЩНИКОВ
    lion_icon = PhotoImage(file="lion_icon.png")
    lion_icon_dark = PhotoImage(file="lion_icon_dark.png")
    lion_fotka = PhotoImage(file="lion_fotka.png")
    lion_fotka2 = PhotoImage(file="lion_fotka2.png")

    def button_lion_enter(a):
        Button_lion['image'] = lion_icon_dark
        Button_lion.config(activebackground='white')
    def button_lion_leave(a):
        Button_lion['image'] = lion_icon
    def fotka_lion():
        Okno_lion = Toplevel(W3)
        Okno_lion.grab_set()
        Okno_lion.resizable(False, False)
        Okno_lion.title("ПАВИЛЬОН ДЛЯ ОБИТАТЕЛЕЙ СЕВЕРНЫХ И ЮЖНЫХ ШИРОТ")
        Okno_lion.config(width=1200, height=600)
        Photo_lion = Label(Okno_lion, image=lion_fotka)
        Photo_lion.place(x=0, y=0, width=600, height=600)
        Photo_lion2 = Label(Okno_lion, image=lion_fotka2)
        Photo_lion2.place(x=601, y=0, width=600, height=600)
        Okno_lion.mainloop()

    Button_lion = Button(W3, image=lion_icon, command=fotka_lion, borderwidth=0, activebackground='white')
    Button_lion.place(x=695, y=501, width=88, height=87)
    Button_lion.bind("<Enter>", button_lion_enter)
    Button_lion.bind("<Leave>", button_lion_leave)

    # ДЛЯ ТИГРОВ
    tiger_icon = PhotoImage(file="tiger_icon.png")
    tiger_icon_dark = PhotoImage(file="tiger_icon_dark.png")
    tiger_fotka = PhotoImage(file="tiger_fotka.png")

    def button_tiger_enter(a):
        Button_tiger['image'] = tiger_icon_dark
        Button_tiger.config(activebackground='white')

    def button_tiger_leave(a):
        Button_tiger['image'] = tiger_icon

    def fotka_tiger():
        Okno_tiger = Toplevel(W3)
        Okno_tiger.grab_set()
        Okno_tiger.resizable(False, False)
        Okno_tiger.title("ВОЛЬЕР АМУРСКИХ ТИГРОВ")
        Okno_tiger.config(width=600, height=600)
        Photo_tiger = Label(Okno_tiger, image=tiger_fotka)
        Photo_tiger.place(x=0, y=0, width=600, height=600)
        Okno_tiger.mainloop()

    Button_tiger = Button(W3, image=tiger_icon, command=fotka_tiger, borderwidth=0, activebackground='white')
    Button_tiger.place(x=89, y=503, width=88, height=88)
    Button_tiger.bind("<Enter>", button_tiger_enter)
    Button_tiger.bind("<Leave>", button_tiger_leave)

    W3.mainloop()
def but2_enter1(a):
    But2['image'] = but2_enter
    But2.config(activebackground='gray')
def but2_img2(a):
    But2['image'] = but2_img

But2 = Button(W1, image=but2_img, command=but2, borderwidth=0, activebackground='white')
But2.place(x=820, y=180, width=402, height=437)
But2.bind("<Enter>", but2_enter1)
But2.bind("<Leave>", but2_img2)

def but3_enter1(a):
    But3['image'] = but3_enter
    But3.config(activebackground='gray')
def but3_img3(a):
    But3['image'] = but3_img

def open_vk():
    webbrowser.open('https://vk.com/zooekb?ysclid=lwoves78pn806340004')
def open_yout():
    webbrowser.open('https://www.youtube.com/channel/UCAN5lzzXn2S-DLVJBE3JK3A')

def but3():
    W4 = Toplevel(W1)  # окно о нас
    W4.title("О НАС")
    W4.grab_set()
    W4.resizable(False, False)
    W4.config(width=977, height=700)

    fon_ona = PhotoImage(file="o_nas_2.png")
    L4 = Label(W4, image=fon_ona)
    L4.place(x=0, y=0, width=977, height=700)

    vvk = PhotoImage(file="vk.png")
    vk_temnee = PhotoImage(file="vk_temnee.png")
    yout = PhotoImage(file="youtube.png")
    youtube_temnee = PhotoImage(file="youtube_temnee.png")

    Butvk = Button(W4, image=vvk, command=open_vk)
    Butyout = Button(W4, image=yout, command=open_yout)

    Butvk.place(x=665, y=525, height=50, width=50)
    Butyout.place(x=735, y=525, height=50, width=76)

    def on_enter_vk(event):
        Butvk.config(image=vk_temnee)
        Butvk.config(activebackground='gray')

    def on_leave_vk(event):
        Butvk.config(image=vvk)

    def on_enter_yout(event):
        Butyout.config(image=youtube_temnee)
        Butyout.config(activebackground='gray')

    def on_leave_yout(event):
        Butyout.config(image=yout)

    Butvk.bind("<Enter>", on_enter_vk)
    Butvk.bind("<Leave>", on_leave_vk)
    Butyout.bind("<Enter>", on_enter_yout)
    Butyout.bind("<Leave>", on_leave_yout)

    W4.mainloop()

But3 = Button(W1, image=but3_img, command=but3, borderwidth=0, activebackground='white')
But3.place(x=345, y=540, width=251, height=248)
But3.bind("<Enter>", but3_enter1)
But3.bind("<Leave>", but3_img3)

def but4_enter1(a):
    But4['image'] = but4_enter
    But4.config(activebackground='gray')
def but4_img4(a):
    But4['image'] = but4_img


def but4():
    W5 = Toplevel(W1)  # окно опека
    W5.title("ОПЕКА")
    W5.grab_set()
    W5.config(width=755, height=790)
    W5.resizable(False, False)
    fon_opek = PhotoImage(file="fon_opeka_2.png")
    L5 = Label(W5, image=fon_opek)
    L5.place(x=0, y=0, width=755, height=790)

    ENTRY_1 = ttk.Entry(W5, bootstyle='primary', font=('Calibri', '20'), width=48)
    ENTRY_1.place(x=33, y=285)

    ENTRY_2 = ttk.Entry(W5, bootstyle='primary', font=('Calibri', '20'), width=48)
    ENTRY_2.place(x=35, y=414)

    TEXT_1 = ttk.Text(W5, font=('Calibri', '20'), width=48, height=4)
    TEXT_1.place(x=35, y=545)

    LABEL_11 = ttk.Label(W5, anchor=CENTER, font=('Calibri', '20', 'bold'), text='Ваше имя:',
                         foreground='white', background='black', bootstyle='dark')
    LABEL_11.place(x=28, y=230)

    LABEL_22 = ttk.Label(W5, anchor=CENTER, font=('Calibri', '20', 'bold'), text='Ваш телефон:',
                         foreground='white', background='black', bootstyle='dark')
    LABEL_22.place(x=30, y=355)

    LABEL_33 = ttk.Label(W5, anchor=CENTER, font=('Calibri', '20', 'bold'), text='Комментарий к обращению:',
                         foreground='white', background='black', bootstyle='dark')
    LABEL_33.place(x=30, y=485)

    def b1():
        answ1 = ENTRY_1.get().lower()
        answ2 = ENTRY_2.get().lower()
        answ3 = TEXT_1.get("1.0", ttk.END).lower()

        if not answ1 or not answ2 or not answ3:
            messagebox.showinfo("ОШИБКА", "Пожалуйста, заполните все поля")
        elif not answ2.isdigit():
            messagebox.showinfo("ОШИБКА", "Номер телефона должен состоять только из цифр")
        else:
            ENTRY_1.delete(0, 'end')
            ENTRY_2.delete(0, 'end')
            TEXT_1.delete('1.0', 'end')
            messagebox.showinfo("ОТПРАВКА СООБЩЕНИЯ", "Ваше сообщение успешно отправлено! Ожидайте обратную связь.")

    style = ttk.Style()
    style.configure('My.TButton', font=('Calibri', 20), foreground='black', background='white')
    style.map('My.TButton', foreground=[('active', 'white'), ('!active', 'black')],
              background=[('active', 'black'), ('!active', 'white')])

    B_opeka = ttk.Button(W5, text="ОТПРАВИТЬ", style='My.TButton', command=b1)
    B_opeka.place(x=35, y=715)
    W5.mainloop()

But4 = Button(W1, image=but4_img, command=but4, borderwidth=0, activebackground='white')
But4.place(x=603, y=0, width=313, height=306)
But4.bind("<Enter>", but4_enter1)
But4.bind("<Leave>", but4_img4)

def but5_enter1(a):
    But5['image'] = but5_enter
    But5.config(activebackground='gray')
def but5_img5(a):
    But5['image'] = but5_img

def but5():
    W6 = Toplevel(W1)  # окно купить билет
    W6.title("ПОКУПКА БИЛЕТОВ")
    W6.grab_set()
    W6.resizable(False, False)
    W6.geometry("750x500")

    t_main = PhotoImage(file="t_main.png")
    L_t_main = Label(W6, image=t_main).place(x=-1, y=-1)

    def open_ticket_window(ticket_type, ticket_price):
        W7 = Toplevel(W6)
        W7.title("ВЫБОР БИЛЕТОВ")  # Устанавливаем новый заголовок
        W7.grab_set()
        W7.config(width=318, height=218)

        buy_main = PhotoImage(file="buy_main.png")
        W7.buy_main_image = buy_main  # Сохраняем ссылку на изображение
        L_buy_main = Label(W7, image=buy_main).place(x=-10, y=0)

        Label(W7, text=f"Выберите количество {ticket_type} билетов:", font=("Arial", 12)).pack(pady=10)

        quantity = IntVar(value=1)
        Spinbox(W7, from_=1, to=10, textvariable=quantity, font=("Arial", 12)).pack(pady=5)

        def add_to_cart():
            num_tickets = quantity.get()
            total_price = num_tickets * ticket_price
            messagebox.showinfo("Корзина", f"Добавлено {num_tickets} {ticket_type} билетов на сумму {total_price} руб.")
            W7.destroy()  # Закрываем только текущее окно добавления билетов
            W6.lift()  # Поднимаем окно W6 на передний план

        Button(W7, text="ДОБАВИТЬ В КОРЗИНУ", command=add_to_cart, font=("Arial", 12)).pack(pady=25)

    tv = PhotoImage(file="tv.png")
    tl = PhotoImage(file="tl.png")
    td = PhotoImage(file="td.png")

    tv_clicked = PhotoImage(file="tv_c.png")
    tl_clicked = PhotoImage(file="tl_c.png")
    td_clicked = PhotoImage(file="td_c.png")

    def tv_click(a):
        tvB['image'] = tv_clicked
        tvB(activebackground='white', foreground = 'white')

    def td_click(a):
        tdB['image'] = td_clicked
        tdB.config(activebackground='white', foreground = 'white')

    def tl_click(a):
        tlB['image'] = tl_clicked
        tlB.config(activebackground='white', foreground = 'white')

    def tv_unclick(a):
        tvB['image'] = tv

    def td_unclick(a):
        tdB['image'] = td

    def tl_unclick(a):
        tlB['image'] = tl

    tvB = Button(W6, image=tv, borderwidth=0, command=lambda: open_ticket_window("взрослых", 500))
    tvB.place(x=120, y=200)
    tvB.bind("<Enter>", tv_click)
    tvB.bind("<Leave>", tv_unclick)

    tdB = Button(W6, image=td, borderwidth=0, command=lambda: open_ticket_window("детских", 300))
    tdB.place(x=325, y=200)
    tdB.bind("<Enter>", td_click)
    tdB.bind("<Leave>", td_unclick)

    tlB = Button(W6, image=tl, borderwidth=0, command=lambda: open_ticket_window("льготных", 200))
    tlB.place(x=530, y=200)
    tlB.bind("<Enter>", tl_click)
    tlB.bind("<Leave>", tl_unclick)

    W6.mainloop()

But5 = Button(W1, image=but5_img, command=but5, borderwidth=0, activebackground='white')
But5.place(x=1005, y=0, width=294, height=180)
But5.bind("<Enter>", but5_enter1)
But5.bind("<Leave>", but5_img5)

mainloop()