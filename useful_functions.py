import json

def computeMD5hash(my_string):
    import hashlib
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def write_to_file(this_file):
    """[This takes a data and writes to a file]

    Args:
        this_file ([date]) : [writes to json file]
    """
    with open('response_text.json', 'w') as f:
        f.write(this_file)
        
def convertJSON():
    """
        This takes no arguments and returns a dictonary from json 
    Returns:
        [dict] : [from json file]
    """
    with open('response_text.json', 'r') as f:
        distros_dict = json.load(f)
    return distros_dict


def clear_file():
    with open('response_text.json', 'r+') as f:
        f.truncate(0)
