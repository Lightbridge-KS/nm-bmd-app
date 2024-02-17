def attempt_float(x: str):
    try:
        return float(x)
    except ValueError:
        if x == "":
            return None
        else:
            raise ValueError(f"x = `{x}` must be a number")
        
def parse_str_to_num_or_list(x: str, sep = ","):
    if not isinstance(x, str):
        raise ValueError("`x` must be string")
    
    try:
        # Split the string into parts based on comma, then strip whitespace and convert each part to a float 
        res = [float(num.strip()) for num in x.split(sep)]
        if len(res) == 1: # Ex: [1.1] will convert to 1.1
            return res[0] 
        if len(res) > 1: # Ex: [1.1, 1.2, 1.3, 1.45]
            return res
    except ValueError:
        if x == "":
            return None
        else:
            raise ValueError(f"x = `{x}` must be string of number(s) separated by comma")
        
if __name__ == "__main__":
    print(parse_str_to_num_or_list("1.1"))
    print(parse_str_to_num_or_list("1.1, 1.22,12 , 22"))
    # print(parse_str_to_num_or_list("1.1, 1.22,12 , 22, *"))