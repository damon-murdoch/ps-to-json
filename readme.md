# Showdown Set to JSON Converter
## An application for converting showdown sets to json, written in Python.
### Developed by Damon Murdoch ([@SirScrubbington](https://twitter.com/SirScrubbington)).

### Summary
This Python application was developed for the 
simplification of creating the .json files required
for Pokemon Showdown! Server randomised formats. This
application converts all of the (valid) files in the 
/in directory to .json files and saves them in the /out
directory by default. 

### Expected Format
The Expected Format for input sets is as follows:

Species @ Item 1 / Item 2 / ...
Ability: Ability 1 / Ability 2 / ...
EVs: n HP / n Atk / n SpD / ...
IVs: n Atk / n Spe / ....
Nature 1 / Nature 2 / ... nature
- Move 1 / Move 2 / ...
- Move 1 / Move 2 / ...
- Move 1 / Move 2 / ...
- Move 1 / Move 2 / ...

### Sample Files
Inside the /in directory, I've placed the 
resource files which are currently being used
on my own private Pokemon Showdown! server for
my VGC Battle Factory format(s). This is also
the official repository for these files. Please
feel free to push changes to this repository 
which add new sets you would like to see in 
the server and I will review them :) 

### Credits
VGC Factory Sets have been sourced, in no particular order from:
* Smogon Usage Stats ([link](https://smogon.com/stats))
* Dawoblefet's VGC Room Tour Sample Teams ([link](https://pastebin.com/rhFBBMMB))
* Nugget Bridge VGC Team Reports ([link](https://nuggetbridge.com))
* Trainer Tower Sample Sets / Team Reports ([link](https://trainertower.com))
* My Personal Blog ([link](https://sir-scrubbington.hatenablog.com))

## Future Changes
A list of future planned fixes / improvements are listed below.

### Change Table

| Change Description     | Priority |
| ---------------------- | -------- |
| Allow Shiny True/False | High     |
| Allow Level 1-100      | High     |

### Problems / Improvements
If you have any suggested improvements for this project or you encounter any issues, please feel free to open an issue [here](https://github.com/damon-murdoch/set-scheduler/issues) or send me a message on twitter detailing the issue and how it can be replicated.

## Sponsor this Project
If you'd like to support this project and other future projects, 
please feel free to use the paypal domation link below.

https://www.paypal.com/paypalme/sirsc
