from Bio import *
from Bio import Phylo



## https://bioinfo-fr.net/automatiser-le-parcours-et-la-manipulation-darbres-phylogenetiques-avec-le-module-bio-phylo-de-biopython
##http://biopython-cn.readthedocs.io/zh_CN/latest/en/chr13.html
## ete toolkit    http://etetoolkit.org/download/
#import pickle

import os
from os import chdir


nom_repertoire=(str(raw_input("donnez le nom du repertoire selon le readme: ")))
os.chdir(nom_repertoire)


dicoEspeces={1:"Amazon molly", 2:"Cave fish", 3:"Cod", 4:"Fugu", 5:"Medaka", 6:"Platyfish", 7:"Stickleback", 8:"Tetraodon", 9:"Tilapia", 10:"Zebrafish"}
dicoCode={"1":'ENSPFO.*', "2":'ENSAMX.*', "3":'ENSGMO.*', "4":'ENSTRU.*', "5":'ENSORL.*', "6":'ENSXMA.*', "7":'ENSGAC.*', "8":'ENSTNI.*', "9":'ENSONI.*', "10":'ENSDAR.*'}


for i in dicoEspeces.keys():
	print (str(i)+" "+":"+" "+dicoEspeces[i]+"\n")


llllll=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
cont=True
while cont:
	NumEspece=(str(raw_input("donnez le nom de code du poisson: ")))
	for i in NumEspece:
		if i not in llllll:
			print "vous n avez pas rentre les bons caracteres"
		elif int(NumEspece) < 1 or int(NumEspece) >10:
			print "le numero n est pas le bon"
		else:
			cont=False

CodeEspece=dicoCode[NumEspece]
print CodeEspece

liste = open("human_genes", "r")
lili=liste.readlines()

## faire une boucle dans lili, et dans chaque boucle l'arbre et faire tourner (tree=Phylo.read("i.nhx", "newick")

liste_genes_singloton=[]
liste_genes_dupliques=[]
liste_genes_sans_poissons=[]
liste_sans_clupeo=[]




def get_parent(tree, child_clade):
	node_path = tree.get_path(child_clade)
	#print node_path
	if len(node_path)>=2: 
		return node_path[-2]
	elif len(node_path)==1: 
		return False

