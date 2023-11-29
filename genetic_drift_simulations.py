def genetic_drift_task_1(): # defines function for task 1
	import random # imports random module
	from matplotlib import pyplot as plt # imports pyplot function of matplotlib module
	popsize = 100 # sets population size as 100
	pop_array = [] # creates empty 1st population array
	y_data_A = [] # creates empty A allele frequency list
	y_data_B = [] # creates empty B allele frequency list

	# two consecutive for loops add 50% 'A's and 50% 'B's to 1st population array
	for i in range(0, int(popsize/2)):
		pop_array.append('A')
	for i in range(int(popsize/2), popsize):
		pop_array.append('B')
	y_data_A.append(pop_array.count('A')/popsize) # adds A allele frequency to list
	y_data_B.append(pop_array.count('B')/popsize) # adds B allele frequency to list

	for generation in range(1, 1001): # outer for loop works through 1000 generations
		pop_array_2 = [] # makes empty 2nd population array
		for j in range(0, popsize): # inner for loop works through random selections
			# generates random index, accesses allele from 1st array and adds to 2nd array
			pop_array_2.append(pop_array[random.randint(0, popsize-1)])
		y_data_A.append(pop_array_2.count('A')/popsize) # adds A allele frequency to list
		y_data_B.append(pop_array_2.count('B')/popsize) # adds B allele frequency to list
		pop_array = pop_array_2[:] # copies over 2nd to 1st population array
		# checks condition: if neither allele lost continues for loop
		if y_data_A[generation] and y_data_B[generation] > 0: continue
		else: break # mops up every other scenario: if either allele lost breaks for loop

	x_data = range(0, len(y_data_A)) # creates list for X coordinates
	plt.plot(x_data, y_data_A, label='Allele A') # plots curve for A allele
	plt.plot(x_data, y_data_B, label='Allele B') # plots curve for B allele
	plt.legend() # adds legend to plot
	plt.xlabel ('Number of generations') # adds label for X axis to plot
	plt.ylabel('Allele frequency') # adds label for Y axis to plot
	plt.title('Genetic Drift Simulation: Task 1') # adds title to plot
	plt.axis(xmin=0, xmax=len(x_data)-1, ymin=0, ymax=1) # adjusts start/end of both axes
	plt.show() # displays plot on screen
	
genetic_drift_task_1() # calls function for task 1

def genetic_drift_task_2(): # defines function for task 2
	import random # imports random module
	from matplotlib import pyplot as plt # imports pyplot function of matplotlib module
	popsize = 100 # sets population size as 100
	pop_array = [] # creates empty 1st population array
	y_data_AA = [] # creates empty AA genotype frequency list
	y_data_Aa = [] # creates empty Aa genotype frequency list
	y_data_aa = [] # creates empty aa genotype frequency list

	# three consecutive for loops add 25% 'AA's, 50% 'Aa's and 25% 'aa's 1st population array
	for i in range(0, int(popsize/4)):
		pop_array.append('AA')
	for i in range(int(popsize/4), int(popsize*0.75)):
		pop_array.append('Aa')
	for i in range(int(popsize*0.75), popsize):
		pop_array.append('aa')
	y_data_AA.append(pop_array.count('AA')/popsize) # adds AA genotype frequency to list
	y_data_Aa.append((pop_array.count('Aa')+pop_array.count('aA'))/popsize) # adds Aa genotype frequency to list
	y_data_aa.append(pop_array.count('aa')/popsize) # adds aa genotype frequency to list

	for generation in range(1, 501): # outer for loop works through 500 generations
		pop_array_2 = [] # makes empty 2nd population array
		aa_counter = 0 # sets counter for aa genotype to 0
		# inner while loop works through random selections until len(pop_array_2) = popsize
		while len(pop_array_2) <= popsize:
			# randomly selects genotype from 1st array and assigns to indiv1
			indiv1 = pop_array[random.randint(0,popsize-1)]
			# randomly selects genotype from 1st array and assigns to indiv2
			indiv2 = pop_array[random.randint(0,popsize-1)]
			# randomly selects and combines one allele from each individual
			genotype = indiv1[random.randint(0,1)]+indiv2[random.randint(0,1)]
			# checks condition: if not aa genotype adds to 2nd array
			if genotype != 'aa': pop_array_2.append(genotype)
			else: # mops up every other scenario: if aa genotype
				aa_counter += 1 # adds 1 to aa genotype counter
				# checks condition: adds 80% of aa genotypes to 2nd array
				if aa_counter % 5 != 0: pop_array_2.append(genotype)
				else: continue # mops up every other scenario: rejects 20% of aa genotypes
		y_data_AA.append(pop_array_2.count('AA')/popsize) # adds AA genotype frequency to list
		y_data_Aa.append((pop_array_2.count('Aa')+pop_array_2.count('aA'))/popsize) # adds Aa genotype frequency to list
		y_data_aa.append(pop_array_2.count('aa')/popsize) # adds aa genotype frequency to list
		pop_array = pop_array_2[:] # copies over 2nd to 1st population array
		# checks condition: if a allele not lost continues outer for loop
		if y_data_Aa[generation] or y_data_aa[generation] > 0: continue
		else: break # mops up every other scenario: if a allele lost breaks outer for loop

	x_data = range(0, len(y_data_AA)) # creates list for X coordinates
	plt.plot(x_data, y_data_AA, label='Genotype AA') # plots curve for AA genotype
	plt.plot(x_data, y_data_Aa, label='Genotype Aa') # plots curve for Aa genotype
	plt.plot(x_data, y_data_aa, label='Genotype aa') # plots curve for aa genotype
	plt.legend() # adds legend to plot
	plt.xlabel ('Number of generations') # adds label for X axis to plot
	plt.ylabel('Genotype frequency') # adds label for Y axis to plot
	plt.title('Genetic Drift Simulation: Task 2') # adds title to plot
	plt.axis(xmin=0, xmax=len(x_data)-1, ymin=0, ymax=1) # adjusts start/end of both axes
	plt.show() # displays plot on screen

genetic_drift_task_2() # calls function for task 2
