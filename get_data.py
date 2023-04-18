import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    f=open(filename).read()
    data=json.loads(f)

    return data
filename="randomuser_data.json"

get_data(filename)


# import json

# def get_data(filename):
#     a=open("randomuser_data.json").read()
#     b=json.loads(a)
#     return b
# print(get_data("salom"))