def double_char(str):
  result = ''
  for c in str:
    result += c*2
  return result

def string_times(str, n):
  result = ''
  for c in range(n):
    result += str
  return result

def string_splosion(str):
  result = ''
  for c in range(len(str)+1):
    result += str[:c]
  return result

def array_front9(nums):
  count = 0
  for x in nums:
    count += 1
    if(x == 9 and count <=4):
      return True
  return False

def front_times(str, n):
  front = str[:3]
  result = ""
  for x in range(n):
    result += front
  return result

def last2(str):
  count = 0
  substring = str[-2:]
  for x in range(len(str)-1):
    if(x+1 < len(str)-1 and str[x:x+2] == substring):
      count += 1
  return count
    
def array123(nums):
  for x in range(len(nums)-2):
    if(nums[x] == 1 and nums[x+1] == 2 and nums[x+2] == 3):
      return True
  return False
    
def string_bits(str):
  result = ""
  for x in range(len(str)):
    if(x % 2 == 0):
      result += str[x]
  return result

def array_count9(nums):
  count = 0
  for x in nums:
    if(x == 9):
      count += 1
  return count

def string_match(a, b):
  count = 0
  if(len(a)<len(b)):
    limiter = a
  else:
    limiter = b
  for x in range(len(limiter)-1):
    if(a[x] + a[x+1] == b[x] + b[x+1]):
      count += 1
  return count

def count_code(str):
  count = 0
  for x in range(len(str)-3):
    if(str[x] == "c" and str[x+1] == "o" and str[x+3] == "e"):
      count += 1
  return count