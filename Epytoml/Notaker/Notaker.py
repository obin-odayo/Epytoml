# Epytomil, Notaker
# Created by: Zhean Ganituen

from datetime import date as dt

# REMEMBER: Change version number in ntkGen() function
# REMEMBER: To add a '\n' at the end of each line that is appended in the ntkTitleHead

# variable that stores all of the content of the Notaker file being created
ntk_ContWhole = ""

# these variables are the variables for the Notaker file being created
# _toc and _main are separated because _toc has to come first but the headers must be complete once it is generated
ntk_ContGen = ""
ntk_ContShut = ""
ntk_ContToc = ""
ntk_ContMain = ""
ntk_ContMakeTitle = ""


# variable that collects all the headerCounts and their corresponding text in a key
ntk_heads = {}

# variable that collects all the ntk_links of the headers, to be used in the table of contents
ntk_links = {}

# variable that stores the author name/s
# this variable must have its key as the author surname and the value as the author name/s
# sample: {1: ["FirstName_1", "Surname_1"], 2: ["FirstName_2", "Surname_2"] ... }
ntk_authors = {}


# variable that stores the creation date of the file
ntk_date = {"month": "", "day": "", "year": ""}


def ntkGen(fileName):
    # ntkFile is the output of the Notaker, append all user inputs here.
    file = fileName + ".html"

    #'<title>fileName</title>\n'
    ntkTitle = "<title>" + fileName + "</title>\n"
    ntkTitleHead = "<h1><b>" + fileName + "</b></h1>\n"

    # write the beginning of an html document
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    # <meta charset="UTF-8">
    # <meta http-equiv="X-UA-Compatible" content="IE=edge">
    # <meta name="viewport" content="width=device-width, initial-scale=1.0">
    # <title>Document</title>
    # </head>
    # <body>

    global ntk_ContGen
    ntk_ContGen += "<!DOCTYPE html>\n"
    ntk_ContGen += '<html lang="en">\n'
    ntk_ContGen += "<head>\n"
    ntk_ContGen += '<meta charset="UTF-8">\n'
    ntk_ContGen += '<meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
    ntk_ContGen += (
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    )
    ntk_ContGen += ntkTitle
    ntk_ContGen += "</head>\n"
    ntk_ContGen += "<body>\n"
    ntk_ContGen += "<!-- Created with Epytoml and Notaker. Version 1.0 --> \n"
    ntk_ContGen += "<!-- Notaker Start --> \n"
    ntk_ContGen += ntkTitleHead


def ntkShut():
    # write the end of an html document
    # </body>
    # </html>

    global ntk_ContGen
    global ntk_ContMakeTitle
    global ntk_ContToc
    global ntk_ContMain
    global ntk_ContShut

    ntk_ContShut += "<!-- Notaker End -->\n"
    ntk_ContShut += "</body>\n"
    ntk_ContShut += "</html>\n"

    # append all the content to the ntk_ContWhole variable
    global ntk_ContWhole
    ntk_ContWhole += (
        ntk_ContGen
        + "\n"
        + ntk_ContMakeTitle
        + "\n"
        + ntk_ContToc
        + "\n"
        + ntk_ContMain
        + "\n"
        + ntk_ContShut
        + "\n"
    )


def nl(value):
    global ntk_ContMain
    for i in range(value):
        ntk_ContMain += "<br> \n"


class headerClass:
    def __init__(self):
        # variable that counts how many header 1s are created
        self.headCount = 1

    def h(self, content):
        # Make a header with the given text
        ntkHeader1 = "<h1>" + content + "</h1>\n"

        # Add the header to the ntk_heads dictionary
        ntk_heads[self.headCount] = ntkHeader1

        global ntk_ContMain
        ntk_ContMain += ntkHeader1

        return ntkHeader1

    def makeLink(self, content, autoFormat=None):
        # convert headerNumber to str, so it can be concatenated with ntkRefText
        headerNumberStr = str(self.headCount)

        if autoFormat is None:
            # when no autoFormat is given, use defualt or autoFormat = True
            ntkRefText = "Chapter " + headerNumberStr + ": " + content
        else:
            if autoFormat == True:
                ntkRefText = "Chapter " + headerNumberStr + ": " + content
            elif autoFormat == False:
                ntkRefText = content
            else:
                # when autoFormat is given but input not found, use defualt or autoFormat = True
                ntkRefText = "Chapter " + headerNumberStr + ": " + content

        ntkRef = '<a href="#' + content + '">' + ntkRefText + "</a><br>\n"

        ntk_links[self.headCount] = ntkRef

        return ntkRef

    def makeId(self, content):
        global ntk_ContMain
        # Make a link id to the said header, to be used in the table of contents
        ntkID = '<a id="' + content + '"></a>\n'

        ntk_ContMain += ntkID

        return ntkID

    def headCountAdd(self):
        # increment the headerCount by 1
        self.headCount += 1

    def toc(self, size=None):
        # make a table of contents

        headerValStart = "<h1>"
        headerValEnd = "</h1>"

        # make size=none to make it default to the header 1 size, unless specified
        if size is None or size == 1:
            headerValStart = "<h1>"
            headerValEnd = "</h1>"
        else:
            if size == 2:
                headerValStart = "<h2>"
                headerValEnd = "</h2>"
            elif size == 3:
                headerValStart = "<h3>"
                headerValEnd = "</h3>"
            elif size == 4:
                headerValStart = "<h4>"
                headerValStart = "</h4>"
            else:
                # if input not found then set to default
                headerValStart = "<h1>"
                headerValEnd = "</h1>"

        global ntk_ContToc

        tocTitle = headerValStart + "<b>Table of Contents</b>" + headerValEnd + "\n"

        ntk_ContToc += tocTitle

        for header in range(1, self.headCount):
            linkTitle = ntk_links[header]
            linkTitle += "\n"
            ntk_ContToc += linkTitle


