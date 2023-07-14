characters = [
    {
        "id": 1,
        "name": "Miranda"
    },
    {
        "id": 2,
        "name": "Carrie"   
    },
    {
        "id": 3,
        "name": "Samantha"
    },
    {
        "id": 4,
        "name": "Charlotte"
    }
]

def delete_character(id):
    character_index = -1
    for index, character in enumerate(characters):
        if character["id"] == id:
            character_index = index
            break

    if character_index > -1:
        characters.pop(character_index)
        

def update_character(id, body):
    for index, character in enumerate(characters):
        if character["id"] == id:
            body["id"] = id
            characters[index] = body
            break




def get_all_characters():
    return characters