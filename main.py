
def count(inputstring):
    return len(inputstring.split())

def countchars(inputstring):
    
    legatstring ="abcdefghijlkmnopqrstuvwxyzåøæ"
    resultdict = {}
    for c in inputstring:
        char = c.lower()
        if char in legatstring:
            if (char in resultdict):
                resultdict[char]+= 1 
            else:
                resultdict[char] = 1
       
    return resultdict

def print_report(book,wordcount, countchars):
    print(f'--- Begin report of {book} ---')
    print (f'{wordcount} words found in the document \n')
    for char in countchars:
        print (f"The '{char}' character was found {countchars[char]} times")
    print('--- End report ---')
def main():
    book = 'books/frankenstein.txt'
    with open(book) as f:
        file_contents = f.read()
    print (file_contents)
    wc = count (file_contents)
    print (wc)
    cc = countchars(file_contents)
    print_report(book,wc,cc)

test = '123abcABC!'

main()