import secrets
#import colorama
# -100 total war, -25 to 25 neutral, 100 best allies can be
weather = {}
# data = input("Enter data.txt file path")
# with open(data) as pdata:
#     fdata = pdata.readline()
# for i in fdata:
#     i.split('<')
with open("spring.txt") as spring:
    springL = spring.readlines()
with open("summer.txt") as summer:
    summerL = summer.readlines()
with open("fall.txt") as fall:
    fallL = fall.readlines()
with open("winter.txt") as winter:
    winterL = winter.readlines()
for q in springL:
    w = q.split('|')
    w.pop()
    x = w.pop(0)
    weather[x] = w
for q in summerL:
    w = q.split('|')
    w.pop()
    x = w.pop(0)
    weather[x] = w
for q in fallL:
    w = q.split('|')
    w.pop()
    x = w.pop(0)
    weather[x] = w
for q in winterL:
    w = q.split('|')
    w.pop()
    x = w.pop(0)
    weather[x] = w

print(list(weather))


def weatherf():
    print("1: Check current date/weather/temperature, 2: Change day/weather/temperature (updates relations and populations)")
    dm = int(input("What would you like to do?"))
    currweather = 'clear'
    if dm == 1:
        print(" ")
        print(currweather)
    elif dm == 2:
        print(" ")
        x = int(input("How many days would you like to advance?"))
        #for i in range(x):
            #populationu()
            #factionu()
        newWeather = weatheru()
    elif dm == 3:
        print("")

def weatheru():
    c = ['Coast', 'Tundra', 'Wasteland', 'Volcanic', 'Snowpeak', 'Mountain', 'Shale', 'Hills', 'Jungle', 'Evergreen forest','Deciduous forest', 'Dense forest', 'Plains', 'Marsh', 'Swamp', 'Sandy Desert', 'Rocky Desert', 'Dune', 'Scrub']
    output = [] #list of tuples
    print("Seasons: S, SU, F, WI")
    print("Magical Levels: N, L, H (N means natural)")
    s = str(input("Season?"))
    me = ['n', 'N', 'n', 'N', 'L', 'H']
    m = str(secrets.choice(me))
    for i in c:
        m = str(secrets.choice(me))
        clim = weather[str(i) + str(s) + str(m)]
        CW = secrets.choice(clim)
        print("your weather for", i, "is ", CW)
        jkl =  i + " " + CW
        output.append(jkl)
        dt = secrets.randbelow(11)  # need jesse's input on how big of a table
        pm = secrets.randbelow(3)
        if pm == 1:
            dt -= dt * 2
            print(dt, "F")
        elif pm == 2:
            print("+",dt, "F of change")

    #m = str(input("Magical?"))



    return output


# def faction():
#     x = 0
#     print("1: view faction information, 2: edit one faction's stats, X: return to main menu")
#     if x = 'X':
#         return
#     elif x = 1:
#         print(fInfo)
print("1: Date system Weather and Temperature, 2: Faction Relations and Populations, 3: Language Progress")
x = int(input("Mode?"))

if x == 1:
    weatherf()
# elif x == 2:
#     faction()
# elif x == 3:
#     progress()
#elif x == "" :
    #print("REEEEEEEEEEE")