"""
Trisha Lapiz
Number converter program
"""
def converter(number,base):    
    a_list = []
    if number == 0: #BASE CASE, when down to the last number
        if base == 2 or base == 8 or base == 16: 
            return ""
    elif number > 0: #getting the remainder from the number by using the modulus with the base and appending it to a list so that the elements in the list can be turned into a string using the join method and be displayed in the output
        if base == 2: #BINARY
            remainder = str(number % base)
            a_list.append(remainder)
            a_string = "".join(a_list) 
        elif base == 8: #OCTAL
            increment = number // base #dividing by 8 to get the increment
            if increment > 0:
                remainder = str(number % base)
                a_list.append(remainder)
                a_string = "".join(a_list)
            else:
                remainder = str(number % base)
                a_list.append(remainder)
                a_string = "".join(a_list)
        elif base == 16: #HEXADECIMAL
            remainder = number % base
            if remainder < 10:
                a_list.append(str(remainder))
                a_string = "".join(a_list)
            else:
                if remainder >= 10 and remainder < 16: #for hexadecimal it only counts 0-9 so when it gets to 10-15 it's in letters
                    if remainder == 10:
                        a_list.append("A")
                    elif remainder == 11:
                        a_list.append("B")
                    elif remainder == 12:
                        a_list.append("C")
                    elif remainder == 13:
                        a_list.append("D")
                    elif remainder == 14:
                        a_list.append("E")
                    elif remainder == 15:
                        a_list.append("F")
                a_string = "".join(a_list) 
        return converter(number//base, base) + a_string
