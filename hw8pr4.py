#
# hw8pr4.py
#
import math

def menu():
    """Prints the menu of options that the user can choose."""
    print()
    print("(0) Input a new list")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the minimum and its day")
    print("(5) Find the maximum and its day")
    print("(6) Your TT investment plan")
    print("(9) Quit")
    print()

def average(L):
    """Finds the average of list L
    """
    result = 0
    for x in L:
        result += x
    return result/(len(L))


def standardDeviation(L):
    """Finds the standard deviation of list L
    """
    avg = average(L)
    result = 0
    for x in L:
        result += (x-avg)**2

    result = result/(len(L))
    return math.sqrt(result)
    

def minimum(L):
    """Finds the minimum of list L and the index
    """
    min_index = 0
    min = L[0]
    for x in range(len(L)):
        if(L[x] < min):
            min_index = x
            min = L[x]
    return min_index+1, min

def maximum(L):
    """Finds the maximum of list L
    """
    max_index = 0
    max = L[0]
    for x in range(len(L)):
        if(L[x] > max):
            max_index = x
            max = L[x]
    return max_index+1, max

def ttPlan(L):
    """Finds the greatest difference in elements with their location
    """
    buy_day = 1
    sell_day = 2
    buy_price = L[0]
    sell_price = L[1]
    profit = sell_price - buy_price
    for b in range(len(L)):
        for s in range(b, len(L)):
            if((L[s] - L[b]) > profit):
                buy_day = b
                sell_day = s
                buy_price = L[b]
                sell_price = L[s]
                profit = sell_price - buy_price
    return buy_day, sell_day, buy_price, sell_price, profit

def main():
    """The main user-interaction loop."""

    L = [] 

    while True:      
        menu()
        choice = input("Choose an option: ")

        try:
            choice = int(choice)  
        except:
            print("I didn't understand your input! Continuing...")
            continue

        if choice == 9:    
            break          

        elif choice == 0:  
            newL = input("Enter a new list: ")   
            
            try: 
                newL = eval(newL) 
                if type(newL) != type([]): 
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL  
            except:
                print("I didn't understand your input. Not changing L.")


        elif choice == 1: 
            for x in range(len(L)):
                print("Day:",x + 1,"Price:",L[x],"$")
            

        elif choice == 2: 
            print()
            print("The average price is", average(L))

        elif choice == 3: 
            print()
            print("The standard deviation is", standardDeviation(L))          

        elif choice == 4:  
            min_index, min = minimum(L)
            print()
            print("The minimum is",min,"on day", min_index)

        elif choice == 5:  
            max_index, max = maximum(L)
            print()
            print("The maximum is",max,"on day", max_index)
        
        elif choice == 6:
            buy_day, sell_day, buy_price, sell_price, profit = ttPlan(L)
            print()
            print("Buy on day", buy_day,"at price", buy_price)
            print("Sell on day", sell_day,"at price", sell_price)
            print()
            print("For a profit of", profit)
        else:
            print(choice, "?")
            print("That's not on the menu!")
    print()
