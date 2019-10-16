#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix
def CharScore(char1,char2):												#Defines scores for matching certain characters
	if char1 == "A" and char2 == "A":
		return 4
	if char1 == "C" and char2 == "C":
		return 3
	if char1 == "G" and char2 == "G":
		return 2
	if char1 == "T" and char2 == "T":
		return 1
	if char1 == " " or char2 == " ":
		return -2
	else:
		return -3

def Matrix(seq1,seq2):
	matrix = []
	for i in range(len(seq2)+1):										#Creates an empty list of lists of lists matrix, the lowest list being a tuple of score and backtracking letter, and populates it with
		matrix.append([])												#zeros and predetermined parts of the backtracking matrix.
		for j in range(len(seq1)+1):
			matrix[i].append([0,"E"])
	matrix[0][0][1] = "END"
	for i in range(1,len(matrix[0])):
		matrix[0][i][0] = matrix[0][i-1][0] - 2
		matrix[0][i][1] = "L"
	for i in range(1,len(matrix)):
		matrix[i][0][0] = matrix[i-1][0][0] -2
		matrix[i][0][1] = "U"
	for j in range(1,len(matrix[0])):									#Calculates the score and backtracking letter and inserts into the matrix.
		for i in range(1,len(matrix)):
			if i == 1 and j == 1:
				score = CharScore(seq1[i-1],seq2[j-1])
				matrix[i][j][1] = "D"
			D = CharScore(seq1[j-1],seq2[i-1]) + matrix[i-1][j-1][0]
			L = matrix[i][j-1][0] - 2
			U = matrix[i-1][j][0] - 2
			if max(D,U,L) == D:
				matrix[i][j][1] = "D"
				score = D
			if max(D,U,L) == U:
				matrix[i][j][1] = "U"
				score = U
			if max(D,U,L) == L:
				matrix[i][j][1] = "L"
				score = L
			matrix[i][j][0] = score
	col = len(seq1)
	row = len(seq2)
	align = ["",""]
	while matrix[row][col][1] != "END":									#Produces the sequence alignment.
		if matrix[row][col][1] == "D":
			row = row-1
			col = col-1
			align[0] = seq1[col] + align[0]
			align[1] = seq2[row] + align[1]
		if matrix[row][col][1] == "U":
			row = row-1
			align[0] = "-" + align[0]
			align[1] = seq2[row] + align[1]
		if matrix[row][col][1] == "L":
			col = col -1
			align[0] = seq1[col] + align[0]
			align[1] = "-" + align[1]
	maxScore = matrix[len(seq2)][len(seq1)][0]							#Produces the best score
	return (align, maxScore)
# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
result = Matrix(seq1,seq2)
best_alignment = result[0]
best_score = result[1]


#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

