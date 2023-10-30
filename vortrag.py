import matplotlib.pyplot as plt
def Collatz_Algortihmus(Zahl):
    Liste = []
    Liste.append(Zahl)


    for Zahl in Liste:
        if Zahl == 1:
            return Liste
        if Zahl % 2 == 0:
            Liste.append(Zahl/2)
        if Zahl % 2 != 0:
            Liste.append(3*Zahl+1)


def add_value_label(x_list, y_list):
    for i in range(len(x_list)):
        plt.annotate(y_list[i], (i, y_list[i] / 2), ha="center")

Collatz_lst  = Collatz_Algortihmus(int(input("Natürlcihe Zahl(> 0):")))
durchführungen = [round(i) for i in range(len(Collatz_lst))]
plt.bar(durchführungen,Collatz_lst)
add_value_label(durchführungen,Collatz_lst)
plt.xlabel('durchführungen')
plt.ylabel('Zahlenwert')
plt.title('Collatz-Problem')
plt.show()
