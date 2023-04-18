import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    a=get_data.get_data("randomuser_data.json")
    b=len(a["results"])
    c=0
    d=''
    for birinchi in range(b):
        d+=a["results"][birinchi]["name"]["first"]+', '+a["results"][birinchi]["name"]["last"]+', '+a["results"][birinchi]["phone"]+'\n'
    return d
print (get_users_data("salom"))