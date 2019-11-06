def lengthOfLongestSubstring(string):
    highscore = 0
    counter = 1
    if string == " " or len(string) == 1:
        return 1
    elif string == "":
        return 0
    substring = string[0]
    longestString = ""
    for i in range(1, len(string)):
        print("Substring ", substring, " String[i] ", string[i], " Highscore ", len(longestString), " Counter ", counter)
        if string[i] in substring:
            if len(substring) > len(longestString):
                longestString = substring
                counter = 1
            #substring = string[i]
            dupCharsIndex = [i for i, ltr in enumerate(string) if ltr == string[i]]
            index = dupCharsIndex[len(dupCharsIndex)-2]
            substring = string[index:i]
            print("new substring is ", substring)
        else:
            print("before appending", substring)
            substring += string[i]
            print("after appending", substring)
            counter += 1
            if len(substring) > len(longestString):
                longestString = substring
    print("longest string is ", len(longestString), " Longest String", longestString)




lengthOfLongestSubstring("aab") and "dvdf"