compteur=1
for i in lili:
	print "***********"+str(compteur)+"************"
	nom_gene=i[0:15]
	nom_arbre=i[0:15]+".nhx"
	#print nom_arbre
	tree=Phylo.read(nom_arbre, "newick")
	#Phylo.draw(tree)

	myclade = tree.find_clades("Mammalia")
	clade_fils=""

	for i in myclade:
		lolo=i
		tree2 = tree.from_clade(lolo)
		#Phylo.draw(tree2)
		resultat1 = tree2.find_any({'name' : nom_gene})
		if resultat1!=None:
			clade_fils=i
			#print clade_fils
			#Phylo.draw(tree2)
			break
	if clade_fils=="":
		myclade = tree.find_clades("Eutheria")
		for i in myclade:
			lolo=i
			tree2 = tree.from_clade(lolo)
			#Phylo.draw(tree2)
			resultat1 = tree2.find_any({'name' : nom_gene})
			if resultat1!=None:
				clade_fils=i
				#print clade_fils
				#Phylo.draw(tree2)
				break



	if clade_fils!="":

		boucleur=True
		Presence_poisson=True
		while boucleur:
			zaza=get_parent(tree, clade_fils)
			if zaza==False:
				arbre=Phylo.read(nom_arbre, "newick")
				#Phylo.draw(arbre)
				trouve=arbre.find_any({'name' : 'Euteleostomi'})
				if trouve!=None:
					bon_ou_dupli_autre = arbre.find_any({'comment' : '&&NHX:S=Euteleostomi:D=Y.*'})
					if bon_ou_dupli_autre != None:
						marqueur=True
						arbres_de_teleost = tree.find_clades("Euteleostomi")
						for caca in arbres_de_teleost:
							teleost_tree=tree.from_clade(caca)
							derniere_chance=teleost_tree.find_any({'comment' : '&&NHX:S=Euteleostomi:D=N.*'})
							if derniere_chance != None:
								essais1=teleost_tree.find_clades("Mammalia")
								essais2=teleost_tree.find_clades("Eutheria")
								if essais1 == None and essais2 == None:
									arbre=teleost_tree
									marqueur=False
									boucleur=False
									break
						if marqueur==True:
							clade_fils=""
					boucleur=False
					break
				else:
					clade_fils=""
					Presence_poisson=False
					boucleur=False
			elif zaza==None:
				clade_fils=""
				Presence_poisson=False
				boucleur=False
			else:
				nom=str(zaza)
				arbre = tree.from_clade(zaza)
				#Phylo.draw(arbre)
				trouve=arbre.find_any({'name' : 'Euteleostomi'})
				if trouve!=None:
					bon_ou_dupli_autre = arbre.find_any({'comment' : '&&NHX:S=Euteleostomi:D=Y.*'})
					if bon_ou_dupli_autre != None:
						marqueur=True
						arbres_de_teleost = tree.find_clades("Euteleostomi")
						for caca in arbres_de_teleost:
							teleost_tree=tree.from_clade(caca)
							derniere_chance=teleost_tree.find_any({'comment' : '&&NHX:S=Euteleostomi:D=N.*'})
							if derniere_chance != None:
								essais1=teleost_tree.find_clades("Mammalia")
								essais2=teleost_tree.find_clades("Eutheria")
								if essais1 == None and essais2 == None:
									arbre=teleost_tree
									marqueur=False
									boucleur=False
									break
						if marqueur==True:
							clade_fils=""
					boucleur=False
					break
				else:
					a=arbre.find_any({'comment' : '&&NHX:S=Eutheria:D=Y.*'})
					b=arbre.find_any({'comment' : '&&NHX:S=Amniota:D=Y.*'})
					c=arbre.find_any({'comment' : '&&NHX:S=Tetrapoda:D=Y.*'})
					d=arbre.find_any({'comment' : '&&NHX:S=Sarcopterygii:D=Y.*'})
					e=arbre.find_any({'comment' : '&&NHX:S=Theria:D=Y.*'})
					f=arbre.find_any({'comment' : '&&NHX:S=Mammalia:D=Y.*'})
					if a == None and b == None and c == None and d == None and e == None and f == None:
						clade_fils=zaza
					else:
						clade_fils=""
						Presence_poisson=False
						boucleur=False



	if clade_fils=="":
		#print "kk"
		liste_genes_sans_poissons.append(nom_gene)### !!!!!nom arbre!!!!

	else:
		verif_clupeo=arbre.find_any({'name' : "Clupeocephala"})
		if verif_clupeo!=None:
			duplication="n"
			liste_genes_du_poisson=[]
			poisson=arbre.find_clades({'name' : "Clupeocephala"})
			for i in poisson:
				arbre_poissons = tree.from_clade(i)
				#Phylo.draw(arbre_poissons)
				dupli = arbre_poissons.find_any({'comment' : '&&NHX:S=Clupeocephala:D=Y.*'})


				if dupli!=None:
					duplication="y"
					term=arbre_poissons.find_elements({'name' : CodeEspece})
					for i in term:
						#print i
						liste_genes_du_poisson.append(i)
				else:

					term=arbre_poissons.find_elements({'name' : CodeEspece})
					for i in term:
						#print i
						liste_genes_du_poisson.append(i)
			if duplication == "n":
				liste_genes_singloton.append(nom_gene)
				if len(liste_genes_du_poisson)>0:
					for elt in liste_genes_du_poisson:
						if elt not in liste_genes_singloton:
							liste_genes_singloton.append(elt)
			if duplication == "y":
				liste_genes_dupliques.append(nom_gene)
				if len(liste_genes_du_poisson)>0:
					for elt in liste_genes_du_poisson:
						if elt not in liste_genes_dupliques:
							#print elt
							liste_genes_dupliques.append(elt)
			#print liste_genes_du_poisson
			#print duplication
							

		else:
			poisson=arbre.find_clades({'name' : "Euteleostomi"})
			liste_genes_du_poisson=[]
			for i in poisson:
				arbre_poissons = tree.from_clade(i)
				#Phylo.draw(arbre_poissons)
				term=arbre_poissons.find_elements({'name' : CodeEspece})
				for j in term:
					#print j
					liste_genes_du_poisson.append(j)

			liste_sans_clupeo.append(nom_gene)
			if len(liste_genes_du_poisson):
				for elt in liste_genes_du_poisson:
					#print elt
					liste_sans_clupeo.append(elt)
			#print liste_sans_clupeo
	compteur+=1



liste.close()

f=open("genes_singleton", "w")
for elt in liste_genes_singloton:
	if elt[0:5]=="ENSG0":
		f.write("\n"+elt)
	else:
		f.write(" "+str(elt))
f.close()

f=open("genes_without_fish", "w")
for elt in liste_genes_sans_poissons:
	f.write(elt+"\n")
f.close()


f=open("genes_duplicat", "w")
for elt in liste_genes_dupliques:
	if elt[0:5]=="ENSG0":
		f.write("\n"+elt)
	else:
		f.write(" "+str(elt))
f.close()


f=open("genes_without_clupeocephala", "w")
for elt in liste_sans_clupeo:
	#print elt
	if elt[0:5]=="ENSG0":
		f.write("\n"+elt)
	else:
		f.write(" "+str(elt))

f.close()










			

