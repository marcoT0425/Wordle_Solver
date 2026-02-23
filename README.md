# Wordle_Solver
A Wordle solver created by me (Turbowarp)

<img width="746" height="365" alt="Screenshot 2026-02-23 at 11 57 42 AM" src="https://github.com/user-attachments/assets/3d041d03-4b5f-4a2f-997d-d149bda21b7a" />

This is an example of my Wordle solver. The user must type the starting word, and the AI will automatically calculate the second word. After that, the AI starts to run all 2,315 words in the list. 

# Checking the greens
This is a very common mistake. For the double letters, I've used a "`letter frequency`" rule to count all the occurrences of each letter in the word. Next, calculate the green tiles, if the target word is "`slate`" and the user types "chase", the "`a`" and "`e`" are in the same position, so -1 for each letter's occurrences, i.e. checking greens only for answer=`chase` while target=slate is `__g_g`. 

# Examples of my letter frequency rule:

`apple`: `a`:1 `p`:2 `l`:1 `e`:1

`eerie`: `e`:3 `r`:1 `i`:1 

# Checking the yellow (how to get grey or yellow?)
This is the hardest procedure. I've told you that each occurrence of green will be duducted by 1 of the letter. If the letter frequency is 0, it shows grey because there are no more occurrences. Scan from the first to the last letter, and if the letter is not `g`, scan it, if the frequency of the letter is greater than 0, hit yellow. Otherwise, if there are no more occurrences, hit grey.

# Examples of my double letter rule

answer=`chase` input=`slate` colouring=`y_g_g`

answer=`fever` input=`eerie` colouring=`ygy__`

answer=`speed` input=`tribe` colouring=`__y__`
