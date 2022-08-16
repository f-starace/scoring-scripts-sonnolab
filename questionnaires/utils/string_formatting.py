from typing import List



def format_string(string: str) -> str:
    """
    Strips, lowers and removes punctuation and accents from a string.
    """
    return string.strip().lower().translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans(normalMap))


def link_strings(input_lst: List[str], lookup_lst: List[str]):
    """
    Link a list of strings to a list of strings.
    """
    return [lookup_lst[input_lst.index(s)] for s in input_lst]

normalMap = {
    'À': 'A',
    'Á': 'A', 
    'Â': 'A', 
    'Ã': 'A', 
    'Ä': 'A',
    'à': 'a', 
    'á': 'a', 
    'â': 'a', 
    'ã': 'a', 
    'ä': 'a', 
    'ª': 'A',
    'È': 'E', 
    'É': 'E', 
    'Ê': 'E', 
    'Ë': 'E',
    'è': 'e', 
    'é': 'e', 
    'ê': 'e', 
    'ë': 'e',
    'Í': 'I', 
    'Ì': 'I', 
    'Î': 'I', 
    'Ï': 'I',
    'í': 'i', 
    'ì': 'i', 
    'î': 'i', 
    'ï': 'i',
    'Ò': 'O', 
    'Ó': 'O', 
    'Ô': 'O', 
    'Õ': 'O', 
    'Ö': 'O',
    'ò': 'o', 
    'ó': 'o', 
    'ô': 'o', 
    'õ': 'o', 
    'ö': 'o', 
    'º': 'O',
    'Ù': 'U', 
    'Ú': 'U', 
    'Û': 'U', 
    'Ü': 'U',
    'ù': 'u', 
    'ú': 'u', 
    'û': 'u', 
    'ü': 'u',
    'Ñ': 'N', 
    'ñ': 'n',
    'Ç': 'C', 
    'ç': 'c',
    '§': 'S',
    '³': '3', 
    '²': '2', 
    '¹': '1'
}


