file = str(input("File name: ").strip().lower())

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")






# lorena = str(input("Are you stressing about work? ").strip().lower())

# if lorena == "yes":
#     print("We love you and we're here for you, Lorena")
# elif lorena == "no":
#     print("We still love you, Lorena")
# else:
#     print("We love you no matter what, Lorena")


