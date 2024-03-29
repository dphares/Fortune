import random
import os

#main accepts 1 or 0 as an argument.
#1 will cause the function to return it's value, whereas
#0 will cause the compiler to initialize for the first roll
def rolestart():
      main(0)


def main(m):
      global rolls
      rolls = []
      rollcount = 0
      while rollcount < 3:
            roll = random.randint(1,6)
            value = dice()
            rolls.append(value)
            rollcount = rollcount + 1
      if rollcount == 3 and m == 1:
            return rolls
      if rollcount == 3 and m == 0:
            compiler(rolls, 0)


#x is input in the form of a rolls list, u is a tracker to skip unecessary execution
#
def compiler(x, u):
      global image
      #dicecount is used to track which dice is currently being printed
      #
      dicecount = 0
      #linecount is used to track the line currently being printed on
      #
      linecount = 0
      image = 'Your rolls: \n'
      while linecount < 6:
            #Image editing line adds the current line of the current dice tracked by line/dice counter
            #After adding one line of one dice, it adds one to dicecount, and adds the same line of the next dice
            image = image + (x[dicecount][linecount])
            dicecount = dicecount + 1
            #After all three die of one row are added, a line break is added and linecount gains one, while dicecount
            #is reset, to begin drawing the next line of all three die
            #After all six lines are drawn, the program exits to the end function
            if dicecount == 3:
                  dicecount = 0
                  linecount = linecount + 1
                  image = image + '\n'
      #If the function was called for the first time, call it with 0 for u in order to initiate the inputmanager
      # and exchange or 1 to trigger the function's return
      if u == 0:
            printer(image)
            print ('Would you like to reroll any of your dice?')
            inputone = inputmanager(1)
            if inputone == 0:
                  end()
            #If the player chooses to replace one or two of their dice, this will initiate the exchanger function
            #
            if inputone == 1:
                  exchanger()
      if u == 1:
            return image

#Input manager handles any non-mechanical aspects of the program. It accepts an integer as argument to trigger
#specific prompts.
def inputmanager(z):
      #z1 is used to collect yes/no responses in appropriate format, and will return a 1 for yes, or a 0 for no
      #
      if z == 1:
            while True:
                  yesno = input('Input [Y/N]\n')
                  if yesno.lower() != 'y' and yesno.lower() != 'n':
                        yesno2 = input(
                              'Please input [Y] or [N]\n')
                        if yesno2.lower() == 'n':
                              return 0
                        if yesno2.lower() == 'y':
                              return 1
                  if yesno.lower() == 'n':
                        return 0
                  if yesno.lower() == 'y':
                        return 1
      #z2 is used to determine which of the players dice that they would like to re-roll. z2 ensures the input is
      #a valid integer between 1 and 3, then returns that input.
      if z == 2:
            while True:
                  choice = input('Which of the three die do you wish to replace?\n')
                  try:
                        isinstance(choice, int)
                        if int(choice) > 3 or int(choice) < 1:
                              print('Please input a number between one and three.')
                        if int(choice) == 1:
                              return int(choice)
                        if int(choice) == 2:
                              return int(choice)
                        if int(choice) == 3:
                              return int(choice)
                  except:
                        print("That wasn't even a number!")
      #z3 is used to restart, or close the program
      #
      if z == 3:
            retry = input('Enter to escape.' + '\n' + 'R to reroll.' + '\n')
            if retry.lower() == 'r':
                  main(0)
            else:
                  raise SystemExit

#Exchanger creates a copy of the original roll list and saves it to be later spliced with replacements generated by
#player's input during the inputmanager2 script. Exchanger will invoke the input manager first to see if the player
#wishes to reroll a second die, and second, to determine which die that is.
#The player's choices will be stored in a list 'replacements'. The items in replacements are used to determine which
#die should be spliced out from the newrolls list generated by feeding the main function '1', and which die to keep.
#The final image of the new die the player chose to replace with the old they didn't is compiled and
#stored as newimage, then given to the printer.
def exchanger():
      originalrolls = rolls
      replacements = [inputmanager(2)]
      print('Would you like to reroll another die?')
      confirm = inputmanager(1)
      if confirm == 1:
            replacements.append(inputmanager(2))
      rr = len(replacements)
      newrolls = main(1)
      if rr == 1:
            originalrolls[replacements[0] -1] = newrolls[0]
      if rr == 2:
            originalrolls[replacements[0] -1] = newrolls[0]
            originalrolls[replacements[1] -1] = newrolls[1]
      newimage = compiler(originalrolls, 1)
      printer(newimage)
      end()


def comparison():
      pass


def printer(i):
      print ('```' + '\n' + i + '\n' + '```')


def end():
      inputmanager(3)


def dice():
      #Contains art for the die in the format of a list to be parsed by the printer function
      #
      roll = random.randint(1,6)
      d1 = ["  _______  ",
            " /       \ ",
            " |       | ",
            " |   0   | ",
            " |       | ",
            " \_______/ "]
      d2 = ["  _______  ",
            " /       \ ",
            " |     0 | ",
            " |       | ",
            " | 0     | ",
            " \_______/ "]
      d3 = ["  _______  ",
            " /       \ ",
            " |     0 | ",
            " |   0   | ",
            " | 0     | ",
            " \_______/ "]
      d4 = ["  _______  ",
            " /       \ ",
            " | 0   0 | ",
            " |       | ",
            " | 0   0 | ",
            " \_______/ "]
      d5 = ["  _______  ",
            " /       \ ",
            " | 0   0 | ",
            " |   0   | ",
            " | 0   0 | ",
            " \_______/ "]
      d6 = ["  _______  ",
            " /       \ ",
            " | 0   0 | ",
            " | 0   0 | ",
            " | 0   0 | ",
            " \_______/ "]

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


def envselect():
      if 'discord_bot_token' in os.environ:
            output = rolestart()
            return output


envselect()