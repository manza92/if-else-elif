'''a = 93
b = 27
if a >= b:
    print(a)

    a = 24
b = 44
if a <= 0:
    print(a)
print(b)

a = 27
b = 93
if a >= b:
    print(a)
else:
    print(b)

a = 27
b = 93
if a <= b:
    print("a is less than or equal to b")
elif a == b:
    print("a is equal to b")

a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b")

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

object_size = 10
if object_size > 5:
    print('We need to keep an eye on this object')
else:
    print('Object poses no threat.')

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)

object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')

fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

multiline = "Facts about the Moon:\nThere is no atmosphere.\nThere is no sound."
print(multiline)

multiline = """Facts about the Moon:
 There is no atmosphere. 
 There is no sound."""
print(multiline)

print("temperatures and facts about the moon".title()) 

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)  

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list) 

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list) 

print("Moon" in "This text will describe facts and challenges with space travel")

print("Moon" in "This text will describe facts about the Moon") 
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper())

print("The Moon And The Earth".lower().count("the")) 
 
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1]) 

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

        print("-60".startswith('-')) 

    if "30 C".endswith("C"):
        print("This temperature is in Celsius") 


print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")) 

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))


text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split('. ')

for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence) 

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage) 

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth")) 

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))	

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))


print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.") 

print(round(100/6, 1))

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)   '''

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {Ganymede}: {gravity} m/s2"""
print(template.format(name=name, planet=planet, gravity=gravity))