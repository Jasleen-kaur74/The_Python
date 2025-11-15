""". What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20')"""


s = set()
s.add(20)                         #this is beacuse python check if these are numerically equal or not
s.add(20.0)                        # and as 20==20.0 numerically so hence it treats them as duplicate elements
s.add('20')                     #and as sets dont have duplicate elements hence it ignores one

print(len(s))