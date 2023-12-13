import re
file = 'input_7_1.txt'

def duplicates(file):
    with open(file, 'r') as file:
        code_lines = file.readlines()

    func_def_pattern = r'def\s+(\w+)\('
    func_call_pattern = r'\b(\w+)\('

    func_defs = {}
    func_calls = {}

    for i, line in enumerate(code_lines, start=1):
        def_match = re.search(func_def_pattern, line)
        if def_match:
            func_name = def_match.group(1)
            func_defs[func_name] = i

        call_matches = re.finditer(func_call_pattern, line)
        for match in call_matches:
            func_name = match.group(1)
            if func_name in func_defs and func_defs[func_name] != i:  # Exclude definition line
                if func_name not in func_calls:
                    func_calls[func_name] = set()
                func_calls[func_name].add(i)

    for func_name, def_line in func_defs.items():
        calls = sorted(list(func_calls.get(func_name, [])))
        print(func_name + ': def in ' + str(def_line) + ', calls in ' + str(calls))
duplicates(file)
