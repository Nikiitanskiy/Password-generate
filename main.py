import random
import customtkinter



app = customtkinter.CTk()

app.geometry("400x100")
app.title("Password generator")



#Function to generate password
def generate_pass():
    return None


generate_button = customtkinter.CTkButton(app, text="Generate", command=generate_pass)
generate_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

check_special = customtkinter.CTkCheckBox(app, text="Special characters")
check_special.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

pass_label = customtkinter.CTkLabel(app, text="CLICK GENERATE")
pass_label.grid(row=0, column=2, padx=20, pady=20)

if __name__ == "__main__":
    app.mainloop()



