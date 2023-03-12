def str_to_int(exp):
    s = ''
    num_dict = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9', 'ten': '10', 'hundred': '100', 'substract': '-', 'plus': '+', 'division': '/', 'multiple': '*', 'equals': '=', 'eleven': '11',
                'twelve': '12', 'thirteen': '13', 'fourteen': '14', 'fifteen': '15', 'sixteen': '16',
                'seventeen': '17', 'eighteen': '18', 'nineteen': '19', 'twenty': '2', 'thirty': '3', 'forty': '4', 'fifty': '5', 'sixty': '6', 'seventy': '7', 'eighty': '8', 'ninety': "9"}
    for i in exp:
        if i in ['and', 'hundred']:
            continue
        elif i in num_dict.keys():
            s += num_dict[i]
        else:
            s += i
    return s

with open("input.txt",'r') as file:
    lst=file.read().splitlines()
    for i in range(1,int(lst[0])+1):
        demo = str_to_int(lst[i].split()).split("=")
        with open("output.txt",'a') as files:
            files.write(('true' if eval(demo[0]) == float(demo[1]) else 'false')+'\n')
