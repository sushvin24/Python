def main():
    infileName = input("Enter the Name file : ")
    outfileName = input("Enter the Uname file : ")

    infile = open(infileName,'r')
    outfile = open(outfileName,'w')

    for line in infile.readlines():

        first, last = str.split(line)

        uname = str.lower(first[:4]+last[:4])

        outfile.write(uname+'\n')

    infile.close()
    outfile.close()
    print("The username in ",outfileName)

main()
