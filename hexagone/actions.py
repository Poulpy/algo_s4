#coding: utf-8
"""
    Les actions que vous écrirez prennent en paramètre un modele.
    Les objets manipulés sont :
        - les sommets (visuellement, les cases hexagonales).
             (Les sommets sont des objets 'Hex' mais 
             vous n'avez pas besoin de les manipuler directement,
             seulement de les passer en paramètre.)

        - les flèches
            (même remarque que pour les sommets
            ce sont en fait des entiers qui representent des objets manipulés
            par la bibliothèque graphique Tkinter)

    Les methodes de l'objet modele utilisables sont les suivantes :

    ### METHODES LIEES AU MODELE THEORIQUE #########################

    modele.getListeSommets():
        renvoie la liste des sommets du modele.
        Rq : modele.getListeSommets(True) renvoie la liste de tous les
        sommets même noirs

    modele.getDepart():
        renvoie le sommet de départ

    modele.getObjectif(self):
        renvoie le sommet objectif

    modele.getVoisins(self, sommet):
        renvoie la liste des sommets voisins d'un sommet donné.
        Rq : modele.getVoisins(True) renvoie la liste de tous les
        voisins même noirs

    modele.longueur(sommet1, sommet2):
        renvoie la longueur de l'arete entre ces deux sommets
        configurable en changeant les valeurs dans hexa_modele

    ### METHODES GRAPHIQUES #########################

    modele.addFleche(sommet1, sommet2, couleur):
        ajoute une fleche du sommet 1 au sommet 2, de la couleur donnée,
        et renvoie un indentifiant (un entier) qui permet de la supprimer plus tard
        couleurs : "Black", "Red", etc.

    modele.delFleche(ref):
        supprimer la fleche dont l'identifiant est ref

    modele.addTexte(sommet, texte):
        ajoute un texte sur le sommet donne. Renvoie un identifiant pour
        pouvoir le supprimer.

    modele.deltexte(ref):
        suppprime le texte dont l'identifiant est ref.

"""



from hexa_modele import *
import random
import time
from collections import deque


def parcoursEnLargeur(modele):
    """effectue un parcours en largeur du sommet de depart
    affiche les prédécesseurs par des flèches grises et le chemin jusqu'à
    l'objectif en rouge"""

    depart = modele.getDepart()
    pred = {}
    distance = {}
    distance[depart] = 0
    attente = [depart]
    while attente:
        courant = attente.pop(0)
        for v in modele.getVoisins(courant):
            if v not in distance:
                distance[v] = distance[courant] + 1
                pred[v] = courant
                attente.append(v)
                modele.addFleche(courant, v, "Black")
                #modele.addTexte(v, distance[v])


def compConnexes(modele):
    comp = [None * len(modele.getListeSommets(True))]
    num = 0
    for s in modele.getListeSommets(True):
        if comp[v] == None:
            #

            #
            num += 1




def parcoursEnProfondeur(modele):
    """effectue un parcours en profondeur du sommet de depart
    affiche les prédécesseurs par des flèches grises et le chemin jusqu'à
    l'objectif en rouge
    Affiche le numero prefixe"""
    depart = modele.getDepart()
    sommets = modele.getListeSommets(depart)
    pred = {}
    connu = set([])
    for s in sommets:
        if s not in connu:
            parcoursEnProfondeurEtape(modele, connu, pred, s)

def parcoursEnProfondeurEtape(modele, connu, pred, s):
    connu.add(s)
    voisins = modele.getVoisins(s)
    random.shuffle(voisins)
    for v in voisins:
        if v not in connu:
            pred[v] = s
            modele.addFleche(pred[v], v, "Black")
            parcoursEnProfondeurEtape(modele, connu, pred, v)

def bellmanFord(modele):
    pass
    
def dijkstra(modele): 
    pass


def astar(modele): 
    pass

