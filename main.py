import random
import customtkinter

alphabet_syms="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"

#Function to generate password
def generate_pass(specialsymbols=True):
    list1=[]
    str_to_return = ""
    for i in range(10):
        if specialsymbols == True:
            list1.append(alphabet_syms[random.randint(0,len(alphabet_syms)-1)])
    for el in list1:
        str_to_return+=str(el)
    return str_to_return



app = customtkinter.CTk()

app.geometry("400x100")
app.title("Password generator")

app.minsize(400,100)
app.maxsize(400,100)




#Button that generetad password
generate_button = customtkinter.CTkButton(app, text="Generate", command=generate_pass)
generate_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
#Checkbox for checking special symbols in pass
check_special = customtkinter.CTkCheckBox(app, text="Special characters")
check_special.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
#There will be a password here
pass_label = customtkinter.CTkLabel(app, text="CLICK GENERATE")
pass_label.grid(row=0, column=2, padx=20, pady=20)

if __name__ == "__main__":
    app.mainloop()
    print(generate_pass(True))


