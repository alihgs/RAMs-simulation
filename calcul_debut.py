#1)


class RAM_Machine:
    def __init__(self):
        self.instructions = []
        self.registres = {}  # Dictionnaire pour stocker les valeurs des registres
        self.position = 0  # Position de l'instruction courante


# fonction pour lire RAM.txt et le mettre dans une liste d'instruction de la class RAM()
def lecture_program(file_path):
    Program = RAM_Machine()
    with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('(')
                opcode = parts[0].strip()
                operands = parts[1].split(')')[0].split(',')
                operands = [operand.strip() for operand in operands]
                instruction = [opcode, operands]
                Program.instructions.append(instruction)
    return Program


"""
le code RAM doit etre sous cette forme pour etre correctement lu
SUB(r1,1,i0)
ADD(0,0,r2)
ADD(0,1,r2)
"""

#TEST
program = lecture_program('RAM.txt')
# print('instructions : ',program.instructions)

#2)

def recherche_registre(operand, registre):
    if operand.isdigit():
        return int(operand)
        #retourne sa valeur à partir des registres
    else:
        if operand in registre:
            return registre[operand]
        else:
            registre[operand]=0
            return registre[operand]
        
    

def execution(R):
    while R.position < len(R.instructions):
        p = R.position
        if R.instructions[p][0] == 'ADD':
            print(R.instructions[p][0])
            res = recherche_registre(R.instructions[p][1][0], R.registres) + recherche_registre(R.instructions[p][1][1], R.registres) 
            R.registres[R.instructions[p][1][2]] = res
            R.position += 1
            print("instructions",R.instructions,"\nregistre:",R.registres,R.position)
        elif R.instructions[p][0] == 'SUB':
            print(R.instructions[p][0])
            res = recherche_registre(R.instructions[p][1][0], R.registres) - recherche_registre(R.instructions[p][1][1], R.registres)
            R.registres[R.instructions[p][1][2]] = res
            R.position += 1
            print("instructions",R.instructions,"\nregistre:",R.registres,R.position)
        elif R.instructions[p][0] == 'MULT':
            print(R.instructions[p][0])
            res = recherche_registre(R.instructions[p][1][0], R.registres) * recherche_registre(R.instructions[p][1][1], R.registres)
            R.registres[R.instructions[p][1][2]] = res
            R.position += 1
            print("instructions",R.instructions,"\nregistre:",R.registres,R.position)
        elif R.instructions[p][0] == 'DIV':
            print(R.instructions[p][0])
            res = recherche_registre(R.instructions[p][1][0], R.registres) // recherche_registre(R.instructions[p][1][1], R.registres)
            R.registres[R.instructions[p][1][2]] = res
            R.position += 1
            print("instructions",R.instructions,"\nregistre:",R.registres,R.position)
        elif R.instructions[p][0] == 'JUMP':
            print(R.instructions[p][0])
            R.position += int(R.instructions[p][1][0])
            print("instructions",R.instructions,"\nregistre:",R.registres,R.position)
        elif R.instructions[p][0] == 'JE':
            print(R.instructions[p][0])
            if recherche_registre(R.instructions[p][1][0], R.registres) == recherche_registre(R.instructions[p][1][1], R.registres):
                return
            R.position+=1
        elif R.instructions[p][0] == 'POW':
            print(R.instructions[p][0])
            res = recherche_registre(R.instructions[p][1][0], R.registres) ** recherche_registre(R.instructions[p][1][1], R.registres)
            R.registres[R.instructions[p][1][2]] = res
            R.position += 1
            print("instructions",R.instructions,"\nregistre:",R.registres,R.position)
        elif R.instructions[p][0] == 'TRI':
            print(R.instructions[p][0])
            tab=R.instructions[p][1]
            n = len(tab)
            # Traverser tous les éléments du tableau
            for i in range(n):
                for j in range(0, n-i-1):
                    # échanger si l'élément trouvé est plus grand que le suivant
                    if int(tab[j]) > int(tab[j+1]) :
                        tab[j], tab[j+1] = int(tab[j+1]), int(tab[j])
            R.position+=1
            c=False
            i=0
            while c==False:
                if f"tab{i}" in R.registres:
                    i+=1
                else:
                    R.registres[f"tab{i}"]=R.instructions[p][1]
                    c=True

#TEST
# execution(program)
# print("instructions",program.instructions,"\nregistre:",program.registres)

#Q3,Q4
def simulateur(txt):
    # Initialiser la configuration de la machine
    ram3 = lecture_program(txt)
    execution(ram3)
    print("instructions",ram3.instructions,"\nregistre:",ram3.registres,ram3.position)

