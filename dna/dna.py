import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv)!=3:
        sys.exit("Error! Please type 2 command line arguments")

    # TODO: Read csv database file into a list
    csvlist=[]
    with open(sys.argv[1],'r') as file1:
        reader1 = csv.DictReader(file1)
        for line in reader1:
            csvlist.append(line)


    # TODO: Read DNA sequence file into a variable reader2
    with open(sys.argv[2],'r') as file2:
        dnasequence = file2.read()


    #store subsequences into a list
    subsequences = list(csvlist[0].keys())
    subsequences.remove("name")

    # TODO: storing longest match of each subsequence in a dictionary
    dictionary={}
    for i in range(len(subsequences)):
        dictionary[subsequences[i]] = longest_match(dnasequence,subsequences[i])


    # TODO: Check CSV database for matching profiles
    for person in csvlist:
        match=0
        for subsequence in subsequences:
            if int(person[subsequence])==dictionary[subsequence]:
                match+=1
        if match==len(subsequences):
            print(person["name"])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

