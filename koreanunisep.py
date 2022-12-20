letters = [
['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'],

['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
                 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'],

['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ',
                 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ',
                 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
                 ]

def koreansep(t):
    outp = []
    t = list(t)
    for i in t:
        if 44032<=ord(i)<=55203:
            outp.append([letters[0][(ord(i)-44032)//588],letters[1][((ord(i)-44032)%588)//28],letters[2][(ord(i)-44032)%28]])
        else:
            outp.append(i)
    return outp

def koreangather(t):
    outp = []
    for i in t:
        if len(i)==3:
            outp.append(chr(letters[0].index(i[0])*588+letters[1].index(i[1])*28+letters[2].index(i[2])+44032))
        else:
            outp.append(str(i))
    return outp
