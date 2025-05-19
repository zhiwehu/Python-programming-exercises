"""
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
网站要求用户输入用户名和密码进行注册。编写一个程序来检查用户输入的密码的有效性。

Following are the criteria for checking the password:
以下是检查密码的标准：

1. At least 1 letter between [a-z]
1.[a-z]之间至少有一个小写字母
2. At least 1 number between [0-9]
2.[0-9]之间至少有一个数字
1. At least 1 letter between [A-Z]
1.[A-Z]之间至少有一个大写字母
3. At least 1 character from [$#@]
3.[$#@]中至少有1个字符
4. Minimum length of transaction password: 6
4.交易密码最小长度:6
5. Maximum length of transaction password: 12
5.交易密码最大长度:12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
您的程序应接受逗号分隔的密码序列，并将根据上述标准进行检查。将打印符合标准的密码，每个密码用逗号分隔。

Example
例子

If the following passwords are given as input to the program:
如果程序输入了以下密码：

ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:
那么，程序的输出应该是：

ABd1234@1

"""

str1=input().split(',')
str2=[]
for i in str1:
    if len(i)<6 or len(i)>12:
        continue
    if not i.isupper:
        continue
    if not i.islower:
        continue
    if not i.isdigit:
        continue
    if not any(c in '$#@' for c in i):
        continue
    str2.append(i)
print(','.join(str2))