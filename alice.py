def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        """Count approximate number of words in the file."""
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = ["Alice in Wonderland.txt", "new book.txt", "guest.txt"]
for filenames in filename:
    count_words(filenames)