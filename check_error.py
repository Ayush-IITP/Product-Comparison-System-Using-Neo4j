import tkinter
import tkinter.messagebox

def error_msg():
    tkinter.messagebox.showinfo("Error", "One of the entries do not have correct datatype.")

def rating_limit():
    tkinter.messagebox.showinfo("Error", "rating is not in the range of 0 to 5.")    

def int_check(s):
    if s.isnumeric():
        return True
    return False

def float_check(s):
    if(int_check(s)):
        return True;
    try:
        b = float(s)
        if '.' in s:
            return True
        return False
    except ValueError:
        return False

def rating_check(s):
        try:
            b = float(s) 
            if b <= 5 and b>=0:
                return True
            
            return False
        except ValueError:
              return False       

def string_check(s):
    if s.isalpha():
        return True
    return False
