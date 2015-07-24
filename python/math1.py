# import math
#
# def square(value):
#     return value*value
#
# def area(radius):
#     return 3.14*(radius**2)
#
# def cir(radius):
#     return 2*3.14*radius
#
# def distance(x1,y1,x2,y2):
#     x=(x1-x2)**2 + (y1-y2)**2
#     return math.sqrt(x)
#
# print square(2)
# print area(2)
# print cir(2)
# print distance (3,0,0,5)

# def reverse(list):
#     temp=[]
#     index=len(list)
#     for item in list:
#         temp[item]=list[index-1]
#         index=index-1
#         list=temp
#     return list


# def reverse(list):
#     temp = []
#     index = 1
#     while index <= len(list):
#         temp.append(list[- index ])
#         index += 1
#     return temp
#
# print reverse([1,2,3,4,5])

# sandwich = [["rye", "sourdough", "baguette"],[["ham", "salami", "turkey"],
# ["swiss", "munster", "cheddar"]],["mayo", "mustard", "tabasco"]]

# print sandwich[0][1][4] #sourdough
# print sandwich[1] #ham, salami, turkey
# print sandwich[1][0][0] #ham
#
# print sandwich[2]
# print sandwich [1][1][2]
# print sandwich [0][1]

city_info = {'new_york' : { 'mayor' : "Bill DeBlasio",
                            'population' : 8337000,
                            'website' : "http://www.nyc.gov"
                            },
             'los_angeles' : { 'mayor' : "Eric Garcetti",
                            'population' : 3884307,
                            'website' : "http://www.lacity.org"
                            },
             'miami' : { 'mayor' : "Tomas Regalado",
                            'population' : 419777,
                            'website' : "http://www.miamigov.com"
                            },
             'chicago' : { 'mayor' : "Rahm Emanuel",
                            'population' : 2695598,
                            'website' : "http://www.cityofchicago.org/"
                            }
        }
# print city_info["los_angeles"] # { 'mayor' : "Eric Garcetti",
#             #    'population' : 3884307,
#             #    'website' : "http://www.lacity.org"
# print city_info["chicago"]["mayor"] #Rahm Emanuel
# print city_info["new_york"]["population"]
# print city_info["miami"]["website"]
# print city_info["los_angeles"]["mayor"]
# print city_info["chicago"]

def parse(dictionary):

    for item in dictionary:
        for item1 in dictionary[item]:
            print "The " + item1 + " of " + item + " is " + str(dictionary[item][item1])

parse(city_info)
