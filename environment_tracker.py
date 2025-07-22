number_of_showers_per_week = input("How many showers do you take per week?")
print(number_of_showers_per_week)

how_long_are_average_showers = input("How long are your average showers?")
print(how_long_are_average_showers)

amount_of_gallons_total_from_showers = int(how_long_are_average_showers) * 2
# calculates total amount of gallons by multiplying input 
# for average shower length by 2 
print("You use an average of",amount_of_gallons_total_from_showers,"gallons per shower.")

weekly_gallons_from_showers = int(amount_of_gallons_total_from_showers) *7

number_of_meals_per_week = input("How many meals do you eat weekly?")
print(number_of_meals_per_week)

total_dishes_per_week = int(number_of_meals_per_week) * 5
print("The total amount of dishes used to make all of your weekly meals is about",total_dishes_per_week)
# used 5 is average amount of dishes 
# used to make each meal 

gallons_used_with_dishwasher = int(total_dishes_per_week) / 3.5
print("You use a total of",gallons_used_with_dishwasher,"gallons to wash that many dishes if you ran a dishwasher every other day." )
# used 3.5 to divide for if you washed dishes every other day
# average dishwash cycle uses about 9 gallons 

total_gallons_used_weekly = int(gallons_used_with_dishwasher) + int(weekly_gallons_from_showers)
print("Your total amount of gallons used weekly from the shower and dishwasher is",total_gallons_used_weekly)
# add gallons from using dishwasher
# & gallons from showering 
