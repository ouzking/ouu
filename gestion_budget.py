import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
connection = sqlite3.connect("budget.db")
cursor = connection.cursor()
cursor.execute("create table if not exists depense(le_type text, montant numeric)")
cursor.execute("create table if not exists revenu(son_type text, montant1 numeric)")
  
def la_depense_budget():
    print("Remplissez la liste de vos dépense:")
    le_type = input("donnez le type de depense que voulez-vous ajoutée:\n")
    print(le_type)
    montant = float(input("donnez la somme de votre dépense:"))
    print(montant)
    cursor.execute("insert into depense (le_type, montant) values (?,?)", (le_type, montant))
    print("la dépense est ajoutée")
    connection.commit()
            
def le_revenu_budget():
    print("Remplissez la liste de vos revenus:")
    son_type = input("donnez le type de revenu que vous voulez ajouté:\n")
    print(son_type)
    montant1 = float(input("donnez le montant de votre revenu:"))
    print(montant1)
    cursor.execute("insert into revenu (son_type, montant1) values (?,?)",(son_type, montant1))
    print("le revenu a été consulté")
    connection.commit()
   
def ecart_budget():
    print("l'ecart que vous auriez est de")
    depense_totale= cursor.execute("SELECT * FROM depense").fetchall()
    depense_totale=sum(int(depense[1]) for depense in depense_totale)
    print("la depense totale des depenses est de :" +str(depense_totale)+"Franc(CFA)")
    revenu_total=cursor.execute("SELECT * FROM revenu").fetchall()
    revenu_total=sum(int(revenu[1]) for revenu in revenu_total)
    print("le revenu total des revenus est égale à :" +str(revenu_total)+"Franc(CFA)")  
    if revenu_total>depense_totale:
        ecart_budget=revenu_total-depense_totale
        print("l'ecart qui existe entre les revenus et les depenses est de :" +str(ecart_budget)+"Franc(CFA)")
        print("vous avez un bénéfice de :" +str(ecart_budget)+"Franc(CFA)")
    elif revenu_total==depense_totale:
        print("vous avez rien gagner ni perdre")
    else:
        print("votre depense est élèvé")  
    connection.commit()
    connection.close()
       
while True:
    choix =""
    print("       Que voulez-vous faire ?      ")
    print("                                         ")
    print("   A) Remplir votre depense      ")
    print("   B) Remplir votre revenu        ")
    print("   C) Voir l'ecart qui existe entre la dépense et le revenu")
    print("   0) quitter l'application")
    choix = input("quel est votre désire:\n")
    if choix == "A" or choix == "a":
        print("votre depense:")
        la_depense_budget()
    elif choix == "B" or choix == "b":
        print("votre revenu:")
        le_revenu_budget()
    elif choix == "C" or choix == "c":
        print("votre ecart:")
        ecart_budget()
    elif choix == "0" or choix == "o" or choix == "O":
        print("Quitter")
        exit()
    else:
        print("votre choix n'est pas reconnu" )
        
    