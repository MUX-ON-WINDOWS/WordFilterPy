infile = "input_file.txt"
outfile = "output_file.txt"

delete_list = [
    # Your words you want to fill to filter.
    "Dog","Bird","Pig"
]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
