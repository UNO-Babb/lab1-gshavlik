#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  verb1 = input("Enter a verb in past tense: ")
  adj1 = input("Enter an adjective that describes how you are doing the verb: ")
  noun2 = input("Enter a second noun: ")
  adj2 = input("Enter a second adjective to describe a feeling: ")
  verb2 = input("Enter a second verb to describe what you're doing: ")
  #Print the story with the user supplied words.
  print("I", adj1 , verb1 , "to the store to get" , noun1 , ".")
  print("I also wanted to get" , noun2 , "but" , adj2 , "they were out so I" , verb2 , "home.")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
