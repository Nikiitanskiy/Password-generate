import random
import customtkinter

alphabet_syms="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphabet_spec_syms = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"

#Function to generate password
def generate_pass(specialsymbols=True):
    password = ""
    if specialsymbols == True:
        alphabet = alphabet_spec_syms
    else:
        alphabet = alphabet_syms
    for i in range (10):
        password += random.choice(alphabet)
    return password
           
#Function to change password in label
def change_label():
    special_sym = check_special.get()
    password = generate_pass(specialsymbols=special_sym)
    pass_label.configure(text = password)
    

app = customtkinter.CTk()

app.geometry("400x100")
app.title("Password generator")
#Lock window`s size
app.minsize(400,100)
app.maxsize(400,100)

#Button that generetad password
generate_button = customtkinter.CTkButton(app, text="Generate", command=change_label)
generate_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
#Checkbox for checking special symbols in pass
check_special = customtkinter.CTkCheckBox(app, text="Special characters")
check_special.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
#There will be a password here
pass_label = customtkinter.CTkLabel(app, text="CLICK GENERATE")
pass_label.grid(row=0, column=2, padx=20, pady=20)

if __name__ == "__main__":
    app.mainloop()
