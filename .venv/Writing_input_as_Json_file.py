import json
def save_user_data():
    user_list=[]
    while True:
        name=input("Enter name ( or 'quit' to exit the program) :")
        if name=='quit':
            break
        email=input("Enter Email")
        Contac=input("Enter Contact")

        user_data={
            "name":name,
            "email":email,
            "contact":Contac
        }
        user_list.append(user_data)
        with open("user_data.json",'w') as file:
            json.dump(user_list,file)
        print("User Data Saved Successfully")

save_user_data()