# simulateur("RAM3.txt")

#Q5
# simulateur("RAM puissance.txt")



#Q6
class Automate:
    def __init__(self, Alpha, Q, q0, AlphaP, S, F, T):
        self.Alpha = Alpha
        self.Q = Q
        self.q0 = q0
        self.AlphaP = AlphaP
        self.S = S
        self.F = F
        self.T = T

    def taille_T(self):
        return len(self.T)


class T:
    def __init__(self, p, a, A, w, q):
        self.p = p
        self.a = a
        self.A = A
        self.w = w
        self.q = q


def Automate_RAM(automate):
    taille_T = automate.taille_T()
    liste_RAM = [taille_T]

    for transition in automate.T:
        p = transition.p
        a = transition.a
        A = transition.A
        w = transition.w
        if len(w)>1:
            w0 = int(w[0])
            w1 = int(w[1])
        else:
            w0 = int(w[0])

        q = transition.q

        ram_T = (p, a, A, len(w), w0, w1, q)
        liste_RAM.append(ram_T)

    return liste_RAM

# # Test Automate_Ram
# A = Automate(Alpha={0, 1}, Q={0, 1}, q0=0, AlphaP={0, 1, 2}, S=0, F={1}, T=[T(0, 1, 0, "11", 1), T(1, 0, 0, "22", 0)])
# ram = Automate_RAM(A)
# print("Liste RAM :", ram)


def convertir_en_binaire(w):
    nouvelle_chaine = ""
    type_actuel = w[0]

    for lettre in w:
        if type_actuel == lettre:
            nouvelle_chaine += "0"
        else:
            nouvelle_chaine += "1"

    return nouvelle_chaine

# #Test convertir
# w = "aaabbb"
# w_converti = convertir_en_binaire(w)
# print(w_converti) 


def RAM2(automate, liste_Ram, w):
    conv_w = convertir_en_binaire(w)
    mot = [c for c in conv_w[::-1]]
    pile = []
    etat_actuel = automate.q0

    # Parcourir les instructions de la liste d'instructions de la RAM
    for instruction in liste_Ram[1:]:
        p, a, A, taille_w, w0, w1, q = instruction

        if mot and etat_actuel == p and pile and mot[-1] == a:
            if w0 == 2:
                pile.pop()
            else:
                pile.pop()
                pile.append(w0)
                pile.append(w1)

            etat_actuel = q

            mot.pop()
            if not mot:
                break
        else:
            return 1
    
    if etat_actuel in automate.F:
        return 0
    else:
        return 1


def simulateur_RAM2(A, w):
    liste_Ram = Automate_RAM(A)
    test = RAM2(A, liste_Ram, w)

    print("Résultat de l'exécution :", test)


#TestQ6
# Définition de l'automate à pile, L = {0^n}
A1 = Automate(Alpha={0}, Q={0, 1}, q0=0, AlphaP={0, 1, 2}, S=0, F={1}, T=[T(0, 0, 1, "01", 1), T(1, 1, 0, "11", 1)])
mots = ["0000", "01"]

# for mot in mots:
#     simulateur_RAM2(A1, mot)
#     print()


#Q7
# Définition de l'automate à pile, L = {a^n*b^n}
A7 = Automate(
    Alpha={0, 1}, Q={0, 1}, q0=0, AlphaP={0, 1, 2}, S=0, F={1},
    T=[T(0, 0, 0, "01", 0), T(0, 1, 0, "11", 0), T(0, 1, 1, "2", 1), T(1, 1, 1, "2", 1)])
        
# simulateur_RAM2(A7, "aaabbb")
# simulateur_RAM2(A7, "abab")


#Q8
import networkx as nx
import matplotlib.pyplot as plt


def creer_graphe(machine):
    G = nx.DiGraph()

    # Ajouter les sommets des instructions
    for i, instruction in enumerate(machine.instructions):
        etiquette = f"{i + 1} / {instruction[0]}"
        G.add_node(i, etiquette=etiquette)

    # Parcourir chaque instruction
    for i, instruction in enumerate(machine.instructions):
        opcode = instruction[0]

        # Instruction arithmétique
        if opcode in ['ADD', 'SUB', 'MULT', 'DIV', 'POW', 'TRI']:
            # Ajouter un arc vers l'instruction suivante
            if i + 1 < len(machine.instructions):
                G.add_edge(i, i + 1)

        # Instruction conditionnelle (JE)
        elif opcode == 'JE':
            # Ajouter un arc vers l'instruction suivante
            if i + 1 < len(machine.instructions):
                G.add_edge(i, i + 1)
            # Ajouter un arc vers l'instruction cible
            cible_saut = i + int(instruction[1][0]) if not instruction[1][0].startswith('r') else i + 1
            if cible_saut < len(machine.instructions):
                G.add_edge(i, cible_saut)
        
        #Instruction JUMP
        elif opcode == 'JUMP':
            # Ajouter un arc vers l'instruction de saut
            offset = int(instruction[1][0]) if not instruction[1][0].startswith('r') else 0
            if offset < 0:
                cible_saut = i + offset
            else:
                cible_saut = i + offset - 1
            if cible_saut >= 0 and cible_saut < len(machine.instructions):
                G.add_edge(i, cible_saut)

    return G


