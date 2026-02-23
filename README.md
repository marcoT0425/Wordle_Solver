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

# Checking the next word
The solver is NOT using hard mode. The rule is that the AI has to check a word with the most pairs and with the smallest "biggest pair", e.g. `slate` = `g_g_g`, the best word is `chirp`, with 9 pairs and the largest group is 4. Check the remaining words first, and then the full word list.

You can download the `full tree` for reference, here is an example:

`aback 1/2315`

`2315 words remaining`

`slate __g__`

`48 words remaining`

`churn y____`

`1 words remaining`

`aback ggggg`

`solved`

...

# Status (for some starting words) (in Easy Mode) (with the method "most groups, smallest biggest group")

After testing some of the starting words, the results are similar to 3B1B. The best is "`SLATE`".

| Starting word | average | total | 1-guess | 2-guess | 3-guess | 4-guess | 5-guess | 6-guess | fail |
| ------------- | ------- | ----- | ------- | ------- | ------- | ------- | ------- | ------- | ---- |
| `slate`       | 3.428   | 7932  | 1       | 67      | **1245**| 945     | 54      | 2       | 0    |
| `trace`       | 3.430   | 7938  | 1       | 73      | **1237**| 937     | 64      | 2       | 0    |
| `crane`       | 3.431   | 7940  | 1       | 70      | **1237**| 946     | 56      | 4       | 0    |
| `crate`       | 3.432   | 7941  | 1       | 82      | **1215**| 951     | 63      | 2       | 0    |
| `trone`       | 3.450   | 7984  | 0       | 58      | **1224**| 964     | 68      | 0       | 0    |
| `stare`       | 3.453   | 7991  | 1       | 48      | **1237**| 958     | 69      | 1       | 0    |
| `trade`       | 3.454   | 7993  | 1       | 71      | **1177**| 1008    | 55      | 2       | 0    |
| `canst`       | 3.459   | 8004  | 0       | 59      | **1174**| 1042    | 38      | 1       | 0    |
| `rated`       | 3.490   | 8075  | 0       | 68      | 1090    |**1111** | 45      | 0       | 0    |
| `craft`       | 3.510   | 8133  | 1       | 67      | 1054    |**1124** | 68      | 0       | 0    |
| `cramp`       | 3.543   | 8199  | 1       | 58      | 1003    |**1187** | 65      | 0       | 0    |

# Status (for some starting words) (in Hard Mode) (with the method "most groups, smallest biggest group")

Some of the puzzles is failed because of the traps, e.g. `wound`, `found`, `bound`, `sound`, `round`, `mound`, `found`, `pound` etc. "Cramp" is the only word with no fails.

| Starting word | average | total | 1-guess | 2-guess | 3-guess | 4-guess | 5-guess | 6-guess | fail |
| ------------- | ------- | ----- | ------- | ------- | ------- | ------- | ------- | ------- | ---- |
| `slate`       | 3.530   | 8168  | 1       | 120     | **1081**| 926     | 148     | 27      | 11   |
| `least`       | 3.531   | 8171  | 1       | 115     | **1075**| 943     | 147     | 24      | 9    |
| `crate`       | 3.537   | 8185  | 1       | 124     | **1075**| 910     | 164     | 30      | 10   |
| `crane`       | 3.538   | 8187  | 1       | 117     | **1059**| 950     | 154     | 27      | 6    |
| `plate`       | 3.547   | 8207  | 1       | 111     | **1047**| 970     | 152     | 28      | 5    |
| `dealt`       | 3.552   | 8220  | 1       | 102     | **1061**| 960     | 158     | 24      | 8    |
| `plant`       | 3.554   | 8223  | 1       | 102     | 1015    | **1034**| 140     | 18      | 4    |
| `stare`       | 3.557   | 8231  | 1       | 110     | **1045**| 967     | 152     | 28      | 11   |
| `trope`       | 3.568   | 8256  | 1       | 109     | 1005    | **1008**| 163     | 21      | 7    |
| `cramp`       | 3.608   | 8350  | 1       | 79      | 930     | **1132**| 159     | 13      | 0    |

Should you have any problems, please contact me by email: mankotoa@gmail.com or to open an issue.

Other starting words (I'll do it later):

* ADIEU
* AUDIO
* SOARE
* ROATE
* STARE (✓)
* QAJAQ
* SUSUS
* XYLYL
* SHINE
* CLASP
* SALET
* CLAST
* REAST
* SLANE
* TRIPE
* TRICE
* RAISE
* OUIJA
* IMMIX
* EERIE
* SAUCE

(Whole processing: about 30 minutes or even hours for each word)
