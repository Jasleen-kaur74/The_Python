#7. Write a program to find out whether a given post is talking about “Harry” or not
post =input("Enter the post: ")

if("Harry".lower() in post.lower()):        #here we added .lower to convert them both in lower case at the time of comparrison
    print("This post is about harry")

else:
    print("This post is not about harry")

    