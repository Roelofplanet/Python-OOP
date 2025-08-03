import random

class Bankrekening():
    def __init__ (self, saldo):
        self.rekeningnummer = self.genereer_rekeningnummer()
        self.saldo = saldo

    def genereer_rekeningnummer(self):
        return str(random.randint(1000000000, 9999999999))


    def geld_storten(self, stort_bedrag:float):
        self.saldo += stort_bedrag
        print(f'Een bedrag van € {stort_bedrag:.2f} is toegevoegd aan uw rekening {self.rekeningnummer}. Uw saldo is € {self.saldo:.2f}')

    def geld_opnemen(self, opneem_bedrag:float):
        if self.saldo >= opneem_bedrag:
            self.saldo -= opneem_bedrag
            print(f'Een bedrag van € {opneem_bedrag:.2f} is afgeschreven van uw rekening {self.rekeningnummer}. Uw saldo is € {self.saldo:.2f}')
        else:
            print(f"Uw saldo voor rekeningnummer {self.rekeningnummer} is onvoldoende. Uw saldo is € {self.saldo:.2f}")
    
    def saldo_opvragen(self):
        print(f'Uw saldo voor rekeningnummer {self.rekeningnummer} is € {self.saldo:.2f}')

mijn_rekening = Bankrekening(0)


def main():

    while True:
        print("\n  ----- Bank Systeem ----- ")
        print("1. Storten")
        print("2. Opnemen")
        print("3. Saldo")
        print("4. Exit")

        optie = input("\n Kies een optie: ").strip()

        if optie == '1':
            try:
                bedrag = float(input("Welk bedrag wilt u storten?: "))
                mijn_rekening.geld_storten(bedrag)
            except ValueError:
                print("Ongeldige invoer. Voer een geldig getal in.")

        elif optie == '2':
            try:
                bedrag = float(input("Welk bedrag wilt u opnemen?: "))
                mijn_rekening.geld_opnemen(bedrag)
            except ValueError:
                print("Ongeldige invoer. Voer een geldig getal in.")

        elif optie == '3':
            mijn_rekening.saldo_opvragen()
        
        elif optie == '4':
            print("Het programma wordt afgesloten.")
            break
        
        else:
            print("Verkeerde keuze, kies 1 - 4")
         

if __name__ == "__main__":
    main()


