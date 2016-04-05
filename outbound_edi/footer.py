import sys

def x12(test,batchId):
    senderID = ''
    receiverID = 'CUSTOMS  '
    dataTestOrProduction = 'P'
    if test:
        receiverID = 'CUSTOMSTST'
        dataTestOrProduction = 'T'
    currentDate = timezone.now()
    transmissionDate = currentDate.format('YYMMDD')
    transmissionLongDate = currentDate.format('YYYYMMDD')
    transmissionTime = currentDate.format('HHMM')

    GE = [
        'GE', # segment identifier
        'SO', sendID, receiverID, #GS01 #GS02 #GS03
        transmissionLongDate, transmissionTime, #GS04 #GS05
        batchId, 'X', 004010 #GS06 #GS07 #GS08
        '\n'
    ].join('*')

    IEA = [
        'IEA', # segment identifier
        00, ' '*10, #ISA01 #ISA02
        00, ' '*10, #ISA03 #ISA04
        'ZZ', senderID, #ISA05 #ISA06
        'ZZ', receiverID, #ISA07 #ISA08
        transmissionDate, transmissionTime, #ISA09 #ISA10
        'U', 00401, #ISA11 #ISA12
        batchId, 0, #ISA13 #ISA14
        dataTestOrProduction, ':' #ISA15 #ISA16
        '\n'
    ].join('*')

    return IEA + GE

'''
first check for argument passed in, then check arguments, then check global variables, finally throw error
'''
def __main__():
    typeOfFile = sys.argv[1].toUpperCase()
    #if !typeOfFile:

    if typeOfFile === 'X12':
        return x12()
