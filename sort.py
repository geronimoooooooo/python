lisa_obj.sort(key=lambda obj: helper_functions.natkey(obj.name))
    dicta_sorted = {k: dicta[k] for k in sorted(dicta, key= helper_functions.natkey)}
    dicta_sorted_reversed = dict(reversed(dicta_sorted.items()))

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    https://stackoverflow.com/questions/5967500/
    how-to-correctly-sort-a-string-with-a-number-inside
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def natkey(s):
    '''https://stackoverflow.com/questions/16955105/sort-list-of-objects-by-attribute-alphanumerically
    https://www.w3docs.com/snippets/python/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects.html
    https://stackoverflow.com/questions/403421/how-do-i-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
    '''
    return [w or int(n) for w, n in re.findall('(\D+)|(\d+)', s)] #type:ignore


def sort_reverse_list(list_str: list[str])->list[str]:
    """Sorts and reverses a list. 'Highest' value at index[0]

    Args:
        list_obj (list): List that should be sorted and reversed

    Returns:
        list: Sorted and reversed list
    """
    
    list_str.sort(key = natural_keys, reverse= True)    
    return list_str

def sort_reverse_list_obj(list_obj:list[Raster])->list[Raster]:
    """Sorts and reverses a list. 'Highest' value at index[0]

    Args:
        list_obj (list): List that should be sorted and reversed

    Returns:
        list: Sorted and reversed list
    """
    list_obj.sort(key=lambda obj: natkey(obj.name), reverse=True)    
    return list_obj
