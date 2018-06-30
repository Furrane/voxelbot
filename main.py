import pyautogui
import time


# Locating the game window

pyautogui.alert('Put the mouse pointer over the top left corner of the game then press "Enter"')
TOP_LEFT = pyautogui.position()

pyautogui.alert('Put the mouse pointer over the bottom right corner of the game then press "Enter"')
BOT_RIGHT = pyautogui.position()

DIM = (BOT_RIGHT[0] - TOP_LEFT[0], BOT_RIGHT[1] - TOP_LEFT[1])

print(TOP_LEFT,BOT_RIGHT,DIM)

# Generating the positions

QSKILL = (0.3*DIM[0]+TOP_LEFT[0], 0.9*DIM[1]+TOP_LEFT[1])
WSKILL = (0.4*DIM[0]+TOP_LEFT[0], 0.9*DIM[1]+TOP_LEFT[1])
ESKILL = (0.5*DIM[0]+TOP_LEFT[0], 0.9*DIM[1]+TOP_LEFT[1])
RSKILL = (0.6*DIM[0]+TOP_LEFT[0], 0.9*DIM[1]+TOP_LEFT[1])
SKILLS = [QSKILL,WSKILL,ESKILL,RSKILL]

SLOTZ = [[( (0.1+(i*0.07))*DIM[0]+TOP_LEFT[0], (0.26+(j*0.125))*DIM[1]+TOP_LEFT[1] )for i in range(5)]for j in range(6)]
SLOTS = [None,]
for line in SLOTZ:
    SLOTS += line

# Tool functions

def use(slot, chest = False):
    pyautogui.moveTo(SLOTS[slot][0], SLOTS[slot][1])
    time.sleep(.1)
    pyautogui.click()
    pyautogui.moveRel(0.194*DIM[0], 0.185*DIM[1])
    time.sleep(.1)
    pyautogui.click()
    if chest :
        pyautogui.moveTo(0.7*DIM[0]+TOP_LEFT[0], 0.5*DIM[1]+TOP_LEFT[1])
        time.sleep(.4)
        pyautogui.click()

def sell(slot):
    pyautogui.moveTo(SLOTS[slot][0], SLOTS[slot][1])
    time.sleep(.1)
    pyautogui.click()
    pyautogui.moveRel(0.084*DIM[0], 0.198*DIM[1])
    time.sleep(.1)
    pyautogui.click()

def equip(slot):
    pyautogui.moveTo(SLOTS[slot][0], SLOTS[slot][1])
    time.sleep(.1)
    pyautogui.click()
    pyautogui.moveRel(0.192*DIM[0], 0.198*DIM[1])
    time.sleep(.1)
    pyautogui.click()


def open_chest(slot, n):
    for i in range(n):
        use(slot, chest=True)
        



running = True

while running :

    userinput = pyautogui.prompt(text = '1 - Open Chests \n2 - Sell items\n 9 - Quit', title = 'What do you want to do ?')
    
    if userinput == '1':
        i = pyautogui.prompt(text='Print the slot number (1 to 30) of the chest followed by the number of chests to open. Example : 5 20').split()
        open_chest(int(i[0]), int(i[1]))

    elif userinput == '2':
        i = pyautogui.prompt(text='Write the starting and end slot (inclusive) of the items you want to sell, EVERYTHING in between will be sold !').split()
        start, end = int(i[0]), int(i[1])
        for slot in range(start, end+1):
            sell(slot)

    else :
        running = False