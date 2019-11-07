import random

def main():
      #rolls list will contain the value of all 3 dice rolls, stored as a list that comprises an image of the
      #corresponding roll to be parsed by the printer function
      rolls = []
      #rollcount is used to terminate the main process after all three dice have been rolled and stored, pushing
      #the program on to the printer to process the rolls list in to an image
      rollcount = 0
      while rollcount < 3:
            #roll variable is established to pull the appropriate image from dice function
            roll = random.randint(1,6)
            value = dice(roll)
            #List append adds the rolled dice as its image to the list of rolls
            rolls.append(value)
            rollcount = rollcount + 1
      if rollcount == 3:
            #Feed all three rolls in the list to the printer function
            printer(rolls)

def printer(rolls):
      #dicecount is used to track which dice is currently being printed
      dicecount = 0
      #linecount is used to track the line currently being printed on
      linecount = 0
      image = 'Your rolls: \n'
      while linecount < 6:
            #Image editing line adds the current line of the current dice tracked by line/dice counter
            #After adding one line of a dice, it adds one to dicecount, and adds the same line of the next dice
            image = image + (rolls[dicecount][linecount])
            dicecount = dicecount + 1
            #After all three die of one row are added, a line break is added and linecount gains one, while dicecount
            #is reset, to begin drawing the next line of all three die
            #After all six lines are drawn, the program exits to the end function
            if dicecount == 3:
                  dicecount = 0
                  linecount = linecount + 1
                  image = image + '\n'

      print(image)
      end()





def end():
      retry = input('Enter to escape.' + '\n' + 'R to reroll.')
      if retry.lower() == 'r':
            main()
      else:
            raise SystemExit






def dice(roll):
      #Contains art for the die in the format of a list to be parsed by the printer function
      d1 = ['   ________  ',
            ' /         \ ',
            ' |         | ',
            ' |    0    | ',
            ' |         | ',
            ' \_________/ ']
      d2 = ["   ________  ",
            " /         \ ",
            " |      0  | ",
            " |         | ",
            " |  0      | ",
            " \_________/ "]
      d3 = ["   ________  ",
            " /         \ ",
            " |      0  | ",
            " |    0    | ",
            " |  0      | ",
            " \_________/ "]
      global d4
      d4 = ["   ________  ",
            " /         \ ",
            " |  0   0  | ",
            " |         | ",
            " |  0   0  | ",
            " \_________/ "]
      d5 = ["   ________  ",
            " /         \ ",
            " |  0   0  | ",
            " |    0    | ",
            " |  0   0  | ",
            " \_________/ "]
      d6 = ["   ________  ",
            " /         \ ",
            " |  0   0  | ",
            " |  0   0  | ",
            " |  0   0  | ",
            " \_________/ "]

      if roll == 1:
            return d1
      if roll == 2:
            return d2
      if roll == 3:
            return d3
      if roll == 4:
            return d4
      if roll == 5:
            return d5
      if roll == 6:
            return d6

main()