def solution(survey, choices):
    dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        a, b = list(survey[i])
        if choices[i]>4:
            dict[b] += (choices[i]-4)
        else:
            dict[a] += (abs(choices[i]-4))
    result=""
    if dict['R'] >= dict['T']:
        result+="R"
    else:
        result+="T"
    if dict['C'] >= dict['F']:
        result+="C"
    else:
        result+="F"
    if dict['J'] >= dict['M']:
        result+="J"
    else:
        result+="M"
    if dict['A'] >= dict['N']:
        result+="A"
    else:
        result+="N"
    return result