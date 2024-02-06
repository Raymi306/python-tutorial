"""
Exports doctested, minimal codeblocks for templating
Docstrings MUST be double quotes!
"""

import inspect


def normalize_indentation(line, set_level, level):
    """Remove unnecessary indentation resulting from doctesting of code"""
    if line == '\n':
        return line, level
    counter = 0
    length = len(line)
    while counter < length - 1 and line[counter] == ' ':
        counter += 1
    if set_level:
        level = int(counter / 4)
        result = line[4 * level:], level
    else:
        index = 4 * level
        result = line[index:], level
    return ''.join(result[0]) + '\n', result[1]


def get_func_body(name):
    """
    Remove docstrings, indentation, and testing artifacts from function
    indicated by name for use with templating as a codeblock

    Functions can be marked with # START and # END comments for special
    trimming of testing code
    """
    raw = inspect.getsource(name)
    lines = raw.split('\n')[1:]
    set_level = True
    level = None
    consume_whitespace = True
    result = []
    if '# START' in raw and '# END' in raw:
        take = False
        for line in lines:
            if '# END' in line:
                take = False
            if take:
                if not line.strip() and consume_whitespace: # DRY :\
                    continue
                consume_whitespace = False
                line, level = normalize_indentation(line, set_level, level)
                set_level = False
                result.append(line)
            if '# START' in line:
                take = True
        return ''.join(result).strip() # confused myself with early return lol
    docstring_occurences = 0
    for line in lines:
        if docstring_occurences >= 2:
            if not line.strip() and consume_whitespace: # DRY :\
                continue
            consume_whitespace = False
            line, level = normalize_indentation(line, set_level, level)
            set_level = False
            result.append(line)
        docstring_occurences += line.count('"""')

    return ''.join(result).strip()
