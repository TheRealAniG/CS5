def sleep_in(weekday, vacation):
  if(weekday == False):
    return True
  elif(vacation == True):
    return True
  else:
    return False

def diff21(n):
  if(n<=21):
    return 21 - n
  else:
    return (n-21)*2
  
def near_hundred(n):
  if(abs(200-n)<= 10 or abs(100-n)<= 10):
    return True
  else:
    return False

def missing_char(str, n):
  return str[0:n] + str[n+1:]

def monkey_trouble(a_smile, b_smile):
  if(a_smile == b_smile):
    return True
  else:
    return False
  
def parrot_trouble(talking, hour):
  if(talking == True and hour < 7 or talking == True and hour > 20):
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if(negative == True):
    if(a < 0 and b < 0):
      return True
    else:
      return False
  else:
    if(a < 0 and b < 0 or a > 0 and b > 0):
      return False
    else:
      return True
    
def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]

def sum_double(a, b):
  if(a==b):
    return 4*a
  else:
    return a + b

def makes10(a, b):
  if(a == 10 or b == 10):
    return True
  elif(a + b == 10):
    return True
  else:
    return False

def not_string(str):
  if(str[0:3]=="not"):
    return str
  else:
    return "not " + str

def front3(str):
  if(len(str)<3):
    return 3*str
  else:
    return 3*str[0:3]

def hello_name(name):
  return "Hello " + name + "!"

def make_out_word(out, word):
  return out[0:2] + word + out[2:4]

def first_half(str):
  return str[0:len(str)/2]

def non_start(a, b):
  return a[1:] + b[1:]

def make_abba(a, b):
  return a + b + b + a

def extra_end(str):
  return 3*str[-2:]

def without_end(str):
  return str[1:-1]

def left2(str):
  return str[2:] + str[0:2]

def make_tags(tag, word):
  return "<" + tag + ">" +  word + "</" + tag + ">"

def first_two(str):
  if(len(str)<2): return str
  else: return str[:2]

def combo_string(a, b):
  if(len(a) < len(b)):
    return a + b + a
  else:
    return b + a + b

def cigar_party(cigars, is_weekend):
  if(is_weekend == True):
    if(cigars >= 40): return True
    else: return False
  else:
    if(cigars >= 40 and cigars <= 60): return True
    else: return False

def caught_speeding(speed, is_birthday):
  if(is_birthday == True):
    speed = speed - 5
    
  if(speed <= 60): return 0
  elif(speed<=80 and speed>=61): return 1
  else: return 2

def love6(a, b):
  if(a == 6 or b == 6): return True
  elif(a + b == 6 or a - b == 6 or b - a == 6 ): return True
  else: return False


