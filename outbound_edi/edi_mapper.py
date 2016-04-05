import sys,os

'''
This file takes certain parameters and creates a temp file based on the edi type that was requested.
This file calls other different files for creating specific pieces of the file that this file then puts on the temp file.

@RecordId
@SendTo
@Return temp file handle
'''


'''
creates the file and puts it in tmp

return file handle
'''
def start_file():
    return os.file()

'''
Build the header segments for the file based on the file type

? Need to know how to get the trading partner attributes to create the header
'''
def header(fileHandle, sendTo, fileType):
    attributes = {tpId: '1234'} # get object of attributes that need to be built in to the header
    headerString = headerMap(fileType, sendTo)

'''
Run the correct map for the type of file and type of record
'''
def message(fileHandle, recordId, typeOfRecord, fileType):
    ST = [
        'ST', # segment identifier
        '309', #ST01
        fileId, #ST02
        '\n'
    ].join('*')

    fileHandle

'''
Build the footer segments for the file based on the file type

? Need to know how to get the trading partner attributes to create the footer
'''
def footer(fileHandle, fileType):
    count = 1 # either we read through the file and count the segments we need to sum or we have it passed to us from the message

'''
Calls the specific methods to construct the file
'''
def build(recordId, sendTo, typeOfRecord, typeOfFile):
    fileHandle = start_file(typeOfFile)
    header(fileHandle, sendTo, typeOfFile)
    message(fileHandle, recordId, typeOfRecord, typeOfFile)
    footer(fileHandle, typeOfFile)
    return fileHandle

'''
Defaults parameters, calls build, and returns the file handle for the tmp file that was created
'''
def __main__():
    sendTo = sys.argv[2]
    typeOfRecord = sys.argv[3]
    typeOfFile = sys.argv[4]

    if sendTo == '':
        sendTo = 'uscustoms'

    if typeOfRecord == '':
        typeOfRecord = 'shipment'

    if typeOfFile == '':
        typeOfFile = 'x12'

    return build(sys.argv[1], sendTo, typeOfRecord, typeOfFile)
