# here in xxargs we use ** which uses the dictionary format to save or return the arguements

def user_info(**user):
    print(user)
    
user_info(id = "1", name = "Sumeet", dept = "BOS")