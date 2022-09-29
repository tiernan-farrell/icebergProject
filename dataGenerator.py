import random

def main(): 
    #create data of 10000 rows varying from 2 to 15 digits that
    #are randomly chosen from 0-9
    
    for i in range (10000): 
        line = ""
        random.seed(i)
        numInRow = random.randint(2, 15)
        for j in range(numInRow):
            line += str(random.randint(0, 6))
            line += " "
        print(line )
    

if __name__ == "__main__": 
    main()