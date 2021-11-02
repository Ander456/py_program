# Introduction to Venn Graph and Set in Python (Check Unique String)
# Set 只允许唯一key的容器

a = set()
b = set([1,2,3,3,2,5])

print(b)

# 判断传入的s是否是一个set
def unique(s):
    st = set()
    for i in s:
        if i in st:
            return False
        st.add(i)
    return True


print(unique([1,2,3,3]))


def unique2(s):
    return len(set(s)) == len(s)


print(unique([1,2,3,3]))