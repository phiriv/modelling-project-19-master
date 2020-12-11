[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=309629&assignment_repo_type=GroupAssignmentRepo)

# CISC/CMPE 204 Modelling Project

Welcome to our group's repository for the CISC 204 final project! We decided to logically model a turn-based board game called the Resistance, where the objective of the players on each of the 2 teams is to deceive the others about their allegiance in order to win rounds by playing hidden tokens. The tricky Spies can sabotage missions but they are outnumbered which makes for an interesting model counting challenge. A major addition to increase the complexity of the project was to compute the likelihood of winning at each of the 5 rounds by counting the number of valid models and dividing by the total. Relevant folders include /images and /documents/final.

## Structure

* `documents`: Contains folders for both of your draft and final submissions. README.md files are included in both.
* `images`: screenshots & figures used for the final report
* `run.py`: General wrapper script that you can choose to use or not. Only requirement is that you implement the one function inside of there for the auto-checks.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.
