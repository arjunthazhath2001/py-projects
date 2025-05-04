import pandas

data= pandas.read_csv("nato_phonetic_alphabet.csv")


nato_dict = {data["letter"]: data["code"] for (index, data) in data.iterrows()}



word= list(input("Enter a name").upper())

res= [nato_dict[w] for w in word]

print(res)
