import os


# Receives the name of the filename to write to, the element_list, which will be a list of tags or systemCategories that
# will be written as the columns and a dictionary, which contains the membership of each feature to tags or wrapper.
# Those elements are used to create a csv file that displays a matrix easily parsable.
def create_csv(filename, features_to_element, elements_list):
    with open(filename, "w+", newline='') as fp:
        fp.write("," + ",".join(elements_list) + "\n")
        for item in features_to_element.keys():
            fp.write(item + ",")
            for elem in elements_list:
                if elem in features_to_element[item]:
                    fp.write("true,")
                else:
                    fp.write(",")
            fp.write("\n")


def read_txt(filename):
    # Open the file in read mode
    file = open(filename, 'r')

    # Read the contents of the file
    file_contents = file.read()

    # Print the contents of the file
    return file_contents


def convert_to_csv_and_append_new_elements(filename, feature_names, new_elements_list, output_name):
    elements_list = []
    feature_to_element = parse_dict_from_output(read_txt(filename), feature_names, elements_list)
    elements_list.extend(new_elements_list)
    create_csv(output_name, feature_to_element, elements_list)


def parse_dict_from_output(text, features_list, output_element_list):
    feature_to_elements = {}
    for feature in features_list:
        feature_to_elements[feature] = []

    for line in text.split("\n"):
        element = line.split(":")[0]
        output_element_list.append(element)
        features = line.split(":")[1].split(" ")
        for feature in features:
            feature_to_elements[feature].append(element)
    return feature_to_elements


def main():
    tags = ["administration, automation, backup, collaboration, communication, containerization, deployment, documentation, engineering, environment, hosting, meetings, modeling, notifications, organizing, programming, publishing, scripting, search, simulation, social, cloudComputing, mobileApplications, customDesktop, gitFunctions, bashFunctions, systemMaintenance, diagramming, cloudStorage, configuration, clipboardManager, customization, conversion, sql, hacking, contentManagementSystem"]

    feature_names = ["a",
"add",
"aircrackng",
"aisleriot",
"alert",
"ansible",
"ant",
"anydesk",
"apache2",
"ardour",
"aspell",
"audacity",
"AutoFirma",
"axel",
"b",
"bashcolors",
"BFunction",
"blender",
"branch",
"brasero",
"c",
"caffeine",
"calculator",
"calibre",
"carbonLang",
"changebg",
"cheat",
"checkout",
"cheese",
"chess",
"chrome",
"clean",
"clementine",
"clion",
"clone",
"clonezilla",
"cmake",
"cmatrix",
"code",
"codeblocks",
"codium",
"commit",
"config",
"converters",
"copyq",
"curl",
"customizer",
"customizerGUI",
"d",
"dart",
"dbeaver",
"dconfEditor",
"dia",
"discord",
"docker",
"documents",
"drive",
"dropbox",
"drupal",
"duckduckgo",
"e",
"eclipse",
"EFunction",
"emojis",
"evolution",
"f",
"facebook",
"fastcommands",
"fdupes",
"fetch",
"ffmpeg",
"FFunction",
"filezilla",
"firc",
"firefox",
"flutter",
"forms",
"freecad",
"gcc",
"geany",
"geogebra",
"ghostwriter",
"gimp",
"git",
"gitcm",
"github",
"githubDesktop",
"gitk",
"gitlab",
"gitPristine",
"gitprompt",
"gmail",
"gnatGps",
"go",
"google",
"googlecalendar",
"gpaint",
"gparted",
"gradle",
"guake",
"gvim",
"h",
"handbrake",
"hard",
"hardinfo",
"historyoptimization",
"i",
"ideac",
"ideau",
"inkscape",
"instagram",
"ipe",
"ipi",
"ips",
"iqmol",
"j",
"java",
"julia",
"jupyterLab",
"k",
"keep",
"keyboardFix",
"l",
"latex",
"LFunction",
"libreoffice",
"lmms",
"loc",
"lolcat",
"mahjongg",
"matlab",
"mdadm",
"megasync",
"meld",
"mendeley",
"merge",
"mines",
"mvn",
"nano",
"nautilus",
"ncat",
"nedit",
"nemo",
"netflix",
"netTools",
"nmap",
"nodejs",
"notepadqq",
"notflix",
"obsStudio",
"octave",
"okular",
"onedrive",
"opensshServer",
"outlook",
"overleaf",
"p",
"pacman",
"parallel",
"pdfgrep",
"pgadmin",
"php",
"phppgadmin",
"pluma",
"postman",
"presentation",
"prompt",
"psql",
"pull",
"pulseaudio",
"push",
"pycharm",
"pycharmpro",
"pypy3",
"python3",
"pytorch",
"R",
"reddit",
"remmina",
"rosegarden",
"rstudio",
"rsync",
"rust",
"s",
"scala",
"scilab",
"screenshots",
"sherlock",
"shortcuts",
"shotcut",
"shotwell",
"skype",
"slack",
"sonarqube",
"sonicPi",
"soundcloud",
"spotify",
"spreadsheets",
"ssh",
"status",
"steam",
"studio",
"sublime",
"sudoku",
"synaptic",
"sysmontask",
"systemFonts",
"teams",
"teamviewer",
"telegram",
"templates",
"terminal",
"terminalBackground",
"terminator",
"thunderbird",
"tilix",
"tmux",
"tomcat",
"tor",
"traductor",
"transmission",
"trello",
"tumblr",
"tweaks",
"twitch",
"twitter",
"u",
"uget",
"upgrade",
"virtualbox",
"vlc",
"vncviewer",
"vommit",
"whatsapp",
"wikipedia",
"wikit",
"wireshark",
"x",
"xclip",
"youtube",
"youtubeDL",
"youtubeMusic",
"z",
"zoom"]

    convert_to_csv_and_append_new_elements("data/tags.txt", feature_names, tags, "tags.csv")
    convert_to_csv_and_append_new_elements("data/systemcategories.txt", feature_names, [], "systemcategories.csv")


if __name__ == '__main__':
    main()

