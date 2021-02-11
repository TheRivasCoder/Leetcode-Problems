myEmails = ["test.email+alex@leetcode.com",
"test.e.mail+bob.cathy@leetcode.com",
"testemail+david@lee.tcode.com",
"t.est.email+alex@leetcode.com",
"test.e.mail+bob@leet.code.com",
"test+emaildavid@leetcodecom"]

class Solution:
    def numUniqueEmails(emails):
        
        new_email_list = set()
        
        for email in emails:
            name, domain = email.split('@')
            name = name.replace('.', '')
            name = name.split('+')[0]
            new_email = ''.join(name + '@' + domain)
            new_email_list.add(new_email)
            
        return len(new_email_list)


print(Solution.numUniqueEmails(myEmails))