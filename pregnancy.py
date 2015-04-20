from sys import argv
from sys import exit

scrpit, in_file = argv

print "Let's start by typing in your name so that I know how to address you"
name = raw_input("Name? ")
    

def start_menu():

    print "-" * 70
    print "Hi, %s, Welcome to your Pregnany Program 0.0.1" % name
    print "Please choose a number from the menu options below:\v\v"
    print "1. Keyword prompt (ask the program any question)"
    print "2. Back Pain"
    print "3. Headache"
    print "4. Fatigue"
    print "5. Suggested Food List"
    print "6. Staple Herbs\v\v"
    print "-" * 70
    print "Exit the program at anytime by pressing CTRL C."
    
    choice = raw_input("> ")
    
    if "1" in choice:
        keyword()
    elif "2" in choice:
        backpain()
    elif "3" in choice:
        headache()
    elif "4" in choice:
        fatigue()
    elif "5" in choice:
        greenlist()
    elif "6" in choice:
        herbs()
    else:
        start_menu()

def herbs():
    with open(in_file, 'r') as herbread:
        print herbread.read()
    print "\vWould you like to add herbs to this list? (y/n)"
    
    ynherb = raw_input("> ")

    if "y" in ynherb:
        print "Ok, type the herb(s) you'd like to add:"
        addherb = raw_input("> ")

        with open(in_file, 'a+') as herbfile:
            herbstring = "%s\n" % addherb
            herbfile.write(herbstring)

            print herbfile.read()

        whatelse()
    
    else:
        start_menu()
        

def backpain():
    print """
%s, your body's center of gravity is shifting as it changes and it also is taking on some weight.  Additionally, your kidneys are doing extra work with the increase in blood volume being processed.
    a. Practice good posture, focusing on engaging your abdominal 
       muscles.  Strong abdominals take the pressure off of the 
       back.
    b. Practice cat/cow posture, breathing deeply and rhythmically.
    c. Calcium and magnesium through diet help diminishe back pain
    d. Help the kidneys with herbs (nettle and comfrey) and 
       by drinking lemon juice in water, several times per day.
    e. Specifically for muscle spasms, take 15-25 drops 
       St. John's wort tincture in water, or rub St. John's
       wort infused oil directly on skin.
""" % name
    whatelse()


def headache():
    print """
    a. Apply warm and cool packs to affected area of head or neck
    b. Eat a little bit throughout the day to maintain blood sugar
    c. Stay hydrated
    d. Rest in a dark room and practice deep breathing
    e. Take a warm shower or bath
    f. Regular walking or light exercise to improve blood
       circulation
"""
    whatelse()


def fatigue():
    print "%s, let me remind you that fatigue is both mental and physical.  You are growing a complete human inside of you!!!  Simultaneously, you brain is busy preparing for this child and it itself changing for a new segment of your life's journey.  It's more than ok that you're tired, so get as much rest as you want." % name

    print "That being said, your body needs plenty of minerals and vitamins."
    print """
    Here are some suggestions:
    a. Take one to two tablespoons of spirulina daily
    b. Take Floradix or similar iron formula. Iron is best taken 
       through food and herbal preparations
    c. Seaweeds and greens
    d. Iron tonic tea:
        Equal parts Yellow Dock root, Nettle Leaf, and Raspberry 
        leaf.  Infuse 2 tablespoons of this mix per cup of water 
        and allow to steep 2 hours.
"""
    whatelse()


def whatelse():
    print "Would you like to return to"
    print "1. Return to Menu"
    print "2. Exit Program"

    menorex = raw_input("> ")

    if "1" in menorex:
        start_menu()
    elif "2" in menorex:
        exit(0)
    else:
        whatelse()


green = ['greens & veg', 'seaweeds', 'romaine', 'celery', 'spinach', 'heirloom lettuces', 'chards', 'sprouts', 'bell peppers', 'spirulina', 'meats', 'sardines', 'salmon', 'bison', 'grass-fed beef', 'duck', 'lamb', 'nuts, beans, & seeds', 'almonds', 'edamame', 'lentils',  'black beans', 'kidney beans', 'tofu', 'nut & seed butters', '100% whole-grain breads, cereal, & pasta', 'wild or brown rice', 'dairy & eggs', 'cow & goat yogurt', 'cow & goat cheese (raw and pasteurized)', 'duck eggs', 'truly pasture-raised chicken eggs', 'fruit', 'dried figs',   'strawberries', 'raspberries', 'blackberries', 'blueberries', 'papaya', 'oranges and mandarins', 'apples', 'pears', 'bananas', 'dates', 'raisins', 'Herbs, Spices, & Sweeteners', 'dark chocolate', 'cinnamon', 'cocoa', 'garlic & onions', 'honey', 'blackstrap molasses', 'turmeric', 'red raspberry leaf', 'comfrey', 'motherwort', 'yellow dock root', 'burdock root', 'chamomile']

yellow = ['\tbutter', '\tcakes and cookies (with 100% whole-grain flour)', '\tFast food /fatty meats', '\tfrench fries', '\tfrozen yogurt', '\t100% fruit juice', '\tice cream', '\tPasta from white flour', '\twhite bread', '\twhite rice']

red = ['\tcorn syrup', '\tartificial dyes', '\tartificial sweeteners', '\thydrogenated oils', '\tnitrit-containing cold cuts % hot dogs', '\thigh-fat, low-fiber baked goods']


def greenlist():
    for gf in green:
        print "%s" % gf
    print "Would you like to see \"yellow-light\" foods that should be consumed moderately?"
    yl = raw_input("y\\n?")
    if "y" in yl:
        for yf in yellow:
            print "%s" % yf
    print "Would you like to see \"red-light\" foods that should not be consumed?"
    rl = raw_input("y\\n?")
    if "y" in rl:
        for rf in red:
            print "%s" % rf
        whatelse()
    else:
        start_menu()

def keyword():
    while True:
        print "Type in your keyword or question"
        i = raw_input("> ")

# page 12 of herbal course

        if "migraine" in i or "headache" in i or "head" in i:
            headache()

        elif "back" in i:
            backpain()

        elif "food" in i or "eat" in i:
            print "Here are some nutrient-packed food suggestions."
            greenlist()

        else:
            print "I'm sorry I didn't understand, try rephrasing your inquiry."


start_menu()

   # elif "1st" in i and "week" in i or "first" in i and "week" in i, or "1" and "week" in i:

  #  elif "2nd" in i and "week" in i or "2" in i and "week" in i or "second" in i and "week" in i:
        
# weeks by pregnancy and trimester     
# further elif subjects: back pain, swelling, foods to avoid, herbs to avoid, substances to avoid, stress, insomnia, hemorrhoids, heartburn, 
# page 46 for nutrition requirements and food sources
# Audrey needs to be able to tell program which week or month she is in and get a response with suggestions for that segment of pregnancy.
# create a for-loop regarding green, yellow, red light foods, herbs, and substancesre
# lists of herbal and foods sources of vitamins and minerals
    
# herbal shopping list: 

# feeling tired/ fatigue:
