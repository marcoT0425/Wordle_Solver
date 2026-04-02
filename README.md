# Wordle_Solver

<img width="424" height="620" alt="Screenshot 2026-03-21 at 7 04 10 PM" src="https://github.com/user-attachments/assets/e7837694-b8dd-4929-9228-9a895d3ac6a5" />

<img width="399" height="238" alt="Screenshot 2026-03-27 at 3 38 09 PM" src="https://github.com/user-attachments/assets/89ace5fb-1048-4a6d-9c89-151c31911a39" />

** (!) NSFW WARNING: This repository contains sexually explicit language and profanity intended for use with the game Lewdle. Content is for technical/gaming purposes only.
**

A Wordle solver created by me (Turbowarp)

It can solve:

* Wordle NYT (Extended 3158) (https://www.nytimes.com/games/wordle/index.html)
* Wordle Unlimited (2315) (https://wordleunlimited.org/)
* Hello Wordl (Easy mode only 4-15 Letters) (https://hellowordl.net/)
* Is that even a word? (12972) le (https://isthatevenawordle.netlify.app/)
* Repeatle (Duplicate letter) (https://repeatle.netlify.app/)
* Lewdle (https://www.lewdlegame.com/)
* Spotle (https://spotlegame.co.uk/)

Later, I'll be making:

* Numberle (https://dduarte.github.io/numberle/)
* Nerdle (https://nerdlegame.com/, https://github.com/pedrokkrause/Nerdle-Equations)
* Thirdle (https://github.com/Web-Dev-Dan/Thirdle)

https://docs.google.com/document/d/1HsSndPdj18PqUPx67PppcufmEn9fEXdVQoeagGPAMt8/edit?usp=sharing

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

# Running the code

(The codes have no relation to Python, JavaScript or CSS. These are just the text expression of the Scratch blocks using different symbols. Copying the code itself is highly discouraged.)

You have to download `Wordle Bot Solver.sb3` and run it in Scratch or Turbowarp.

* List: `proper word` (meaning the answer list) (remember always remove the space at the last item whenever possible) (you can update it)
* List: `word list` (meaning the guessable words) (remember always remove the space at the last item whenever possible) (you can update it)
* List: `full tree` (meaning the statistics) (do not update)
* List: `answer tree` (meaning the statistics without "words remaining") (you can update like)

Method 1 (e.g. `trans __g__ clime y____ aahed gy___ aback ggggg`)

`{variable}` `(text)` `[list]` `<boolean>`

```...
if <{best word} = [item {secret} of proper word]>
add (join(join {best word} (join ()[colourboard]))( )) to [_tree]
else
add (join(join {best word} (join ()[colourboard]))( )) to [_tree]
set {ans} to (join {best word} (join ( )[colourboard]))
...
```

or

Method 2 (e.g. `trans,clime,aahed,aback`)

`{variable}` `(text)` `[list]` `<boolean>`

```...
if <{best word} = [item {secret} of proper word]>
add {best word} to [_tree]
else
add (join{best word}(,)) to [_tree]
set {ans} to (join {best word} (join ( )[colourboard]))
...
```

<img width="280" height="397" alt="Screenshot 2026-02-25 at 6 01 44 PM" src="https://github.com/user-attachments/assets/01f4c174-11f5-4728-ab82-49be836a24df" />

# Word lists

For the word lists, there are two lists, which are:
* `proper word` (the answer word list)
* `word list` (two words) (the guessable word list)
(by finding the word lists, please go to https://github.com/alex1770/wordle)

Word lists:
* (For `proper word`) use https://github.com/alex1770/wordle/blob/main/wordlist_nyt20230701_hidden (post-2023) or https://github.com/marcoT0425/Wordle_Solver/blob/main/proper%20word.txt (pre-2023)
* (For `word list`) use [https://github.com/alex1770/wordle/blob/main/wordlist_nyt20230701_hidden (post-2023) or https://github.com/marcoT0425/Wordle_Solver/blob/main/proper%20word.txt (pre-2023)](https://github.com/marcoT0425/Wordle_Solver/blob/main/nyt%20pre-2023.txt) (pre-NYT) or https://github.com/alex1770/wordle/blob/main/wordlist_nyt20220830_all.

* By using the lists, you **must** delete the last item with a space to avoid causing errors.

# Toggling hard mode

By toggling the hard mode, you have to do something, which are:

1. The hard mode block
<img width="294" height="452" alt="Screenshot 2026-02-25 at 6 41 39 PM" src="https://github.com/user-attachments/assets/5caa0b5e-02d1-4928-a2b1-2e944bef6449" />

2. For the "`find the best choice`" block, you **must** change something, which is:
 
**Easy mode (Original)** (Some of the variable names have no relation to the meaning. Therefore it might be an unknown word or a typo.)

`{variable}` `(text)` `[list]` `<boolean>` 

* Note: greater-than is >, while less-than is <, to avoid confusion.

```
define find the best choice 
...
repeat (length of [cc])
if <[item {crnae} of cc] greater-than {aaaaa}>
set {aaaaaa} to [item {crnae} of cc]
_
change {crnae} by 1
if <([length of crane] + (() - ({aaaaaa} / 1000))) greater-than {best group}>
...
```
<img width="298" height="248" alt="Screenshot 2026-02-25 at 7 00 23 PM" src="https://github.com/user-attachments/assets/c57a265b-e3f3-4089-af11-f9dcb5b53191" />

**Hard mode (If toggled)** (Some of the variable names have no relation to the meaning. Therefore it might be an unknown word or a typo.)

`{variable}` `(text)` `[list]` `<boolean>` 

* Note: greater-than is >, while less-than is <, to avoid confusion. The word "hard" is a customised block.

```
define find the best choice 
...
repeat (length of [cc])
if <[item {crnae} of cc] greater-than {aaaaa}>
set {aaaaaa} to [item {crnae} of cc]
_
hard
change {crnae} by 1
if <<([length of crane] + (() - ({aaaaaa} / 1000))) greater-than {best group}> and <{prob} = 0>>
...
```
<img width="305" height="217" alt="Screenshot 2026-02-25 at 7 05 22 PM" src="https://github.com/user-attachments/assets/429d57ee-cf2c-45b4-a3ee-8d2cd93d13b9" />

# Critical notes when running the .sb3 file

1. The user must turn on the Turbo Mode.
2. The user must turn on the 60 FPS Mode. (TurboWarp only) 
3. If the user is using TurboWarp, they are recommended to turn on the High Quality Pen and Warp Timer mode.

# The .sb3 File

https://github.com/marcoT0425/Wordle_Solver/blob/main/Wordle%20Bot%20(Use).sb3

The user must use this file instead of the others.


# Wordle Status (leaderboard)
* Method 1: Average guesses
Easy mode: 12972 words, 2315 answers:

Note: The results are being re-evaluated. (SALET-PALET testing) https://github.com/alex1770/wordle/blob/main/normal.some3593.proven

1.  `salet`: 3.427 Avg. 
2.  `slate`: 3.431 Avg.
3.  `reast`: 3.432 Avg.
4.  `crate`: 3.432 Avg.
5.  `trace`: 3.433 Avg.
6.  `crane`: 3.433 Avg.
7.  `carle`: 3.436 Avg.
8.  `slane`: 3.437 Avg.
9.  `slant`: 3.439 Avg.
10. `carte`: 3.442 Avg.
11. `torse`: 3.442 Avg.
12. `prate`: 3.445 Avg.
13. `trine`: 3.446 Avg.
14. `least`: 3.446 Avg.
15. `trice`: 3.447 Avg.
16. `stale`: 3.448 Avg.
17. `train`: 3.449 Avg.
18. `caret`: 3.449 Avg.
19. `rance`: 3.449 Avg.
20. `slart`: 3.450 Avg.
21. `roast`: 3.450 Avg.
22. `carse`: 3.451 Avg.
23. `clast`: 3.451 Avg.
24. `trone`: 3.451 Avg.
25. `taser`: 3.451 Avg.
26. `crine`: 3.451 Avg.
27. `react`: 3.452 Avg.
28. `roist`: 3.453 Avg.
29. `trape`: 3.453 Avg.
30. `toile`: 3.453 Avg.
31. `lance`: 3.453 Avg.
32. `earst`: 3.453 Avg.
33. `stare`: 3.453 Avg.
34. `leant`: 3.454 Avg.
35. `trade`: 3.455 Avg.
36. `crone`: 3.455 Avg.
37. `scale`: 3.455 Avg.
38. `saint`: 3.456 Avg.
39. `stane`: 3.457 Avg.
40. `drant`: 3.457 Avg.
41. `slice`: 3.457 Avg.
42. `peart`: 3.458 Avg.
43. `loast`: 3.458 Avg.
44. `plate`: 3.459 Avg.
45. `parse`: 3.459 Avg.
46. `canst`: 3.459 Avg.
47. `clart`: 3.459 Avg.
48. `snare`: 3.459 Avg.
49. `sorel`: 3.459 Avg.
50. `crise`: 3.460 Avg.
51. `crost`: 3.460 Avg.
52. `reist`: 3.461 Avg.
53. `truce`: 3.461 Avg.
54. `soare`: 3.462 Avg.
55. `roset`: 3.462 Avg.
56. `alist`: 3.462 Avg.
57. `dealt`: 3.462 Avg.
58. `store`: 3.462 Avg.
59. `snirt`: 3.462 Avg.
60. `roate`: 3.463 Avg.
61. `liane`: 3.463 Avg.
62. `prase`: 3.463 Avg.
63. `raine`: 3.463 Avg.
64. `trans`: 3.463 Avg.
65. `resat`: 3.464 Avg.
66. `close`: 3.464 Avg.
67. `teals`: 3.464 Avg.
68. `corse`: 3.465 Avg.
69. `tripe`: 3.465 Avg.
70. `orant`: 3.465 Avg.
71. `grate`: 3.465 Avg.
72. `riant`: 3.466 Avg.
73. `tares`: 3.466 Avg.
74. `caner`: 3.466 Avg.
75. `tried`: 3.466 Avg.
76. `sault`: 3.466 Avg.
77. `arose`: 3.466 Avg.
78. `saner`: 3.467 Avg.
79. `thale`: 3.467 Avg.
80. `aline`: 3.468 Avg.
81. `artel`: 3.468 Avg.
82. `strae`: 3.468 Avg.
83. `raise`: 3.468 Avg.
84. `tears`: 3.468 Avg.
85. `caple`: 3.468 Avg.
86. `trail`: 3.468 Avg.
87. `stile`: 3.468 Avg.
88. `snore`: 3.468 Avg.
89. `palet`: 3.468 Avg.
90. `tarns`: 3.468 Avg.
91. `plane`: 3.469 Avg.
92. `cater`: 3.469 Avg.
93. `rinse`: 3.469 Avg.
94. `spalt`: 3.469 Avg.
95. `raile`: 3.469 Avg.
96. `antre`: 3.470 Avg.
97. `stole`: 3.470 Avg.
98. `cline`: 3.470 Avg.
99. `crest`: 3.470 Avg.
100. `taler`: 3.470 Avg.
101. `earnt`: 3.470 Avg.
102. `saine`: 3.471 Avg.
103. `tales`: 3.471 Avg.
104. `anile`: 3.471 Avg.
105. `clint`: 3.471 Avg.
106. `caste`: 3.471 Avg.
107. `place`: 3.471 Avg.
108. `slade`: 3.471 Avg.
109. `ronte`: 3.472 Avg.
110. `orate`: 3.473 Avg.
111. `alter`: 3.474 Avg.
112. `scart`: 3.474 Avg.
113. `seral`: 3.478 Avg.

SALET meaning: A salet (or sallet) is a type of light steel combat helmet that gained popularity across 15th-century Europe, often featuring a slit for vision and a neck guard. It replaced the earlier bascinet and was commonly used by infantry and cavalry. It is also known as a salade, celata, or schaller. (from Gemini)

# The hall of shame (not fully tested, but I've been working with other best openers):
* `qajaq`: 4.114 Avg.
* `immix`: 4.022 Avg.
* `xylyl`: 4.012 Avg.
* `ayaya`: 4.000 Avg.
* `quiff`: 3.960 Avg.
* `akkas`: 3.898 Avg.
* `whiff`: 3.866 Avg.
* `ouija`: 3.802 Avg.

NOTE: ZIZIT is a very bad Wordle starting word. It might fail one of the puzzles. It is recommended to use the "prioritising least group" theory to minimise risks of failing. Later, I'll be testing it.

Zizit (or tzitzit, tzitzith) are specially knotted fringes or tassels worn on the corners of garments by Jewish people, particularly at the corners of a prayer shawl (tallit). They serve as a physical reminder of God’s commandments and the obligation to follow them.

(MinMax counting with ZIZIT)

(test only)

<img width="336" height="393" alt="Screenshot 2026-03-26 at 1 52 56 AM" src="https://github.com/user-attachments/assets/a93ea257-1945-4538-8de9-a5a60e355285" />
<img width="331" height="393" alt="Screenshot 2026-03-26 at 1 54 12 AM" src="https://github.com/user-attachments/assets/92d9e4c1-6fb0-400e-b389-5667b0495aa8" />
<img width="334" height="400" alt="Screenshot 2026-03-26 at 1 57 00 AM" src="https://github.com/user-attachments/assets/8168e9cf-34da-4705-aba2-bdffbb92cfbb" />
<img width="334" height="396" alt="Screenshot 2026-03-26 at 1 58 00 AM" src="https://github.com/user-attachments/assets/00df2837-2921-4603-b131-82766e7bc43b" />
<img width="332" height="391" alt="Screenshot 2026-03-26 at 2 01 20 AM" src="https://github.com/user-attachments/assets/38fd1bdb-dd59-4db6-a526-e172bb0151f8" />
<img width="331" height="393" alt="Screenshot 2026-03-26 at 2 02 06 AM" src="https://github.com/user-attachments/assets/29cb4249-20f4-409a-867c-8488216614cb" />
<img width="332" height="398" alt="Screenshot 2026-03-26 at 2 05 21 AM" src="https://github.com/user-attachments/assets/00006ade-32db-46cf-a28b-8e35cc9154d1" />
<img width="331" height="395" alt="Screenshot 2026-03-26 at 2 06 11 AM" src="https://github.com/user-attachments/assets/a508b3aa-3074-4064-b4b7-115737b8cf9e" />
<img width="329" height="396" alt="Screenshot 2026-03-26 at 2 07 53 AM" src="https://github.com/user-attachments/assets/38517949-8065-4b66-a1b2-3c92bbba5528" />
<img width="333" height="398" alt="Screenshot 2026-03-26 at 2 24 10 AM" src="https://github.com/user-attachments/assets/c8ff2dc8-cd2a-4cb7-9c54-b70d7284a501" />
<img width="330" height="392" alt="Screenshot 2026-03-26 at 2 25 38 AM" src="https://github.com/user-attachments/assets/3f4ac07c-91b9-47be-96f0-8ec30485d08e" />
<img width="336" height="398" alt="Screenshot 2026-03-26 at 2 27 59 AM" src="https://github.com/user-attachments/assets/275e2663-fe7d-440c-ab36-15cbde0476f3" />
<img width="329" height="394" alt="Screenshot 2026-03-26 at 2 28 51 AM" src="https://github.com/user-attachments/assets/fcf6368e-219e-453d-886a-b7dec1a76706" />


* Sorry, something's pretty controversial, isn't it? I mean the word MAMMY is referring to a mother in Irish English, not a stereotype associated with woman of African descent in the US. "Balls" is the plural of "ball", not testicles. "Willy" is an Australian slang for a sudden outburst of anger or annoyance, not a penis (UK English).


With using this method, it is easy to guarantee every puzzle within 6 guesses as the ceiling point. 

# Player's favourite (from NYT) (not fully tested, but I've been working with other best openers):
* `soare`: 3.462 Avg.
* `arose`: 3.466 Avg.
* `raise`: 3.468 Avg.
* `great`: 3.509 Avg.
* `dream`: 3.536 Avg.
* `house`: 3.580 Avg.
* `scowl`: 3.592 Avg.
* `adieu`: 3.623 Avg.
* `audio`: 3.637 Avg.

# Examples of traps and hard Wordle puzzles

(test only)

<img width="258" height="309" alt="Screenshot 2026-03-25 at 11 05 20 PM" src="https://github.com/user-attachments/assets/bd5cef22-ce52-4e6a-904e-6a1f1c952df2" />
(Wordle 1576)

<img width="260" height="308" alt="Screenshot 2026-03-25 at 11 05 56 PM" src="https://github.com/user-attachments/assets/5db2a2c7-85b8-4b70-aeb0-edabe68fd8f6" />
(Wordle 1214)

<img width="258" height="308" alt="Screenshot 2026-03-25 at 11 07 33 PM" src="https://github.com/user-attachments/assets/5511fe38-7f8e-40c2-a4a1-5d18440968ef" />
(Wordle 454)

<img width="260" height="308" alt="Screenshot 2026-03-25 at 11 09 12 PM" src="https://github.com/user-attachments/assets/3ce6266e-749f-4fac-8b17-f1ae929998ae" />
(Wordle 712) 

<img width="331" height="398" alt="Screenshot 2026-03-26 at 2 16 05 AM" src="https://github.com/user-attachments/assets/6ea6108c-3cf0-495f-b78a-881be000bdd8" />
(Wordle 265) 

<img width="329" height="396" alt="Screenshot 2026-03-26 at 2 17 31 AM" src="https://github.com/user-attachments/assets/a5f001eb-de15-4466-aea6-58e6689799f8" />
(Wordle 1052) 

<img width="335" height="395" alt="Screenshot 2026-03-26 at 2 18 22 AM" src="https://github.com/user-attachments/assets/eea9c438-9aa5-4d76-a0cb-a25b96dc00e8" />
(Wordle 1536)

Easy mode 14855 words, 2315 answers:

1.  `tarse`: 3.426 Avg. (Difference: —) (New word)
2.  `salet`: 3.427 Avg. (Difference: ±0)
3.  `slate`: 3.428 Avg. (Difference: -0.003)
4.  `trace`: 3.430 Avg. (Difference: -0.003)
5. `crane`: 3.431 Avg. (Difference: -0.001)
6. `reast`: 3.431 Avg. (Difference: -0.001)
7.  `crate`: 3.432 Avg. (Difference: ±0)

Repeatle (https://repeatle.netlify.app/) 

* `terse`: 3.305 Avg.
* `saree`: 3.325 Avg.
* `eerie`: 3.572 Avg.
* `qajaq`: 3.953 Avg.

Lewdle (5-letter) (Note: I won't show you the list of words due to sensitive context, you MUSTN'T click it!!) (not fully tested)

<details>
<summary><b>Click to show NSFW Word List</b></summary>

* `traps`: 3.082 Avg. / 3.099 Avg. (Hard mode)
* `cunts`: 3.113 Avg. / 3.141 Avg. (Hard mode)
* `penis`: 3.115 Avg. / 3.134 Avg. (Hard mode)
* `train`: 3.115 Avg. / 3.119 Avg. (Hard mode)
* `loins`: 3.117 Avg. / 3.145 Avg. (Hard mode)
* `shart`: 3.130 Avg. / 3.145 Avg. (Hard mode)
* `clits`: 3.130 Avg. / 3.161 Avg. (Hard mode)
* `barse`: 3.132 Avg. / 3.141 Avg. (Hard mode)
* `carse`: 3.136 Avg. / 3.147 Avg. (Hard mode)
* `farts`: 3.138 Avg.
* `boner`: 3.140 Avg.
* `score`: 3.147 Avg.
* `moist`: 3.157 Avg.
* `cakes`: 3.157 Avg.
* `spank`: 3.172 Avg.
* `arsed`: 3.176 Avg.
* `cheat`: 3.185 Avg.
* `chain`: 3.199 Avg.
* `ahole`: 3.216 Avg.
* `shits`: 3.231 Avg.
* `tease`: 3.233 Avg.
* `cream`: 3.235 Avg.
* `clamp`: 3.247 Avg.
* `slave`: 3.256 Avg.
* `fucks`: 3.266 Avg.
* `jizzy`: 3.686 Avg.

(6 letter Lewdle)
* `trains`: 2.803 Avg.

</details>

Easy mode (not fully tested) (4-letter words, based on hello wordl's word lists) Note: It is impossible to guarantee every puzzle to solve within 6 guesses, though the solve rate is very high, which is 99.4%. File: `Wordle Bot (Use) (customised4-letter)` (You can use the Wordle Word filterer project to filter a word list with a customised number of word length.)

1. `tela`: 4.267 Avg. (99.4% Solve rate)
2. `lean`: 4.284 Avg. (99.3% Solve rate)

Easy mode (6-letter words) File: `Wordle Bot (Use) (customised6-letter)` (not fully tested)

1. `salter`: 3.178 Avg. (5-guess: 23/4562, 6-guess: 0/4562)
2. `satire`: 3.184 Avg. (5-guess: 43/4562, 6-guess: 0/4562)
3. `trails`: 3.229 Avg. (5-guess: 41/4562, 6-guess: 0/4562)

Easy mode (7-letter words) File: `Wordle Bot (Use) (customised7-letter)` (not fully tested)

1. `saltire`: 2.904 Avg. (5-guess: 1/5137, 6-guess: 0/4562)

Easy mode (8-letter words) File: `Wordle Bot (Use) (customised8-letter)` (not fully tested)

1. `ceratins`: 2.718 Avg. (Max 4 Guesses)

Easy mode (9-letter words) File: —

1. `coastline`: 2.535 Avg. (Max 4 Guesses)

Easy mode (10-letter words) File: —

1. `centralise`: 2.366 Avg. (Max 4 Guesses)

Easy mode (11-letter words) File: —

1. `unclarities`: 2.282 Avg. (Max 3 Guesses)

Easy mode (12-letter words) File: —

1. `centralities`: 2.159 Avg. (Max 3 Guesses) (note not fully tested)

Easy mode (13-letter words) File: —

1. `uncertainties`: 2.089 Avg. (Max 3 Guesses)

Easy mode (14-letter words) File: —

1. `penitentiaries`: 2.049 Avg. (Max 3 Guesses)

Easy mode (15-letter words) File: —

1. `unceremoniously`: 2.012 Avg. (Max 3 Guesses)

Hard mode (4-letter words) 

1. `tela`: 4.686 Avg. (89.62% solve rate)
2. `lehr`: 4.745 Avg. (89.66% solve rate)

* Method 2

1. Calculating the average guesses left by the pairs shared in each words

<img width="712" height="344" alt="Screenshot 2026-03-28 at 6 49 14 PM" src="https://github.com/user-attachments/assets/d581028f-34c1-4bca-810f-439d0e54ab82" />

2. Calculating the minimum pair of all the pairs shared in the word (MINIMAX)

<img width="712" height="298" alt="Screenshot 2026-03-28 at 6 59 41 PM" src="https://github.com/user-attachments/assets/deed10b7-cc8a-4cea-9436-0bd2124204d5" />

3. Calculating the number of isolated pairs with 1 word only

<img width="711" height="267" alt="Screenshot 2026-03-28 at 7 00 59 PM" src="https://github.com/user-attachments/assets/61dcfa89-2982-4c5a-9316-358beb49698f" />

# Spotle Bot (similar to Wordle Bot Player Usage, but X means a spot (black letter))

`[2315 words remaining]`

`slate gxgxg`

`[24 words remaining]`

`cloth xyx__`

`[1 words remaining]`

`scale ggggg`

For the board, type a code like `0101010100010011001000101`, 0 = white, 1 = black.

(Whole processing: about 30 minutes or even hours for each word)

https://github.com/marcoT0425/Wordle_Solver/blob/main/Spotle%20Bot.sb3 

I'll be making:

1. `parse + clint` / `other + nails` etc
2. `stead,flung,chirp,womby` / `brick,glent,jumpy,vozhd,waqfs` / `brick,flame,shunt,podgy`

Should you have any problems, please contact me by email: mankotoa@gmail.com or to open an issue.

## Credits and acknowledgements:

This project was heavily influenced by the following works:

**[What's the Hardest Answer in Wordle?](https://www.youtube.com/watch?v=QZ21ey0RPSA&t=30s)** by [@Pokecheese](https://www.youtube.com) 
    *   *Contribution:* Provided the methodology for assessing "hardness" using human gameplay simulations and obscurity metrics.

**[Oh, wait, actually the best Wordle opener is not “crane”…](https://www.youtube.com/watch?v=fRed0Xmc2Wg&t=323s)** by [@3Blue1Brown](https://www.youtube.com) 
    *   *Contribution:* Provided the entropy maximising algorithm and the best opener words in Wordle.
