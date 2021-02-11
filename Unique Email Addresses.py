# List of strings to be passed through function as test
myEmails = ["test.email+alex@leetcode.com",
"test.e.mail+bob.cathy@leetcode.com",
"testemail+david@lee.tcode.com",
"t.est.email+alex@leetcode.com",
"test.e.mail+bob@leet.code.com",
"test+emaildavid@leetcodecom"]

class Solution:
    def numUniqueEmails(emails): # Takes list of emails and return number of unique emails
        
        new_email_set = set() # create set to reamove duplicates of unique emails when added to new_email_set
        
        for email in emails:
            name, domain = email.split('@') # split email into name and domain name
            name = name.replace('.', '') # removes periods from name
            name = name.split('+')[0] # removes characters after '+' symbol in name
            new_email = ''.join(name + '@' + domain) # joins name and domain name into new email with '@' symbol in the middle
            new_email_set.add(new_email) # add new email to new_email_set
            
        return len(new_email_set) # returns number of unique emails in set


print(Solution.numUniqueEmails(myEmails))