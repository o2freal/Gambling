from customtkinter import *
import random
import string
from tkinter import messagebox

app = CTk()
app.geometry("700x600")
app.title("generateur de mot de passe")
set_appearance_mode("light")

mot_de_passe = ""

def generer_mot_de_passe():
    global mot_de_passe
    try:
        a_val = int(entry_min.get())
        b_val = int(entry_maj.get())
        c_val = int(entry_chiffres.get())
        d_val = int(entry_speciaux.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres entier dans les cases")
        return

    lettres_min = random.choices(string.ascii_lowercase, k=a_val)
    lettres_maj = random.choices(string.ascii_uppercase, k=b_val)
    chiffres = random.choices(string.digits, k=c_val)
    speciaux = random.choices(string.punctuation, k=d_val)
    liste_finale = lettres_min + lettres_maj + chiffres + speciaux
    random.shuffle(liste_finale)
    mot_de_passe = ''.join(liste_finale)
    label_resultat.configure(text="Mot de passe : " + mot_de_passe)

app.mainloop()