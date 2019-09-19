def load_dictionary(filename):
    dictionary = {}
    try:
        loaded_data = open(filename + ".txt", "r")

    except FileNotFoundError as fnfe:
        print("File not found: " + str(fnfe))
        return []

    except Exception as e:
        print("An error occurred: " + str(e))

    for line in loaded_data.readlines():
        items = line.split()
        if items[0].isnumeric():
            id = int(items[0])
        else:
            print(f"ID must be numeric - Skipping {items[0]}")
            continue
        dictionary[id] = items[1]
    loaded_data.close()
    return dictionary

def save_dictionary(filename, dictionary_to_save):
    try:
        with open(filename + ".txt", 'w+') as dictionary_file:
            for key, value in dictionary_to_save.items():            
                dictionary_file.write(f"{key} {value}\n")        
    except Exception as e:
        print("Unable to save: " + str(e))