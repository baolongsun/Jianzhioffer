# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
# 例如输入字符串”I am a student. “，则输出”student. a am I”。

def reverseWords(s:str):
    if not s or len(s) <= 0:
        return s
    s = s.strip()#去除首位括号
    build = []
    i,j = len(s) - 1,len(s) - 1
    while i >= 0:
        while i >= 0 and s[i] != ' ':
            i -= 1
        build.append(s[i+1:j+1]+' ')
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i
    return ''.join(build).strip()

# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串”abcdefg”和数字2，该函数将返回左旋转两位得到的结果”cdefgab”。
# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"

def reverseLeftWords(s,n):
    build = []
    for i in range(n,n+len(s)):
        build.append(s[i%len(s)])
    return ''.join(build)


if __name__ == "__main__":
    print(reverseWords('Hello World!'))
    print(reverseLeftWords('sfdsfddfe',3))