import string
import argparse

def process(newspaper_array):
    f = open("testfile.txt", "w")
    for entry in newspaper_array:
        entry = entry.translate(str.maketrans('', '', string.punctuation))
        print(entry)
        f.write(entry + ".\n")
    f.close()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
#     )
#     parser.add_argument(
#         "newspaper_array",
#         help="The filename of the movie review you'd like to analyze.",
#     )
#     args = parser.parse_args()
#     process(args.newspaper_array)