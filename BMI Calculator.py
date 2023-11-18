import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.geometry("300x250")


kilo_iste = tkinter.Label(text="Enter Your Weight (Kg)")
kilo_iste.pack(pady = 10)


kilo_entry = tkinter.Entry()
kilo_entry.pack()


boy_iste = tkinter.Label(text="Enter Your Height (Cm)")
boy_iste.pack(pady = 10)


boy_entry = tkinter.Entry()
boy_entry.pack()


Sonuc = tkinter.Label(text=" ")
Sonuc.pack(pady=10)

def calculator():
    try:
        kilo = float(kilo_entry.get())
        boy = float(boy_entry.get())
        bmi = kilo / (boy/100)**2
        if type(bmi) != float or 5>=bmi or bmi>=100:
            Sonuc["text"] = "Please enter your height and weight correctly!"
        elif bmi <= 16:
            Sonuc["text"] = f"Your BMI is: {bmi:.2f}SEVERE THINNESS"
        elif 16 < bmi <= 17:
            Sonuc["text"] = f"Your BMI is: {bmi:.2f}MODERATE THINNESS"
        elif 18.5 <= bmi < 17:
            Sonuc["text"] = f"Your BMI is: {bmi:.2f}MILD THINNESS"
        elif 18.5 < bmi <= 25:
            Sonuc["text"] = f"Your BMI is: {bmi:.2f}NORMAL"
        elif 25 <= bmi < 30:
            Sonuc["text"] = f"Your BMI is: {bmi:.2f}OVERWEİGHT"
        elif 30 < bmi <= 35:
            Sonuc["text"] = f"Your BMI is: {bmi:.2f}OBESE CLASS I"
        elif 35 <= bmi < 40:
            Sonuc["text"] = f"Your BMI is: {bmi:.2f}OBESE CLASS II"
        elif 40 < bmi:
            Sonuc["text"] = f"Your BMI is: {bmi:.2f}OBESE CLASS III"
    except:
        Sonuc["text"] = "Please enter your height and weight correctly!"


calculate_button = tkinter.Button(text="Calculate",command=calculator)
calculate_button.pack()

window.mainloop()