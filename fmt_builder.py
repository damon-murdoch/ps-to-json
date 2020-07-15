import json

from set_parser import Pokemon


# Given a file containing showdown sets,
# separates them and returns them all as
# a list.
def read_sets(content):
    # Return object - list of sets
    sets = []

    # Split the input on the new line charcter
    lines = content.split('\n')

    # While there is content left in the split
    while len(lines):

        # Read over every line in the document
        for i in range(len(lines)):

            # If the current line is blank (is separator)
            if not lines[i]:
                # Add all content preceding blank to a new set
                sets.append(lines[:i])

                # Pop all content preceding blank from the content list
                lines = lines[i:]

                # Pop the blank charcter from the content list
                lines.pop(0)

                # Break the for loop, back to while
                break

            # If we have reached the end, break the loop
            # Will probably happen if newline is missing at bottom of document
            if i == len(lines) - 1:
                # We are done, return the set list object
                return sets

    # Return the set list object
    return sets


# Given a file containing showdown sets,
# converts it into a json file and commits
# it to a new json file with the same name,
# with the extension replaced with 'json'.
def read_file(file, outf=None, indent=4):
    # Object containing set data
    # for specific species
    # KEYS = species name e.g.
    # kangashan, landorus, etc.
    format = {}

    # Open the provided file name
    with open(file, 'r') as f:

        # Read the whole string from the file in one set, pass to reader
        sets = read_sets(f.read())

        # For each set returned
        for s in sets:
            # Create a blank pokemon object
            active = Pokemon()

            # Convert it to a Pokemon object
            species = active.from_ps(s)

            # If an error list has been returned
            if isinstance(species, list):
                if species[1]:
                    print('Failed for document', file, 'Failed on set line', species[0], ': (', species[1], ')')
                else:
                    print('Failed for document', file, ', No content provided! Object:', species)

            else:
                # If species is is not recorded yet
                if species not in format:
                    # Create new list
                    format[species] = [active.to_hash()]

                # Species has a list already
                else:
                    # Add new set to the end of the list
                    format[species].append(active.to_hash())

    # If an output file is provided
    if outf:
        # Open the output file
        with open(outf, 'w+') as o:
            # Write the json file to the output file
            o.write(json.dumps(format, indent=indent))

    # No output filename
    else:
        # Return the python data structure
        return format


# Main (test functions)
if __name__ == '__main__':
    # Test the functions with a sample data set
    read_file('in/vgc2015.set', 'vgc2015.json')
