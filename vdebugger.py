## System libraries imports:
import os
import copy
import pprint

## Global variables:

## The table is a row and column list of entries in format : "{name: "some_variable", "value": 31241, "iterations": 10}"
## The iteration increments every time the value passed for same name is same as before, resets when different. 
table : list[list[dict]] = [[]]
max_val_length = 20

def vd(name, value):
    os.system("cls")
    print(
        vdoutput(name, value)
    )


    
def vdoutput(name, value):
    """ Visually debug a supported name value pair of data """
    ## Handle data first:

    ## Strignify name and value for use in output:
    name  = copy.deepcopy(str(name))
    value = copy.deepcopy(pprint.pformat(value))
    value = value[0:max_val_length]  # <-- Limit the size of value to be max value length bound, see setting above ^^^.
    
    entry_present = False

    ## Try to search and replace the entry with new content:
    for row in table:
        do_break = False
        for column in row:
            entry = column

            ## The entry has the name of the supported argument name - the entry exists within the table already:
            if entry["name"] == name:
                old_value, last_iteration = entry["value"], entry["iterations"]
                ## Actually change the entry contents:
                if value == old_value:  # <-- Just increment the iteration, if the values are the same.
                    iteration = last_iteration + 1
                    entry["iterations"] = iteration
                else:  # <-- Reset iteration counter and change the value of entry, if the values of found entry are different.
                    entry["iterations"] = 1
                    entry["value"] = value
                entry_present = True  # <-- Mark entry as found, so that no adding of new entry is needed.
                do_break = True
                break
        if do_break:
            break

    ## If the entry hasn't been found - create new entry at optionally supported row:
    if not entry_present:
        new_entry = {"name": name, "value": value, "iterations": 1}
       
        table[0].append(new_entry)
       

    ## Entry display:
    '''
    
    1. |-----------|
    2. | name      |  
    3. |-----------|
    4. | >>>(1)>>> |  <-- Number of iterations
    5. | Somevalue |  <-- Place for the value 
    6. |-----------|

    6 lines at least in total
    '''
    every_entry_width = 0
    every_entry_height = 0 
    n_entry_lines = 5  # <-- Not counting the place for value string.
    for row in table:
        for column in row:
            entry = column

            name = entry["name"]
            value = entry["value"]
            iterations = entry["iterations"]

            name_string = name
            iterations_string = f">>>({str(iterations)})>>>"
            value_string = pprint.pformat(value)


            def calc_string_width(string : str):
                splitted = string.split("\n")
                max_width = 0
                for line in splitted:
                    max_width = max(len(line), max_width)
                return max_width
            def calc_string_height(string : str):
                return len(string.split("\n"))

            ## Calculate the whole entry width:
            name_width = calc_string_width(name_string)
            iterations_width = calc_string_width(iterations_string)
            value_width = calc_string_width(value_string)
            entry_width = max(name_width, iterations_width, value_width)
            
            ## Calculate the whole entry height:
            entry_height = n_entry_lines + calc_string_height(value)

            every_entry_width = max(entry_width, every_entry_width)
            every_entry_height = max(entry_height, every_entry_height)


    
    ## Create the output string containing the visually debugged entries:
    output = ""
    fs = " "  # <-- Fill Symbol (spaces by default).
    for row_idx in range(len(table)):
        for col_idx in range(len(table[row_idx])):
            entry = table[row_idx][col_idx]
            output +=  "| " +  "-" * every_entry_width  +                  " |"         # 1. |-----------|  
        output += "\n"

        for col_idx in range(len(table[row_idx])):
            entry = table[row_idx][col_idx]
            ensym_left = every_entry_width - len(entry["name"])   # <-- Entry name symbols left.
            output += f"| {entry["name"]}" + fs * ensym_left +             " |"         # 2. | name      | 
        output += "\n"

        for col_idx in range(len(table[row_idx])):
            entry = table[row_idx][col_idx]
            output +=  "| " +  "-" * every_entry_width  +                  " |"         # 3. |-----------|
        output += "\n"

        for col_idx in range(len(table[row_idx])):
            entry = table[row_idx][col_idx]
            eisym_left = every_entry_width - 6 - len(str(entry["iterations"]))  # <-- Entry iterations symbols left.
            output += f"| >>>{entry['iterations']}>>>" + fs * eisym_left + " |"         # 4. | >>>(i)>>> |  
        output += "\n"

        for col_idx in range(len(table[row_idx])):
            entry = table[row_idx][col_idx]
            evsym_left = every_entry_width - len(entry["value"])  # <-- Entry value symbols left.
            output += f"| {entry["value"]}" + fs * evsym_left +            " |"         # 5. | value     |   
        output += "\n"

        for col_idx in range(len(table[row_idx])):
            entry = table[row_idx][col_idx]
            output +=  "| " + "-" * every_entry_width +                    " |"         # N. |-----------|  

    return output



def vditers(name, iterations):
    for row in table:
        for entry in row:
            if entry["name"] == name and entry["iterations"] == iterations:
                return True
    return False


def vdconf(max_v_length):
    global max_val_length
    max_val_length = max_v_length