def hh(content):
    ntkHeader2 = "<h2>" + content + "</h2>\n"
    global ntk_ContMain
    ntk_ContMain += ntkHeader2

    return ntkHeader2


def h3(content):
    ntkHeader3 = "<h3>" + content + "</h3>\n"
    global ntk_ContMain
    ntk_ContMain += ntkHeader3

    return ntkHeader3


def h4(content):
    ntkHeader4 = "<h4>" + content + "</h4>\n"
    global ntk_ContMain
    ntk_ContMain += ntkHeader4

    return ntkHeader4


def h5(content):
    ntkHeader5 = "<h5>" + content + "</h5>\n"
    global ntk_ContMain
    ntk_ContMain += ntkHeader5

    return ntkHeader5


def h6(content):
    ntkHeader6 = "<h6>" + content + "</h6>\n"
    global ntk_ContMain
    ntk_ContMain += ntkHeader6

    return ntkHeader6


def t(content, emphasis=None):
    # write text to the main body of the Notaker file
    # text does not insert a <br> at the end of the text
    emphasis = emphasis.lower()
    if emphasis is None:
        # default text when there are no emphasis tags specified
        ntkP = "<p>" + content + "</p>\n"
    else:
        if emphasis == "b" or emphasis == "bold" or emphasis == "1":
            # bold text
            ntkP = "<p><b>" + content + "</b></p>\n"
        elif emphasis == "i" or emphasis == "italic" or emphasis == "2":
            # italic text
            ntkP = "<p><i>" + content + "</i></p>\n"
        elif emphasis == "u" or emphasis == "underline" or emphasis == "3":
            # underline text
            ntkP = "<p><u>" + content + "</u></p>\n"
        else:
            # if input not found then set to default
            ntkP = "<p>" + content + "</p>\n"

    global ntk_ContMain
    ntk_ContMain += ntkP

    return ntkP


def tL(content, emphasis=None):
    # write text to the main body of the Notaker file
    # textL inserts a <br> at the end of the text

    if emphasis is None:
        # default text when there are no emphasis tags specified
        ntkP = "<p>" + content + "</p><br>\n"
    else:
        if emphasis == "b" or emphasis == "bold" or emphasis == "1":
            # bold text
            ntkP = "<p><b>" + content + "</b></p><br>\n"
        elif emphasis == "i" or emphasis == "italic" or emphasis == "2":
            # italic text
            ntkP = "<p><i>" + content + "</i></p><br>\n"
        elif emphasis == "u" or emphasis == "underline" or emphasis == "3":
            # underline text
            ntkP = "<p><u>" + content + "</u></p><br>\n"
        else:
            # if input not found then set to default
            ntkP = "<p>" + content + "</p><br>\n"

    global ntk_ContMain
    ntk_ContMain += ntkP

    return ntkP


