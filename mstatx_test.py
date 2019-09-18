from MstatX import MstatxCommandline

"""Example to use MstatX wrapper"""

infile= "Protein.fasta" 	# input aligned fasta file
outfile="Protein_output.txt"    # output result file

mstatx_cline=MstatxCommandline(input=infile,output=outfile,globalSum=True) # to get the global similarity score  of the alignment
#print(mstatx_cline) # ./mstatx -i Protein.fasta -o Protein_output.txt -g

stdout, stderr = mstatx_cline() 
print(stdout) #Statistic: wentropy Multiple alignment : nb seq = 5, nb col = 1902, Mstatx computed in 0.006177 seconds, Results are written in Protein_output.txt
