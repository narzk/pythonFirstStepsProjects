

def BMI_calculation(w,h):
   return w/(h*h*0.01*0.01)
def BMR_calculation(w,h, a, s):

    if s=='f' or s=='F':
        return 10 * w + 6.25 * h - 5 * a -161
    else:
        return 10*w + 6.25*h -5*a +5
def calories_calculation(bmr, l):
    if l==0:
        return bmr*1.2
    if l==1:
        return bmr*1.375
    if l==2:
        return bmr*1.55
    if l==3:
        return bmr*1.725
    if l==4:
        return bmr*1.9
def daily_calories_calculator(w, gw,gd, nc ):
    number_weight_lose=w-gw
    calories_to_not_use=(number_weight_lose/0.45)*3500
    calories_to_not_use_per_day= calories_to_not_use/gd
    if nc<calories_to_not_use_per_day:
        return False
    else:
        return nc-calories_to_not_use_per_day


print("~Welcome to the healthy app!~")
print("BMI Calculation")
print("Enter your Weight in Kg")
weight_kg=int(input())
print("Enter your height in Cm")
height_cm=int(input())

print("The BMI calculation is:")
BMI=BMI_calculation(weight_kg, height_cm)
print('|{}|'.format(BMI))

print("BMR calculation:")
print("what is your age?")
age=int(input())
print("are you male or female?[m,f]")
sex=input()
BMR=BMR_calculation(weight_kg, height_cm, age, sex)
print("Your BMR is :")
print('|{}|'.format(BMR))
print("Now calculating amount of calories that you need to use per day")
print("which categories are you in?")

level_categories=['Sedentary(little or no exercise)[0]','Lightly actuve (light exercise/ sport 1-3 days/weeek)[1]', 'Moderately active(moderate exercise/sports 3-5 days/week)[2]','very active(hard exercise/ sports 6-7 days a week)[3]','Extra active (very hard exercise/ sport & physical job)[4]']

for i in level_categories:
    print('|{}| '.format(i))

user_level=int(input())

normal_calories=calories_calculation(BMR, user_level)
print("you need {} calories each day".format(normal_calories))

print('how much weight do you want to be?')
goal_weight=int(input())
print('how many days do you want to be on a diet?')
goal_days=int(input())

daily_calories=daily_calories_calculator(weight_kg,goal_weight, goal_days, normal_calories)

if daily_calories==False:
    print('it is impossible!!!')
else:
    print('use {} amount of calories each day'.format(daily_calories))

print('Do you want to see the whole info of your BODY STATISTIC?[y,n]')
user_result=input()
if user_result=='y'or user_result=='Y':
    print('BMI: {}|BMR: {}| normal calories each day:{}'.format(BMI, BMR, normal_calories))
    if daily_calories != False:
        print('to loose {} wight in {} days you need to eat {} calories each day'.format(weight_kg-goal_weight, goal_days, daily_calories))
else:
    print('BYE')