def makeTitle(authorNames, date=None, dateFormat=None):
    # creates a title for the Notaker file after ntk_ContGen
    global ntk_ContMakeTitle

    # code for name formatting

    authorFirstName = {}
    authorSurname = {}

    titleAuthor = ""

    for author in range(1, len(authorNames) + 1):
        # first name of author
        # save in authorFirstName dictionary
        authorFirstName[author] = authorNames[author][0]

        # surname of author
        # save in authorSurname dictionary
        authorSurname[author] = authorNames[author][1]

    titleDate = ""

    if date is None:
        monthNames = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        # if no date is specified, get the current month and year

        titleYear = dt.today().year
        titleYear = str(titleYear)

        titleMonth = dt.today().month
        # convert month to month name
        titleMonth = monthNames[titleMonth - 1]

        titleDate = titleMonth + " " + titleYear

    else:
        # if a date is specified, use it.
        titleYear = date["year"]

        titleDay = date["day"]

        titleMonth = date["month"]

    if date is not None:
        # only allow date formatting if dates (day, month, and year) is specified
        if dateFormat is None:
            # if no date format is specified, set the date format to the default (Month YYYY)
            titleDate = titleYear + " " + titleMonth
        elif dateFormat == "1":
            # dateFormat 1 is Month DD, YYYY
            titleDate = titleMonth + " " + titleDay + ", " + titleYear
        elif dateFormat == "2":
            # dateFormat 2 is YYYY
            titleDate = titleYear
        else:
            # if input not found then set to default
            titleDate = titleYear + " " + titleMonth

    # add the title

    # <h2><b> titleAuthor </b></h2>
    # <h2><b> titleDate </b></h2>

    # count authors to check if we're going to use et al. and <abbr>
    titleAuthor += "<h2><b>"
    if len(authorNames) >= 6:
        titleAuthor += authorFirstName[1] + " " + authorSurname[1] + '<abbr title="'
        for i in range(2, len(authorNames) + 1):
            if i == len(authorNames):
                titleAuthor += authorFirstName[i] + " " + authorSurname[i]
            else:
                titleAuthor += authorFirstName[i] + " " + authorSurname[i] + ", "
        titleAuthor += '"> et al. </abbr>'
    else:
        for i in range(1, len(authorNames) + 1):
            if i == len(authorNames):
                titleAuthor += authorFirstName[i] + " " + authorSurname[i]
            else:
                titleAuthor += authorFirstName[i] + " " + authorSurname[i] + ", "

    titleAuthor += "</b></h2>\n"

    titleDate = "<h2><b>" + titleDate + "</b></h2>\n"

    ntk_ContMakeTitle = titleAuthor + titleDate


def lightUpBlock(content, textColor=None, highlightColor=None):
    # highlight block text with given content

    global ntk_ContMain

    # check if textColor is specified
    if textColor is None:
        # if text color is not specified, set to default
        color = "color: " + "black" + ";"
    else:
        # if text color is specified, use it
        color = "color: " + textColor + ";"

    # check if highlightColor is specified
    if highlightColor is None:
        # if highlight color is not specified, set to default
        bgColor = "background-color: " + "yellow"
    else:
        # if highlightColor is specified, use it
        bgColor = "background-color: " + highlightColor

    ntk_ContMain += '<div style="' + color + bgColor + '">' + content + "</div>"


def lightUpBlockS(textColor=None, highlightColor=None):
    # start highlighting block
    # not only does it highlight the text, but it highlights the whole line where the text is located

    global ntk_ContMain

    # check if textColor is specified
    if textColor is None:
        # if text color is not specified, set to default
        color = "color: " + "black" + ";"
    else:
        # if text color is specified, use it
        color = "color: " + textColor + ";"

    # check if highlightColor is specified
    if highlightColor is None:
        # if highlight color is not specified, set to default
        bgColor = "background-color: " + "yellow"
    else:
        # if highlightColor is specified, use it
        bgColor = "background-color: " + highlightColor

    ntk_ContMain += '<div style="' + color + bgColor + '">'


def lightUpBlockE():
    # End highlighting block

    global ntk_ContMain

    ntk_ContMain += "</div>"


def lightUp(content, textColor=None, highlightColor=None):
    # highlight text with given content

    global ntk_ContMain

    # check if textColor is specified
    if textColor is None:
        # if text color is not specified, set to default
        color = "color: " + "black" + ";"
    else:
        # if text color is specified, use it
        color = "color: " + textColor + ";"

    # check if highlightColor is specified
    if highlightColor is None:
        # if highlight color is not specified, set to default
        bgColor = "background-color: " + "yellow"
    else:
        # if highlightColor is specified, use it
        bgColor = "background-color: " + highlightColor

    ntk_ContMain += '<span style="' + color + bgColor + '">' + content + "</span>"


def lightUpS(textColor=None, highlightColor=None):
    # start highlight text
    # highlight text without given content
    # the difference between `lightUp` and `lightUpBlock`:
    # `lightUp` uses span tags to highlight the text, same line
    # `lightUpBlock` uses div tags to highlight the text, new line

    global ntk_ContMain

    # check if textColor is specified
    if textColor is None:
        # if text color is not specified, set to default
        color = "color: " + "black" + ";"
    else:
        # if text color is specified, use it
        color = "color: " + textColor + ";"

    # check if highlightColor is specified
    if highlightColor is None:
        # if highlight color is not specified, set to default
        bgColor = "background-color: " + "yellow"
    else:
        # if highlightColor is specified, use it
        bgColor = "background-color: " + highlightColor

    ntk_ContMain += '<span style="' + color + bgColor + '">'


