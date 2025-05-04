import pandas

data= pandas.read_csv("nato_phonetic_alphabet.csv")


nato_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}



word= list(input("Enter a name").upper())

res= [nato_dict[w] for w in word]

print(res)
