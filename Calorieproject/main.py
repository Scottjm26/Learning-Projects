from tkinter import *


def calculate():
    protein = protein_entry.get()
    carbs = carb_entry.get()
    fats = fats_entry.get()
    item = item_entry.get()

    protein_calories = int(protein) * 4
    carb_calories = int(carbs) * 4
    fats_calories = int(fats) * 9
    calories = protein_calories + carb_calories + fats_calories
    calorie_label2 = Label(canvas, text=f"{calories}", width=13, font=("Arial", 20), bg="#f2f6f7")
    canvas.create_window(227, 75, anchor="nw", window=calorie_label2)
    with open("data.txt", mode="a") as file:
        file.write(f"{item}|{calories}|{protein}|{carbs}|{fats}\n")


window = Tk()
window.title("Macronutrient Calculator")
window.minsize(width=200, height=200)
# window.config(padx=50, pady=50)

canvas = Canvas(width=500, height=500)
background_img = PhotoImage(file="brooke-lark-08bOYnH_r_E-unsplash.png")
canvas.create_image(0, 0, image=background_img, anchor="nw")
canvas.pack(fill="both", expand=True)

# buttons
add_button = Button(canvas, text="Calculate", width=10, command=calculate)
canvas.create_window(350, 400, anchor="nw", window=add_button)

# Entries
item_entry = Entry(canvas, width=13)
canvas.create_window(350, 200, anchor="nw", window=item_entry)
item_entry.focus()
fats_entry = Entry(canvas, width=13)
canvas.create_window(350, 250, anchor="nw", window=fats_entry)
fats_entry.insert(0, f"{0}")
carb_entry = Entry(canvas, width=13)
canvas.create_window(350, 300, anchor="nw", window=carb_entry)
carb_entry.insert(0, f"{0}")
protein_entry = Entry(canvas, width=13)
canvas.create_window(350, 350, anchor="nw", window=protein_entry)
protein_entry.insert(0, f"{0}")

# Labels
item = Label(canvas, text="Item", width=13, font=("Arial", 14), bg="#f2f6f7")
canvas.create_window(315, 175, anchor="nw", window=item)
calorie_label2 = Label(canvas, text="0000", width=13, font=("Arial", 20), bg="#f2f6f7")
canvas.create_window(227, 75, anchor="nw", window=calorie_label2)
calorie_label = Label(canvas, text="Calories", width=13, font=("Arial", 20), bg="#f2f6f7")
canvas.create_window(210, 25, anchor="nw", window=calorie_label)
protein_label = Label(canvas, text="Protein", width=13, bg="#f2f6f7")
canvas.create_window(320, 325, anchor="nw", window=protein_label)
carb_label = Label(canvas, text="Carbs", width=13, bg="#f2f6f7")
canvas.create_window(316, 275, anchor="nw", window=carb_label)
fats_label = Label(canvas, text="Fats", width=13, bg="#f2f6f7")
canvas.create_window(313, 225, anchor="nw", window=fats_label)

window.mainloop()
