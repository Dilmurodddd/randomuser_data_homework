import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    male=0
    female=0
    a=get_data.get_data("randomuser_data.json")
    b=len(a["results"])
    for birinchi in range(b):
        if a["results"][birinchi]["gender"]=="male":
            male+=1

        if a["results"][birinchi]["gender"]=="female":
            female+=1

    return male,female

print(get_gender_users("salom"))