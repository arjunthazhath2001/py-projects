import random
import pandas
import datetime as dt


data= pandas.read_csv('dob.csv')

data=data.to_dict()

# name=data['name'].to_list()
# mail= data['mail'].to_list()
# dob= data['dob'].to_list()


# for d in dob:
#     d.split('-')


# letter_num= random.randint(1,3)
# with open(f"./letter_{letter_num}.txt") as file:
#     contents= file.read()
    

current_day= dt.datetime.now().day
current_month= dt.datetime.now().month

# now= dt.datetime.now()
print(current_day)
print(current_month)

    
# bday_person= 


# with open("./input/names/invited_names.txt") as file:
#     p_names=file.readlines()
    

# print(p_names)

# for i in range(len(p_names)):
#     stripped_name=p_names[i].strip('\n')
#     new_letter= contents.replace('[name]',stripped_name) 
#     with open(f"./output/readytosend/letter_for_{stripped_name}.docx",'w') as file:
#         file.write(new_letter)





# print(name)
# print(mail)
# print(dob)