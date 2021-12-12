cats = 10
cans = 3
#calculation for the amount of cans needed to feed 10 cats
print(cans * cats)
#the total amount of cans needed to feed 10 cats in one day
total_cans = cans * cats
#the total amount of cats needed to feed 10 cats in 7 days
print(total_cans * 7)
#sentence that says 10 cats eat 30 cans
output = str(cats) + " cats eat " + str(total_cans) + " cans"
print(output)
days = 5
#the total amount of cans needed to feed 10 cats in 5 days - variable days with the value of 5 has been added instead of simply stating the number 7 as per line 8
total_cans = cans * cats * days
msg = str(cats) + " cats eat " + str(total_cans) + " cans in " + str(days) + " days"
print(msg)
oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = "{} oranges costs £{}" .format(oranges, total_cost)
print(output)
msg = "{} cats eat {} cans in {} days".format(cats, total_cans, days)
print(msg)
days = 31
hours = 24
total_hours = days * hours
msg = "There are {} in {} days".format(total_hours, days)
print(msg)
