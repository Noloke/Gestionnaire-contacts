import json
import os

# ----------- Données -----------
CONTACTS_FILE = "contacts.json"

# Charger les contacts
if os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, "r") as f:
        try:
            contacts = json.load(f)
        except json.JSONDecodeError:
            contacts = []



def sauvegarder():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)


def ajouter_contact(nom, tel, mail) :
    for c in contacts :
        if tel == c['téléphone'] :
            print("Contact déjà enregistré.")
            return
    contacts.append({"nom": nom, "téléphone": tel, "email": mail})
    print("Contact enregistré.")
    sauvegarder()


def afficher_contacts() :
    if not contacts :
        print("Aucun contact.")
    else :
        for c in contacts :
             print(f"{c['nom']} - {c['téléphone']} - {c['email']}")


def rechercher_contact(nom) :
    for c in contacts :
        if nom.lower() == c['nom'].lower() :
            print(f"{c['nom']} - {c['téléphone']} - {c['email']}")
            return
    print("Contact introuvable.")


def supprimer_contact(nom) :
    avant = len(contacts)
    contacts[:] = [c for c in contacts if c['nom'].lower() != nom.lower()]
    if len(contacts) < avant :
        sauvegarder()
        print("Contact supprimé.")
    else :
        print("Contact introuvable.")



def reinitialiser_contacts() :
    choix = input("êtes-vous sure ? (oui/non)")
    if choix == "oui" :
        contacts.clear()
        sauvegarder()
        print("Contacts réinitialisé.")
        return
    elif choix == "non" :
        return
    else :
        print("Erreur")

# ----------- Menu principal -----------


def menu() :
    while True :
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Réinitialiser tous les contacts")
        print("6. Quitter")
        choix = input("Que souhaitez vous faire ?")
        if choix == '1' :
            nom = input("Nom ?")
            tel = input("Numéro de téléphone ?")
            mail = input("Adresse email ?")
            ajouter_contact(nom, tel, mail)
        elif choix == '2' :
            afficher_contacts()
        elif choix == '3' :
            nom = input("Quel contact souhaitez vous rechercher ?")
            rechercher_contact(nom)
        elif choix == '4' :
            nom = input("Quel contactc souhaitez vous supprimer ?")
            supprimer_contact(nom)
        elif choix == '5' :
            reinitialiser_contacts()
        elif choix == '6' :
            print("Au revoir.")
            break
        else :
            print("Choix invalide.")


if __name__ == "__main__":
    menu()


