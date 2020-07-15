import fmt_builder as builder

import sys, os, os.path

if __name__ == '__main__':

    # Default input path
    inpath = 'in'

    # Default output path
    outpath = 'out'

    # If arguments have been provided
    if len(sys.argv) > 1:

        # Iterate over every line
        # after the default arg
        for arg in sys.argv[1:]:

            # Check if an input path was provided
            if any(a in arg for a in ('input', 'inpath', 'in=', 'i=')):
                # Take the content after the equals and assign it to inpath
                inpath = arg.split('=')[1]
                
                print('Using input path',inpath,'...')

            if any(a in arg for a in ('output', 'outpath', 'out=', 'o=')):
                # Take the content after the equals and assign it ot outpath
                outpath = arg.split('=')[1]
                
                print('Using output path',outpath,'...')

    # Retrieve all the formats in the fmt directory
    formats = os.listdir(inpath)

    # Iterate over each format
    for format in formats:

        # Input file full path
        file = inpath + '/' + format

        # Output file full path
        outf = outpath + '/' + format.split('.')[0] + '.json'

        # Convert the input file to the output file
        builder.read_file(file, outf)
