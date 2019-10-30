# CT-Bioinformatics-Assignment-Year1
Durham University Computational Thinking year 1 assignment.
This readme file briefly describes what each python file does.
A more in-depth specification can be found in the coursework specification pdf.
1) ObjectiveOne.py has the function Matrix(seq1, seq2) where seq1 and seq2 are DNA sequences represented as strings of letters
   and the function outputs the best allignment and the score of that allignment according to some criteria specified in
   the CharScore(char1, char2) function where char1 and char2 are the characters the scoring of which is to be determined.
2) ObjectiveThree.py has the function WPGMA(filename) where filename is the name of the file containing an inter species distance matrix
   the WPGMA algorithm is then used to reduce the distance matrix and the function prints the matrix at every step finally using the
   computed data a phylogenetic tree is drawn and saved to Phylogenetic_Tree.png.
