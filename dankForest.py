hasSword = 0;

def areaWrite(text,options):
    
    for i in text:
        print(">" + i + "\n");

    j = 0;
        
    for i in options:
        j = j + 1;

        print(str(j) + ". " + i)
        
def dankForest():
    
    text = ["You are in the dankest of forests","tbh","You can hear a unicycle to your left","There is a faint smell of Mountain Dew and Doritos to your right","Which way do you turn?"];
    options = ["left","right"];

    areaWrite(text, options);

    i = int(input("???"));

    if i == 1:
        datBoi();
    elif i == 2:
        cave();
    else:
        "????????"

def datBoi():

    text = ["You see a figure aproach out of the fog", "You think out loud \"It's dat boi!!!\"", "He shouts \"O SHIT WADDUP\""];
    options = ["combat", "flee"];

    areaWrite(text,options);

    i = int(input("???"));

    if i == 1:
        datCombat();
    elif i == 2:
        dankForest();
    else:
        "????????"
def datCombat():

    text = ["What method of battle do you pursue?"];
    options = ["Unicycle race", "Dab off"];

    areaWrite(text,options);

    i = int(input("???"));

    if i == 1:
        lose();
    elif i == 2:
        dabOff();
    else:
        "????????"
def lose():

    print(">Y o u  l o s e ,  b o i");
    print("tbh");

    import sys;

    sys.exit;

def dabOff():

    text = ["Dat boi dies","His last words are \"get rekt m8, 8 out of 8\"","Behind him, you see a treasure chest"];
    options = ["Open the chest","Continue on your journey","Chase the bumblebee"];

    areaWrite(text,options);

    i = int(input("???"));

    if i == 1:
        chest();
    elif i == 2:
        dankForest();
    elif i == 3:
          bee();
    else:
        "????????"

def bee():

    print("You thought it was bee \n but is doggo \n \n \n bumboozled again!");

    lose();

def chest():

    global hasSword;
    hasSword = 1;
    
    text = ["It's a sheild", "made from a steel beam"];
    options = ["Go back"];

    areaWrite(text,options);

    i = int(input("???"));

    if i == 1:
        dankForest();
    else:
        "????????"
def cave():

    text = ["From the corner of the room you hear", "Strateegeree","Suddenly a wild George W. Bush Jr. appears!!!"];
    options = ["Combat", "Flee"];

    areaWrite(text,options);

    i = int(input("???"));

    if i == 1:
        georgeCombat();
    elif i == 2:
        print(">Suddenly, Donald Drumpf's Wall appears behind you \n>You can no longer escape Iraq!!!");

        georgeAttacks();
    else:
        "????????"

def georgeCombat():

    text = ["You yell at George \"Fool me twice, won't get fooled again!!!\"","George is now enraged!!!"];
    options = [];

    georgeAttacks();

def georgeAttacks():

    global hasSword;
    
    print(">George throws a bucket of burning jet fuel at you!!!");

    if hasSword == 0:
        lose();
    elif hasSword == 1:
        pepe();

def pepe():

    text = ["Jet fuel can't melt Steel beams!!!","George Bush flees to South America"," Slowly Pepe descends from the ceiling slowly whistling mad world by tears for fears", "He crawls at you backwards ,looks up at you, and says \"It's just a prank bro....\"","You die"]
    options = [];

    areaWrite(text,options);

    print("The philosiphers have only interpreted the world, in various ways: the point, however, is to change it. \n \n        ~Carl Marks \n \n \n");

    lose();
    
dankForest()
   

        
