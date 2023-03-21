import os
import sys

def parse_csv(customizer_project_folder_path, mode, csv_elements_file_path):

    # Obtain path to customizer repository
    if customizer_project_folder_path is None:
        customizer_project_folder_path = ""
        try:
            customizer_project_folder_path = os.environ["CUSTOMIZER_PROJECT_FOLDER"]
            if customizer_project_folder_path == "null":
                print("CUSTOMIZER_PROJECT_FOLDER env variable is not installed. Install customizer and try again or export"
                      " it before executing this script")
                exit(1)
        except KeyError:
            print("CUSTOMIZER_PROJECT_FOLDER variable does not exist")
            exit(1)

    # Read feature keynames from the text file of the repository
    feature_keynames_available = []
    with open(customizer_project_folder_path + "/data/core/feature_keynames.txt", "r") as fp:
        for line in fp.readlines():
            feature_keynames_available.append(line.strip("\n"))

    # Determine what type of data we are reading, categories or tags
    try:
        if mode is None:
            mode = sys.argv[1]
            if not (mode == "tags" or mode == "systemcategories"):
                print("The first argument has to be tags or systemcategories, in order to select the input data type")
                exit(1)
    except IndexError:
        print("You need to supply two arguments")
        exit(1)

    try:
        if csv_elements_file_path is None:
            # Read CSV input file
            csv_elements_file_path = sys.argv[2]
            if csv_elements_file_path == "" or csv_elements_file_path is None:
                print("The second argument has to be path to the CSV file to parse. Because it is not, it will be "
                      " deduced from the mode")
                csv_elements_file_path = customizer_project_folder_path + "/data/core/" + mode + ".csv"

    except IndexError:
        print("The second argument has to be path to the CSV file to parse. Because it is not, it will be "
              " deduced from the mode")
        csv_elements_file_path = customizer_project_folder_path + "/data/core/" + mode + ".csv"

    # Parse csv file
    elements = []
    with open(csv_elements_file_path, "r") as fp:
        # Parse first line
        first_line = fp.readline()
        for elem in first_line.split(",")[1:]:  # Avoid first empty element
            # Skip empty elements
            if elem == "\n" or elem == "":
                continue
            elements.append(elem)

        # Parse each feature
        for line in fp.readlines():
            line_values = line.split(",")
            feature_keyname = line_values.pop(0)  # Obtain feature keyname from the first pos of the line

            # Check that the feature that we are parsing is inside the customizer code
            if feature_keyname not in feature_keynames_available:
                print("WARNING! the feature " + feature_keyname + " is in the CSV but not on the customizer repository"
                                                                  ". Skipping to next value")
                continue

            # For each value in the feature that is true, obtain the corresponding tag and append it to feature_tags
            feature_elements = []
            for i in range(len(line_values)):
                if line_values[i] == "TRUE":
                    feature_elements.append(elements[i])

            # Here the array feature_elements is built. Find the .dat.sh file and append or substitute the current value
            # of the elements in that feature
            dat_content = ""
            with open(customizer_project_folder_path + "/data/features/" + feature_keyname + "/" + feature_keyname + ".dat.sh", "r") as dat_fp:
                dat_content = dat_fp.readlines()
                element_goal_found = False
                for j in range(len(dat_content)):
                    # If we enter the if we have found a matching property. We substitute with our array.
                    if dat_content[j].startswith(feature_keyname + "_" + mode + "="):
                        dat_content[j] = feature_keyname + "_" + mode + "=(\"" + "\" \"".join(feature_elements) + "\")\n"
                        element_goal_found = True

                # If there is not an element property already declared in the dat of the feature, append it
                if not element_goal_found:
                    dat_content.append(feature_keyname + "_" + mode + "=(\"" + "\" \"".join(feature_elements) + "\")\n")

            # rewrite the .dat.sh file that we just parsed
            with open(customizer_project_folder_path + "/data/features/" + feature_keyname + "/" + feature_keyname + ".dat.sh", "w+") as dat_fp:
                dat_fp.write("".join(dat_content))


if __name__ == '__main__':
    parse_csv(None, "tags", None)
    exit(0)
    parse_csv(None, "systemcategories", None)