# Test du Graph
machine = lecture_program('RAM.txt')
machine2 = lecture_program('RAMQ9.txt')
G = creer_graphe(machine2)


plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
etiquettes = nx.get_node_attributes(G, 'etiquette')
nx.draw(G, pos, with_labels=True, labels=etiquettes, font_weight='bold', node_size=3000, node_color='skyblue')
plt.title("Graphe orienté de la machine RAM")
# plt.show()


#Q9
def elimination_code_mort(machine):
    G = creer_graphe(machine)

    # Calculer tous les sommets accessibles à partir de la première instruction
    sommets_accessibles = set(nx.dfs_preorder_nodes(G, source=0))

    # Supprimer les instructions non accessibles
    instructions_a_supprimer = set(range(len(machine.instructions))) - sommets_accessibles
    for i in instructions_a_supprimer:
        machine.instructions[i] = None
    
    # Supprimer les instructions None
    machine.instructions = [instr for instr in machine.instructions if instr is not None]

    return machine

# TestQ9
machine = lecture_program('RAMQ9.txt')
machine_optimise = elimination_code_mort(machine)
G_optimise = creer_graphe(machine_optimise) 

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G_optimise)
etiquettes = nx.get_node_attributes(G_optimise, 'etiquette')
nx.draw(G_optimise, pos, with_labels=True, labels=etiquettes, font_weight='bold', node_size=3000, node_color='skyblue')
plt.title("Graphe orienté optimisé de la machine RAM")
# plt.show()


def run_all():
    # Exécution de chaque question
    print("Exécution de la question 1:")
    lecture_program('RAM.txt')

    print("\nExécution de la question 2:")
    machine = lecture_program('RAM.txt')
    execution(machine)

    print("\nExécution des questions 3 et 4:")
    simulateur("RAM3.txt")

    print("\nExécution de la question 5:")
    simulateur("RAM puissance.txt")

    print("\nExécution de la question 6:  L = {0^n}")
    A1 = Automate(Alpha={0}, Q={0, 1}, q0=0, AlphaP={0, 1, 2}, S=0, F={1}, T=[T(0, 0, 1, "01", 1), T(1, 1, 0, "11", 1)])
    ram = Automate_RAM(A1)
    print(f"Liste RAM : {ram}\n",)
    mots = ["0000", "01"]
    w = "aaabbb"
    w_converti = convertir_en_binaire(w)
    print(f"Le mot {w} devient {w_converti}\n") 
    for mot in mots:
        simulateur_RAM2(A1, mot)
        print()

    print("\nExécution de la question 7: L = {a^n*b^n}")
    A7 = Automate(
    Alpha={0, 1}, Q={0, 1}, q0=0, AlphaP={0, 1, 2}, S=0, F={1},
    T=[T(0, 0, 0, "01", 0), T(0, 1, 0, "11", 0), T(0, 1, 1, "2", 1), T(1, 1, 1, "2", 1)])
    simulateur_RAM2(A7, "aaabbb")
    simulateur_RAM2(A7, "abab")

    print("\nExécution de la question 8:")
    machine = lecture_program('RAMQ9.txt')
    G = creer_graphe(machine)
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    etiquettes = nx.get_node_attributes(G, 'etiquette')
    nx.draw(G, pos, with_labels=True, labels=etiquettes, font_weight='bold', node_size=3000, node_color='skyblue')
    plt.title("Graphe orienté de la machine RAM")
    plt.show()

    print("\nExécution de la question 9:")
    machine = lecture_program('RAMQ9.txt')
    machine_optimise = elimination_code_mort(machine)
    G_optimise = creer_graphe(machine_optimise) 
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G_optimise)
    etiquettes = nx.get_node_attributes(G_optimise, 'etiquette')
    nx.draw(G_optimise, pos, with_labels=True, labels=etiquettes, font_weight='bold', node_size=3000, node_color='skyblue')
    plt.title("Graphe orienté optimisé de la machine RAM")
    plt.show()

run_all()