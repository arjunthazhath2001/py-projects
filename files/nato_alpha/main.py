import pandas

data= pandas.read_csv("nato_phonetic_alphabet.csv")


nato_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}

game_on=True
while game_on:
    word= list(input("Enter a name").upper())

    try:
        res= [nato_dict[w] for w in word]
    except KeyError:
        print("only alpha please")
        
    else:
        print(res)
