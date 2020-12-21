#
#  __    _  _______  _     _  _______  _______  _______  _______  _______    ______    _______  __   __  _______  __   __  _______  ______   
# |  |  | ||       || | _ | ||       ||       ||   _   ||       ||       |  |    _ |  |       ||  |_|  ||       ||  | |  ||       ||    _ |  
# |   |_| ||    ___|| || || ||  _____||    _  ||  |_|  ||       ||    ___|  |   | ||  |    ___||       ||   _   ||  |_|  ||    ___||   | ||  
# |       ||   |___ |       || |_____ |   |_| ||       ||       ||   |___   |   |_||_ |   |___ |       ||  | |  ||       ||   |___ |   |_||_ 
# |  _    ||    ___||       ||_____  ||    ___||       ||      _||    ___|  |    __  ||    ___||       ||  |_|  ||       ||    ___||    __  |
# | | |   ||   |___ |   _   | _____| ||   |    |   _   ||     |_ |   |___   |   |  | ||   |___ | ||_|| ||       | |     | |   |___ |   |  | |
# |_|  |__||_______||__| |__||_______||___|    |__| |__||_______||_______|  |___|  |_||_______||_|   |_||_______|  |___|  |_______||___|  |_|
# - Hazel - Special thanks to Raj!
# - Prerequestites:
#   1. ONLY CATCHES INVALID FILES/DIRECTORY UP TO 158 CHARACTERS!
#      e.g If file/dir consumes 3 Breaklines due to passing 2 max. chars in a single line, this will not fix and continue to next invalid file
#      IN A CASE THIS HAPPENS: CMD will print the invalid file/dir, do take note of such cases and MANUALLY fix them!
#   2. ONLY CATCHES LINUX DIRLISTING!
# - Tested on MY market
# - Use this before any cleaning of directory listing

import sys, getopt

scriptname = 'newspace-remover.py'
residueLine = ''

def main(argv):
    infile = ''
    outfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('««-----------------------------»»\n')	
        print(' How to use? \n««-----------------------------»»\n',scriptname,'-i <infile> -o <outfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            #こんぺこ! こんぺこ! こんぺこ!
            print('««-----------------------------»»')	
            print(' Newline remover \n How to use? \n««-----------------------------»»\n',scriptname,'-i <infile> -o <outfile>')
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            infile = arg
        elif opt in ("-o", "--ofile"):
            outfile = arg

    data = open(infile,'r')
    list = data.read()
    lines = list.split('\n')
    length = len(lines)

    for i in range(length):
        length_line = len(lines[i])
        if(length_line > 78 and length_line < 158):
            residueLine = lines[i+1]
            if(len(residueLine) != 0 and ((lines[i+1]) != '\n')):
                if not (residueLine.startswith('-rw-') or residueLine.startswith('-r-')):
                    lines[i] = lines[i] + lines[i+1]
                    lines[i+1] = "placeholder"
        elif(length_line > 157):
            print(lines[i])
        else:
            continue

    output_file = open(outfile,'w')
    for words in lines:
        if 'placeholder' not in words:
            output_file.write(words+'\n')
        else:
            continue
    print('File successfully fixed: '+infile)
    print('Appended to: '+outfile)

if __name__ == "__main__":
   main(sys.argv[1:])





