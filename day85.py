# -- coding: utf-8 --
# Algorithm to Reverse Words in a Sentence
# 翻转一个句子中的单词 
# 比如 "Alex and Mio" => "Mio and Alex" 而不是 字母翻转

# 我们可以先让字母翻转 变成oiM dna xelA 然后 每一块再翻转字母就变成了 Mio and Alex
# 我们要注意一个问题是 python里 string是不能修改的 immutable 比如s = "Alex" 你可以 s[0] == "A" 但是不能s[0] = "Z" 所以我们下面给他转换成list来[]修改
def reverseWord(sentence):
    def rev(s, i, j):
        while i < j:
            #双指针
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
    s = list(sentence[::-1]) # [::-1] 表示reversed ex:得到"oiM dna xelA"
    prev = 0
    for i, c in enumerate(s): # 遍历每一段然后 rev
        if c == " ":
            rev(s, prev, i - 1)
            prev = i + 1
    rev(s, prev, len(s)-1)
    return "".join(s)

print(reverseWord("Alex and Mio"))

# python里简化
def reverseWord2(sentence):
    return "".join(reversed(sentence.split(" "))) #其实就是 切割 再翻转