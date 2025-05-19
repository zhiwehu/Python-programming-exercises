"""
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
请编写一个程序来生成所有句子，其中主语在[“I”,“You”]，动词在[“Play”,“Love”]，宾语在[“Hockey”,“Football”]。

Hints:
提示：
Use list[index] notation to get a element from a list.
使用list[index]表示法从列表中获取元素。
"""
# 本人答案
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print(f"{subject} {verb} {obj}")
            