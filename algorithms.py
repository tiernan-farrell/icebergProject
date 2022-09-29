

def processData(file: str) -> list[dict]:
    data = []
    with open(file, 'r') as lines: 
        for line in lines: 
            lineContents = {}
            if ("1" in line): 
                lineContents['A'] = "1"
            else:
                lineContents['A'] = "0"

            if ("2" in line): 
                lineContents['B'] = "1"
            else:
                lineContents['B'] = "0"
                
            if ("3" in line): 
                lineContents['C'] = "1"
            else:
                lineContents['C'] = "0"
                
            if ("4" in line): 
                lineContents['D'] = "1"
            else:
                lineContents['D'] = "0"
                
            if ("5" in line): 
                lineContents['E'] = "1"
            else:
                lineContents['E'] = "0"
                
            if ("6" in line): 
                lineContents['F'] = "1"
            else:
                lineContents['F'] = "0"
                
            data.append(lineContents)

    return data


def main():
    processedData = processData('data.txt')
    for i in range(10):
        print (processedData[i])
    return 0

if __name__ == "__main__": 
    main()