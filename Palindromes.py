palindrome = 0
palindromes = []

while True:
    word = input("Please input a word/sentence: ")
    counter = 0
    reverse = ""

    while counter < len(word):
        reverse += word[-(counter + 1)]
        counter += 1

    print(reverse)

    if word == reverse: 
        if word in palindromes:
            print("You have already found that palindrome, try to find another.")
        else:
            palindrome += 1
            print(f"You have found a palindrome! Palindrome number {palindrome}!")
            palindromes.append(word)
    else:
        print("That is not a palindrome. Try again.")