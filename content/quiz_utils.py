from IPython.display import HTML, display

def collapsible(content):
    html = f"""
<details>
    <summary>Show Answer</summary>
    <p >
    {content}
  </p>
</details>
"""
    return html


from itertools import permutations
import numpy as np

def generate_shuffled_order_options(items, n_variants):
    """
    Given the correct order generate mulitple wrong choices including the correct order
    
    Eg. 
    ```
    >>> generate_shuffled_order_options([1,2,3,4], 4)
    # TODO: give output
    ```
    """
    
    perms = np.array(list(permutations(items))[1:])
    options = [items] + perms[np.random.choice(len(perms),n_variants-1)].tolist()
    np.random.shuffle(options)
    return options

def generate_shuffled_match_options(rhs=None,lhs=None, n_variants=4):
    """Given the options in the order generate match option tuples including the correct match"""
    if lhs == None:
        lhs = list(range(1,len(rhs)+1))
    
    options = generate_shuffled_order_options(rhs, n_variants)
    correct_option = list(zip(lhs,rhs))
    match_options = [ [(l,r) for l,r in zip(lhs,right_match)] for right_match in options ]
    return match_options,correct_option


def display_options(options, correct_option= "", correct_index = None):
    if not correct_option and correct_index:
        correct_option = options[correct_index]
    
    result = f"""
    <ol>
    {"\n".join([f"<li>{option}</li>" for option in options])}
    </ol>
    {collapsible(correct_option) if correct_option else ""}
    """
    display(HTML(result))

def display_match_options(options,correct_option=None):
    display_options((", ".join(f"({lhs}) - {rhs}" for lhs, rhs in option) for option in options), ", ".join(f"({lhs}) - {rhs}" for lhs, rhs in correct_option))
