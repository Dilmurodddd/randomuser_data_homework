import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    a=get_data.get_data("randomuser_data.json")
    b=''
    c=''
    for birinchi in a:
        if birinchi=="results":
            c=birinchi
    d=len(a[c])
    for ikkinchi in range(d):
        b+=a[c][ikkinchi]["email"]+'\n'
    return b
print(get_email("salom"))