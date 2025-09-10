#!/usr/bin/python

# any line starting with # is a comment, which is ignored by Python

# Setting variables

a = 5 # this is an integer
b = "Susan" # this is a string
c = 3.5 # this is a float
f = [1, 2, 3, 4, 5] # this is a list

# you can print variables to the screen
print(a)

# or find out what type of variable it is
print(type(a))

# you can do mathematical operations
d = a + c
print(d)

# A very useful feature in Python is string indexing
# Each character in a string has a number, starting from 0
# S u s a n
# 0 1 2 3 4
print(b[0]) # this will print the first letter of the string
print(b[-1]) # this will print the last letter of the string
print(b[1:4]) # this will print letters 1 to 3 (4 is not included)
print(b[2:]) # this will print from letter 2 to the end

# You can also split strings
path_example = "/home/user1/data/file.txt"
print(path_example.split("/")) # this will split the string at each "/"
print(path_example.split("/")[-1]) # this will print just the file name

# Lists are stored in [ ] and can be indexed like strings
samples = ["sample1", "sample2", "sample3", "sample4"]
print(samples[0]) # prints the first item in the list

# Dictionaries store key-value pairs
# They are stored in { } with a colon between key and value
sample_dict = {"sample1": "file1.txt", "sample2": "file2.txt"}
print(sample_dict["sample1"]) # prints the value for key "sample1"

# You can also add new key-value pairs
sample_dict["sample3"] = "file3.txt"
print(sample_dict)

# Dataframes are a powerful way to store tables of data
import pandas as pd # import the pandas package
tsv_file_path = "/Users/samalope/python_intro/example_data.tsv"
df = pd.read_csv(tsv_file_path, sep="\t") # read in a tab-delimited file
print(df) # print the whole dataframe
print(df.head()) # print the first 5 rows of the dataframe
print(df.columns) # print the column names
print(df["Sample_ID"]) # print the SampleID column

# You can also filter dataframes
filtered_df = df[df["Classified_insects"] > 10000] # filter rows where Classified_insects > 10,000
print(filtered_df)

# You can also define functions in python. For example, let's define a function to parse a tsv file
def parse_tsv(file_path):
    df = pd.read_csv(file_path, sep="\t")
    return df

df_f1 = parse_tsv(tsv_file_path) # call the function
print(df_f1)

# We can also add other arguments to the function, like for example if the file is csv or tsv
def parse_file(file_path, file_type="tsv"):
    if file_type == "tsv":
        df = pd.read_csv(file_path, sep="\t")
    elif file_type == "csv":
        df = pd.read_csv(file_path)
    else:
        raise ValueError("file_type must be 'tsv' or 'csv'")
    return df

df_f2 = parse_file(tsv_file_path, file_type="tsv") # call the function
print(df_f2)

# Or we can add a filtering threshold
def parse_and_filter(file_path, file_type="tsv", filter_col=None, threshold=None):
    df = parse_file(file_path, file_type)
    if filter_col and threshold is not None:
        df = df[df[filter_col] > threshold]
    return df

df_f3 = parse_and_filter(tsv_file_path, file_type="tsv", filter_col="Classified_insects", threshold=10000) # call the function
print(df_f3)

# Loops are also very useful in Python.
# you can loop through lists:
list_example = ["sample1", "sample2", "sample3", "sample4", "sample5_a", "sample6_b"]
for item in list_example:
    print(item)

# or perhaps a little more complex, like printing only items that contain "_a"
for item in list_example:
    if "_a" in item:
        print(item)

# the word item can be replaced with any word, as long as it is consistent within the loop
for banana in list_example:
    if "_b" in banana:
        print(banana)

# You also loop through dictionaries
for key in sample_dict:
    print(key, sample_dict[key]) # print both key and value

# or through dataframes
for index, row in df.iterrows(): # here, the index is the row number (0, 1, 2...) and row is the actual row data
    print(row["Sample_ID"], row["Classified_insects"]) # print Sample_ID and Classified_insects columns

# You can also loop through a range of numbers
for i in range(5): # this will loop through numbers 0 to 4
    print(i)   

# in any loop, you can use "break" to exit the loop early
for i in range(10):
    if i == 5:
        break # exit the loop when i is 5
    print(i)    

# or "continue" to skip to the next iteration of the loop, for example:
list_example = ["insect_butterfly", "insect_ant", "insect_beetle", "insect_fly", "insect_bee", "mammal_dog", "mammal_cat"]
for animal in list_example:
    if "insect" in animal: # if this happens, do the next line
        print(animal)
    else: # if not
        continue # skip to the next item in the loop

# You can also read and write files in Python
# Writing a file
output_file_path = "output.txt"
with open(output_file_path, "w") as f: # open the file in write mode "w"
    f.write("Hello, world!")
    f.write("\nThis is a new line.")

# Reading a file
with open(output_file_path, "r") as f: # open the file in read mode "r"
    content = f.read()
    print(content)

# You can also read files line by line (useful in fastas, for example)
with open(output_file_path, "r") as f:
    for line in f:
        print(line.strip()) # strip() removes leading/trailing whitespace, including newlines


