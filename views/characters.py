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

def update_character(id, body):
    for index, character in enumerate(characters):
        if character["id"] == id:
            body["id"] = id
            characters[index] = body
            break




def get_all_characters():
    return characters