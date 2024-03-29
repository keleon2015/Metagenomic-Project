## **IBS 574**
## **Python Programming Exercises**
## Class Sessions: 15, 20, 22, 27 January 2015

**Each homework should be submitted as a separate pull request (HW1, 2, 3 each in their own pull request). Please let us know if you have any trouble submitting pull requests before the due date. You can submit a test pull request, then edit its contents at any point up to the submission deadline. After the submission deadline, assignment pull requests will be closed to further edits.**

The purpose of the problems below are to introduce you to programming with Python. While we do not expect that every student will necessarily be successful in completing every exercise, we expect that you will attempt them all. We will select a student at random to present and discuss their solution to the class (whether it is complete or incomplete). Class time over the next three sessions will focus on going over solutions and devising programs (with assistance from instructors) to solve each of these problems together. The ultimate goal of this exercise is not to make you expert Python programmers, but to give you enough background that you could use Python to manipulate the types of large datasets that you will surely be generating as graduate students. Hopefully these exercises will make you interested in learning more as you progress through your graduate career.

# **Setup Instructions (General and Git)**
[http://ibs574.github.io/docs/](http://ibs574.github.io/docs/)

# **Submission Instructions** 
`All assignments should be submitted as pull requests.`

`Name you pull request "HW# : Your Full Name"`

`You can edit any files, before the submission deadline. `
`To make changes to your pull request, you can simply push a new change to your repository.`

`To submit a pull request, push the changes you made, as instructed above`


# **Complete by January 22, 2015 (end of day)**
->1. Use a text editor (vi or nano) to extend the “Hello World” program to accept a name via Unix pipe and print the word “Hello”, followed by the name, followed by the word “again.” What happens when no argument is supplied? What should happen?

*(Teaching Objective: basic text editing, become familiar with Unix environment, learn about commands, pipes and input/output redirection)*

->2. Extend the program from #1 to accept an arbitrary number of names and produce the output described in #1 for each supplied name. Bonus: Use Unix commands and pipes to count the number of names.

*(Teaching Objective: basic text editing, become familiar with Unix environment, learn about commands, pipes and input/output redirection)*

->3. Write a program to read a FastA file, count CG di-nucleotides in the sequence and output the count to the screen. Use the following FastA files:

	/home/Shared/IBS574/Programming_Exercises_Data/tempDNA.fasta
	/home/Shared/IBS574/Programming_Exercises_Data/phix_genome.fa

*(Teaching objective: string searching)*

# **Complete by  January 23, 2015**
->4. Extend the program from #3 to read a multi-FastA file and output the CG count for each sequence. The output should contain four tab-separated columns - chromosome, start coordinate, stop coordinate, and CG count, one line per input sequence. Use the following multi-FastA file: 

	/home/Shared/IBS574/Programming_Exercises_Data/Acinetobacter_baumannii_AB5075.fa

*(Teaching objective: loops, formatted output)*

->5. Write a program to read a number on the command line and generate the hailstone sequence for that number. The hailstone sequence is generated by repeated application of the following rules:
	
	1. If n is even, divide it by 2
	2. If n is odd, multiply it by 3 and add 1

Your program should check that the input parameter is valid (n > 0), and stop when n = 1.

*(Teaching Objective: input validation, mathematical operators, flow control)*

->6. Generate the reverse complement of a sequence. The program should read the input sequence via the command line and print the output on the screen. Your program should check for valid input and take appropriate action. What checks ought to be performed?

*(Teaching Objective: string and character manipulation, input validation, loops, 3’ 5’ notation and implementation)*

# **Complete by January 27, 2015**
->7. Write a program to compute min, median, average, max of a range of numbers supplied on the command line or via Unix pipe.

*(Teaching Objectives: loops, dynamic number of command line parameters, mathematical operators, arrays, flow control)*

->8. Extend the program from #2 to find CpG islands (CG flanked by n non-CG bases) and output to a file. Your program should accept three parameters - the name of the input file, the name of the output file, and a number n (2 <= n <= 6).  CpG islands for this problem will be defined as one or more consecutive CG di-nucleotides surrounded by bases that do not form (or contain) a CG pair, e.g.

    n=2 agCGtt
    n=4 atgtCGCGCGCGtttt
    n=6 aatccaCGtgcata
    n=6 aataacCGCGCGatatat

Surrounding bases are shown in lower-case for clarity.
Students should use the chrY.fa file as the input file.  The path for chrY.fa is as follows:

    /home/Shared/IBS574/Programming_Exercises_Data/chrY.fa

*(Teaching Objective: advanced string searching/manipulation, file output, multiple command line parameters, arrays)*

->9. Write a program that will take two parameters on the command line. The first parameter is a BED file and the second parameter is a reference file. The program should generate a multi-FastA file from the sequence coordinates in the BED file. The program should output a to the screen, unless a third parameter is provided which would be the name of the output file. The program should output valid FastA sequences (header + sequence) for each coordinate, whether to the screen or to a file. The program should not prompt the user for any input.

For problem 9 use the following BED file and the following FastA file as the reference:

    /home/Shared/IBS574/Programming_Exercises_Data/mm10_chr5_exons.bed
    /home/Shared/IBS574/Programming_Exercises_Data/mm10_chr5.fa

*(Teaching Objective: multiple file input, loops, reference genomes, genomic coordinate system, string manipulation, arrays, file output, BED files)*

### **Optional:**
->10. Using the coordinates contained within a BED file (see BED file for Question 10 in Programming_Exercises_Data Directory), extend the program from #9 to eliminate duplicate sequences, remove embedded sequences (sequences that lie completely within another sequence), and merge overlapping sequences.

*(Teaching Objective: loops, coordinate system, string manipulation, arrays, functions, algorithms)*
