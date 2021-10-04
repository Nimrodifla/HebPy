from bidi.algorithm import get_display

words = {
    "אם": "if",
    "הדפס": "printf",
    "אחרת אם": "elif",
    "אחרת": "else",
    "קלט": "input",
    "אמת": "True",
    "שקר": "False",
    "כל עוד": "while",
    "לכל": "for",
    "בתוך": "in",
    "טווח": "range"
    }

def printf(s):
    print(get_display(s))

printf("שפת תכנות בעברית:\n\n")

runCmd = "הרץ"

while True:
    printf("קוד:")
    code = ""
    flag = True
    i = 0
    while (flag):
        i += 1
        # write code
        temp = input("")
        if temp == runCmd:
            flag = False
        else:
            # encode from hebrew to english
            hebTemp = temp
            for hw in words:
                hebTemp = hebTemp.replace(hw, words[hw])
            # add to code
            code += hebTemp + "\n"


    printf("\n\nהרצה:\n")
    exec(code)
    printf("\n\n\n\n")
