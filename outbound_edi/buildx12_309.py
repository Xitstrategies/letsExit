'''
FileBuilder x12 309
'''

def build309string(data):
    finalString = ''
    if !data:
        return None;

    ST = [

    ].join('*')

    # mandatory
    M10 = [

    ].join('*')

    # optional
    if data.N9:
        N9 = [].join('*')

    # loop
    P4 = data.P4

    
    SE = [

    ].join('*')

    finalString =

    return finalString

def __main__():
    data = sys.argv[1]
    if !data:
        data = 1

    return build309string(data);