def lightUpE():
    # End highlighting block

    global ntk_ContMain

    ntk_ContMain += "</span>"


def note(content, borderColor=None, textColor=None, autoHide=None, summaryText=None):
    # create a note

    # check if borderColor is specified
    if borderColor is not None:
        # if border color is specified, use it
        borderStyle = "border-left: 5px solid " + borderColor + "; "
    else:
        # if border color is not specified, set to default (red)
        borderStyle = "border-left: 5px solid red; "

    # check if color is specified
    if textColor is not None:
        color = "color: " + textColor
    else:
        # if color is not specified, set to default
        color = "color: black"

    global ntk_ContMain

    blockQuoteStart = '<blockquote style="' + borderStyle + color + '">'
    blockQuoteEnd = "</blockquote>"

    if autoHide == False:
        # if autoHide is False, do not auto hide the note
        ntk_ContMain += blockQuoteStart

        ntk_ContMain += '<p style="margin-left: 10px">'

        ntk_ContMain += content

        ntk_ContMain += "</p>"

        ntk_ContMain += blockQuoteEnd
    elif autoHide == True:
        # if autoHide is True, auto hide the note

        ntk_ContMain += "<details>"

        # check if there is a summaryText specified
        if summaryText is not None:
            # if there is summaryText specified, use it
            ntk_ContMain += "<summary>" + summaryText + "</summary>"
        else:
            # if there is no summaryText specified, use default
            ntk_ContMain += "<summary>Notes:</summary>"

        ntk_ContMain += blockQuoteStart

        ntk_ContMain += '<p style="margin-left: 10px">'

        ntk_ContMain += content

        ntk_ContMain += "</p>"

        ntk_ContMain += blockQuoteEnd

        ntk_ContMain += "</details>"
    else:
        # if other input is given, use default
        ntk_ContMain += blockQuoteStart

        ntk_ContMain += '<p style="margin-left: 10px">'

        ntk_ContMain += content

        ntk_ContMain += "</p>"

        ntk_ContMain += blockQuoteEnd


class shortcutsClass:
    def __init__(self):
        # count how many shortcuts are there
        self.shortcutCount = 1
        # dictionary filled with the shortcuts
        # sample: {1: ["Address", "Value"], 2: ["Address_2", "Value_2"] ... }
        self.shortcutList = {}

    def addShortcut(self, address, value):
        # adds a shortcut to the shortcut list
        # check if the key provided has an address

        if "!" in address or "@" in address or "$" in address:
            # key already has an address
            self.shortcutList[self.shortcutCount] = [address, value]
        else:
            # key doesnt have an address
            # set a default address to the key
            address = "@" + address
            self.shortcutList[self.shortcutCount] = [address, value]

        # append 1 to the value of shortcutCount
        self.shortcutCount += 1

    def mergeShortcut(self, dictionary):
        # merge a dictionary with the shortcut list
        self.shortcutList = self.shortcutList | dictionary

    def viewShortcut(self, printList=None, key=None):
        # lets the user view the shortcut list or a specific shortcut
        if key is None:
            # if key is none, return all the shortcuts
            if printList == True:
                # if print is true, print and return the shortcuts
                print(self.shortcutList)
                return self.shortcutList
            else:
                # if print is false, return the shortcuts
                return self.shortcutList
        else:
            # if key is not none, return the specific shortcut
            if printList == True:
                # if print is true, print and return the specific shortcut
                print(self.shortcutList[key])

    def viewRangeShortcut(self, rangeMin, rangeMax, printList=None):
        # lets the user view a range of shortcuts
        for key in range(rangeMin, rangeMax + 1):
            # for each key in range, print the shortcut
            # check if printList is not None
            if printList is None:
                # if printList is None, return the shortcut
                return self.shortcutList[key]
            else:
                # if printList is not None, print the shortcut
                if printList == True:
                    # if printList is True, print the shortcut
                    print(self.shortcutList[key])
                elif printList == False:
                    # if printList is False, return the shortcut
                    return self.shortcutList[key]
                else:
                    # if printList is not True or False, print the shortcut
                    print(self.shortcutList[key])

    def readMain(self):
        # read the ntk_ContMain variable (or the main content of the Notaker file created)
        # and check for any shortcuts, and replace the shortcut address with the value
        global ntk_ContMain

        for key in self.shortcutList:
            # iterate for each key in the shortcut list
            
            # {key: [shortcutAddress, shortcutValue]
            
            # give the value of the shortcut address to shortcutAddress
            shortcutAddress = self.shortcutList[key][0]
            
            # give the value of the shortcut value to shortcutValue
            shortcutValue = self.shortcutList[key][1]
            
            # check if the shortcut address is in the content then replace the key with the value
            ntk_ContMain = ntk_ContMain.replace(shortcutAddress, shortcutValue)