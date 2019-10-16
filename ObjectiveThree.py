import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time
def WPGMA(filename):
	start = time.time()
	f = open(filename, "r")
	strmatrix = f.read()
	matrix = []
	matrix.append([])
	index = 0
	alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	edges = []
	for char in range(len(strmatrix)):									#Converts input string to list of lists
		if strmatrix[char] == "-":
			matrix[index].append(strmatrix[char])
		if strmatrix[char] == "\n":
			index = index + 1
			matrix.append([])
		if strmatrix[char] == " ":
			place = char + 1 
			while True:
				if place == len(strmatrix) -1:
					place = place 
					break
				place = place +1
				if strmatrix[place] == " ":
					place = place -1
					break
				if strmatrix[place] == "\n":
					place = place -1
					break
			nu = strmatrix[char:place+1]
			num = nu.replace(" ","")
			if num not in alph:
				matrix[index].append(int(num))
		if strmatrix[char] in alph:
			matrix[index].append(strmatrix[char])
	for i in range(1,len(matrix)):
		for j in range(1,len(matrix)):
			temp = int(matrix[i][j])
			matrix[i][j] = temp
	while len(matrix) > 3:												#Calculates reduced distance matrices and phylogenetic tree structure
		print("Reduced distance matrix:")
		for i in range(len(matrix)):									#Prints reduced distance matrices
			stri = '	'.join(str(e) for e in matrix[i])
			print(stri)
		smallest = int(matrix[1][len(matrix)-1])
		for i in range(1,len(matrix)):
			for j in range(1,len(matrix)):
				if matrix[i][j] < smallest:
					if matrix[i][j] != 0:
						smallest = matrix[i][j]
						location = [j,i]
		NewName = matrix[0][location[1]] + matrix[location[0]][0]
		edges.append((NewName, matrix[0][location[1]]))
		edges.append((NewName,matrix[location[0]][0]))
		newMatrix = []
		for i in range(len(matrix)-1):
			newMatrix.append([])
		newMatrix[0].append("-")
		newMatrix[0].append(NewName)
		for i in range(len(matrix)):
			if matrix[0][i] != matrix[0][location[1]]:
				if matrix[0][i] != matrix[0][location[0]]:
					if i != 0:
						newMatrix[0].append(matrix[0][i])
		for i in range(1,len(newMatrix)):
			newMatrix[i].append(newMatrix[0][i])
		newMatrix[1].append(0)
		for i in range(2,len(newMatrix)):
			letter = newMatrix[0][i]
			index = matrix[0].index(letter)
			value = (matrix[location[1]][index] + matrix[location[0]][index])/2
			newMatrix[1].append(value)
		for i in range(2,len(newMatrix)):
			newMatrix[i].append(newMatrix[1][i])
		for col in range(2,len(newMatrix)):
			for row in range(2,len(newMatrix)):
				if newMatrix[col][0] != NewName:
					if newMatrix[0][row] != NewName:
						colletter = newMatrix[col][0]
						rowletter = newMatrix[0][row]
						colindex = matrix[0].index(colletter)
						rowindex = matrix[0].index(rowletter)
						newMatrix[row].append(matrix[colindex][rowindex])
		matrix = newMatrix
	print("Reduced distance matrix:")
	for i in range(len(matrix)):										#Prints final reduced distance matrix.
		stri = '	'.join(str(e) for e in matrix[i])
		print(stri)
	finalname = matrix[0][1]+matrix[0][2]
	edges.append((finalname,matrix[0][1]))
	edges.append((finalname,matrix[0][2]))
	G = nx.DiGraph()													#Creates graph for phylogenetic tree.
	G.add_edges_from(edges)
	black_edges = [edge for edge in G.edges()]
	pos = nx.circular_layout(G)
	nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_size = 500)
	nx.draw_networkx_labels(G, pos)
	nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
	plt.savefig("Phylogenetic_Tree.png")								#Saves phylogenetic tree graph to Phylogenetic_Tree.png
	end = time.time()
	print("The program took "+str(end - start)+" to execute.")
print(WPGMA("Matrix2.txt"))

