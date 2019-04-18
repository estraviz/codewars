"""Format a string of names like 'Bart, Lisa & Maggie'
"""


def namelist(names):
    if len(names) == 0:
        return ""
    list_of_names = []
    for d in names[:-1]:
        (k_i, v_i), = d.items()
        list_of_names += [v_i]
    output = ", ".join(list_of_names)
    (k_n, v_n), = names[-1].items()
    return output + " & " + v_n if len(output) > 0 else v_n
