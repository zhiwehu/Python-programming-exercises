"""
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
假设我们有一些电子邮件地址username@companyname.com，请编写程序打印给定电子邮件地址的用户名。用户名和公司名称都只由字母组成。

Example:
例子：
If the following email address is given as input to the program:
如果程序输入了以下电子邮件地址：

john@google.com

Then, the output of the program should be:
那么，程序的输出应该是：

john

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。

Hints:
提示：

Use \w to match letters.
使用\w匹配字母。
"""
#本人答案
def get_username(email):
    try:
        username = email.split('@')[0]
        return username
    except IndexError:
        return "Invalid email format"