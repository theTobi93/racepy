from tkinter import *
import json
import googlemaps as gm

#key : AIzaSyAQetGa5tmV2s0qNzJ3WcTWadqy_Q80OL8
gmaps = gm.Client(key='AIzaSyAQetGa5tmV2s0qNzJ3WcTWadqy_Q80OL8')

geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result)


breakpoint()
# Öffne bei betätigen des Buttons ein neues Fenster
def open_next():
    # altes Fenster schließen
    fenster.destroy()

    # neues Fenster öffnen
    fenster2 = Tk()
    fenster2.title("Next Window")
    fenster2.mainloop()


# neues Ticket erstellen
def open_new_ticket():
    # neues Fenster öffnen
    ticket = Tk()
    ticket.title("Neues Ticket")

    # Untertitel
    under_label = Label(ticket)

    # Entrys:
    name_entry = Entry(ticket, bd=5, width = 20)
    length_entry = Entry(ticket, bd=5, width = 20)
    hm_entry = Entry(ticket, bd=5, width=20)

    # Anweisungen:
    name_label = Label(ticket, text="Name:")
    length_label = Label(ticket, text = "Länge in km:")
    hm_label = Label(ticket, text="Höhenmeter")


    def save_ticket():

        # Eingaben nehmen
        name = name_entry.get()
        length = length_entry.get()
        hm = hm_entry.get()




        if len(name) == 0 or len(length) == 0 or len(hm) == 0:
           under_label.config(text="Gib zuerst die Daten ein.")
        else:
            ticket_dic = {"name": name, "length": length, "hm": hm}

            file_out = open(".\/Tickets/" + name + ".json", 'w')
            json.dump(ticket_dic, file_out)
            file_out.close()
            ticket.destroy()

    # Buttons
    save_button = Button(ticket, text="Speichern", command=save_ticket)

    # Positionen:
    name_entry.grid(row=0, column= 1)
    name_label.grid(row=0, column = 0)
    length_entry.grid(row = 1, column= 1)
    length_label.grid(row = 1, column =0)
    hm_entry.grid(row=2, column=1)
    hm_label.grid(row=2, column=0)
    save_button.grid(row=3, column=2)
    under_label.grid(row=4, column=0, columnspan=2)

    ticket.mainloop()

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button Klick me anklickt
def button_action():
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        welcome_label.config(text="Gib zuerst einen Namen ein.")
    else:
        entry_text = "Welcome " + entry_text + "!"
        welcome_label.config(text=entry_text)

fenster = Tk()
fenster.title("Ich warte auf eine Eingabe von dir.")

# Anweisungs-Label
my_label = Label(fenster, text="Gib deinen Namen ein: ")

# In diesem Label wird nach dem Klick auf den Button der Benutzer
# mit seinem eingegebenen Namen begrüsst.
welcome_label = Label(fenster)

# Hier kann der Benutzer eine Eingabe machen
eingabefeld = Entry(fenster, bd=5, width=100)

welcom_button = Button(fenster, text="Klick me", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)
next_button = Button(fenster, text="Weiter", command=open_next)
new_ticket = Button(fenster, text="Neues Ticket", command=open_new_ticket)


# Nun fügen wir die Komponenten unserem Fenster hinzu
my_label.grid(row = 0, column = 0)
eingabefeld.grid(row = 0, column = 1)
welcom_button.grid(row = 1, column = 0)
exit_button.grid(row = 1, column = 1)
next_button.grid(row=2, column=0)
new_ticket.grid(row=2, column=2)
welcome_label.grid(row = 2, column = 0, columnspan = 2)

mainloop()