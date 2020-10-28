character={
    "name": "기사",
    "level": 12,
    "item": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
        },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }
for key in character:
    if type(character[key]) is dict:
        for items in character[key]:
            print(items, ":", character[key][items])
    elif type(character[key]) is list:
        for small_key in character[key]:
            print(key, ":", small_key)
            
    else:
        print(key, ":", character[key])
    
