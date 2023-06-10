#ask for input
text=input("Text: ")

wordcount=0
#count no. of words
wordlist=text.split()
for word in wordlist:
    wordcount+=1

sentencecount=0
#count no. of sentences
for i in range(len(text)):
    if text[i]=="." or text[i]=="?" or text[i]=="!":
        sentencecount+=1

lettercount=0
#count no. of letters
for i in range(len(text)):
    if text[i].isalpha()==True:
        lettercount+=1

#average no. of letters per 100 words
L = lettercount/wordcount*100

#average no. of sentences per 100 words
S = sentencecount/wordcount*100

#Coleman-Liau index
index=round(0.0588*L - 0.296*S -15.8)

if index>=16:
    print("Grade 16+")
elif index<1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")

