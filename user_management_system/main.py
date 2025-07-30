import customtkinter as ctk
from CTkMenuBar import *
from CTkMessagebox import *

# Set window appearance and theme color.
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

def center_window(window, width, height):
    """Centers the window on the screen based on the user's screen resolution."""
    
    # Ensure the window is up to date.
    window.update_idletasks()

    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate coordinates to center the window.
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set window size and location.
    window.geometry(f"{width}x{height}+{x}+{y}")

class LoginFrame(ctk.CTkFrame):
    """Custom login form frame for user authentication.
    
    Provides entry field for username and password, along 
    with buttons for login, password visibility toggle, 
    and navigation to signup form.

    Parameters:
        master (widget): The parent widget for this frame.
        switch_to_login_callback (Callable): A function to switch to the signup form when triggered.
    """

    def __init__(self, master, switch_to_singup_callback):
        super().__init__(master)
        self.master = master
        self.switch_to_signup_callback = switch_to_singup_callback
        self.create_widgets()

    def create_widgets(self):
        """Create all elements displayed in the login form."""

        self.rowconfigure((0, 1, 2, 3, 4 ,5, 6), weight = 0) # Prevent row expansion.

        # Set column 2 to take up available space; others remain fixed.
        self.columnconfigure(0, weight=0) 
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1) 
        self.columnconfigure(3, weight=0) 

        # Add label and entry for username/email.
        ctk.CTkLabel(self, text= "Username/Email").grid(row= 0,  sticky = "w", padx = 10, pady = (5, 0))
        self.username_email_entry = ctk.CTkEntry(self)
        self.username_email_entry.grid(row= 1, columnspan = 4, sticky = "ew", padx = 10, pady = (0, 20))

        # Add password label and masked entry field (using '*').
        ctk.CTkLabel(self, text= "Password").grid(row= 2, sticky = "w", padx = 10)
        self.password_entry = ctk.CTkEntry(self, show = "*")
        self.password_entry.grid(row= 3, columnspan = 3, sticky = "ew", padx = (10, 0))

        # Add toggle button beside password entry that switches between 'Show' and 'Hide' states.
        self.show_password_button = ctk.CTkButton(self, width= 50, text = "Show", command= lambda: show_password_toggle(self.password_entry, self.show_password_button))
        self.show_password_button.grid(row= 3, column = 3, padx = (0, 10), sticky = "ns")

        # Add clickable "Forgot Password?" label to trigger password reset.
        self.forgot_password_label = ctk.CTkLabel(self, text = "Forgot Password?", text_color="cyan")
        self.forgot_password_label.bind("<Button-1>", lambda e: print("Under Development.")) # Password reset window(under dev).
        self.forgot_password_label.grid(row = 4, column = 0, sticky = "w", padx = 10, pady = (0, 10))

        # Add login button to confirm credentials and (eventually) redirect to dashboard.(under development).
        self.login_button = ctk.CTkButton(self, text = "Login", height = 45, command= lambda: print("Under Development."))
        self.login_button.grid(row = 5, columnspan = 4, sticky = "ew", padx = 10)

        # Add "Don't have an account?" label and clickable "Click here!" label to switch to signup form.
        ctk.CTkLabel(self, text= "Don't have an account?").grid(row=6, column = 0, sticky = "w", padx = (10, 5))
        self.signup_label = ctk.CTkLabel(self, text = "Click here!", text_color="cyan")
        self.signup_label.bind("<Button-1>", lambda e: go_to_signup())
        self.signup_label.grid(row = 6, column = 1, sticky = "w")

class SignupFrame(ctk.CTkFrame):
    """Custom login form frame for user registration.

        Provide entry field for firstname, middlename, lastname, email,
        username and password, along with button for signup, password
        visibility toggle and navigation to login form.

        Parameters:
            master (widget): The parent widget for this frame.
            switch_to_login_callback (Callable): A function to swich to the signup form when trigerred. 
    """
    def __init__(self, master, switch_to_login_callback):
        super().__init__(master)
        self.master = master
        self.switch_to_login_callback = switch_to_login_callback
        self.create_widgets()

    def create_widgets(self):
        """Create all the elements widget in signup form."""

        # Prevent row expansion.
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight = 0) 

        # Set columns 0 and 1 to take available space; column 2 remains fixed.
        self.columnconfigure((0, 1), weight = 1)
        self.columnconfigure(2, weight = 0)

        # Create frame to group first to last name label and entry field.
        self.frame_info_field = ctk.CTkFrame(self, fg_color= "transparent")
        self.frame_info_field.grid(row = 0, columnspan = 3, sticky = "ew", padx = 10, pady = (5, 0))
        self.frame_info_field.columnconfigure((0, 1, 2), weight = 1)

        # Add first to last name label.
        self.firstname_label = ctk.CTkLabel(self.frame_info_field, text= "Firstname")
        self.firstname_label.grid(row = 0, column= 0, sticky = "w")
        self.middlename_label = ctk.CTkLabel(self.frame_info_field, text= "Middlename")
        self.middlename_label.grid(row = 0, column = 1, sticky = "w")
        self.lastname_label = ctk.CTkLabel(self.frame_info_field, text= "Lastname")
        self.lastname_label.grid(row = 0, column = 2, sticky = "w")

        # Add first to last name entry field.
        self.firstname_entry = ctk.CTkEntry(self.frame_info_field)
        self.firstname_entry.grid(row = 1, column = 0, sticky = "ew")
        self.middlename_entry = ctk.CTkEntry(self.frame_info_field)
        self.middlename_entry.grid(row = 1, column = 1, sticky = "ew")
        self.lastname_entry = ctk.CTkEntry(self.frame_info_field)
        self.lastname_entry.grid(row = 1, column = 2, sticky = "ew")

        # Add label and entry field for email.
        self.email_label = ctk.CTkLabel(self, text= "Email")
        self.email_label.grid(row= 2, column = 0, padx = 10, sticky = "w")
        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.grid(row = 3, columnspan = 3, sticky= "ew", padx= 10, pady = (0, 5))

        # Add label and entry field for username.
        self.username_label = ctk.CTkLabel(self, text= "Username")
        self.username_label.grid(row= 4, column = 0, padx = 10, sticky= "w")
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row = 5, columnspan = 3, sticky = "ew", padx = 10, pady = (0, 5))
        
        # Add password label and masked entry field (using '*').
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.grid(row= 6, column = 0, padx = 10, sticky = "w")
        self.password_entry = ctk.CTkEntry(self, show = "*")
        self.password_entry.grid(row = 7, columnspan = 2, sticky = "ew", padx = (10, 0), pady = (0, 20))

        # Add toggle button beside password entry that switches between 'show' and 'hide'.
        self.show_password_button = ctk.CTkButton(self, text= "Show", width= 50, command = lambda: show_password_toggle(self.password_entry, self.show_password_button))
        self.show_password_button.grid(row = 7, column = 2, sticky = "w", padx = (0, 10), pady = (0, 20))

        # Add signup button to confirm signup information.
        self.button_signup = ctk.CTkButton(self, text = "Signup", height= 45, command= self.on_signup_click)
        self.button_signup.grid(row = 8, columnspan = 3, sticky = "ew", padx = 10)

        # Create frame to group "Already have an account?" label and "Click here!" label to the bottom of the window.
        self.frame_already = ctk.CTkFrame(self, fg_color= "transparent")
        self.frame_already.grid(row = 9, columnspan = 3, sticky = "w", padx = 10)

        # Add "Already have an account?" label.
        self.label_already = ctk.CTkLabel(self.frame_already, text = "Already have an Account?")
        self.label_already.pack(side="left")

        # Add clickable "Click here!" label next to "Already have an account?" label to switch to login form.
        self.to_login_label = ctk.CTkLabel(self.frame_already, text = "Click here!", text_color="cyan")
        self.to_login_label.bind("<Button-1>", lambda e: go_to_login())
        self.to_login_label.pack(side="left", padx = (5, 0))

    def on_signup_click(self):
        """Commands after signup button is pressed."""

        self.firstname = self.firstname_entry.get()
        self.middlename = self.middlename_entry.get()
        self.lastname = self.lastname_entry.get()
        self.email = self.email_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        if self.validate_signup():
            # If the information is valid:
            print("valid")
            self.confirm_signup()
        else:
            print("invalid")

    def validate_signup(self):
        """Check if the information entered is valid."""

        is_valid = None

        if not is_names_valid(self.firstname, self.middlename, self.lastname):
            # If name is not valid:
            is_valid = False

        if not is_email_valid(self.email):
            # If email is not valid:
            is_valid = False
        
        if not is_username_valid(self.username):
            # If username is not valid:
            is_valid = False
        
        if not is_password_valid(self.password):
            # If password is not valid:
            is_valid = False

        if is_valid == None:
            # If is_valid is none:

            # Set is_valid to true.
            is_valid = True

        # If all information entered is valid return true.
        return is_valid
    
    def confirm_signup(self):
        """Signup information Confirmation Messagebox."""
        result = CTkMessagebox(
            master= self.master,
            title= "Confirm Your Signup Information",
            message= 
            "\nFirst Name: " + self.firstname +
            "\nMiddle Name: " + self.middlename +
            "\nLast Name: " + self.lastname +
            "\nEmail Name: " + self.email +
            "\nUsername: " + self.username +
            "\n\nAre these informations correct?",
            icon = "question",
            option_1="Cancel",
            option_2="No",
            option_3="Yes"
        )
    
def is_names_valid(*names):
        """Check if names are at least 2 characters and only alphabetic."""

        for name in names:
            # Iterates through all names.

            if len(name) <= 1 or not name.isalpha():
                # If name is less than or equal to 1 and not all characters are in alphabeth:
                return False

        # Returns true if all name iteration is valid.
        return True

def is_email_valid(email):
    """Check if email entered is valid."""

    return True

def is_username_valid(username: str):
    """Check if username entered is valid."""
    
    # Returns true if username input is atleast 2 or more characters and starts with a letter.
    return len(username) > 1 and username.strip().isalpha

def is_password_valid(password):
    """check if password entered is valid."""

    # Return true if password input is greater or equal to 6 charaters.
    return len(password) >= 6

def show_password_toggle(password_entry, show_password_button):
    """Toggle the visibility of text of the password entry and update the button text.
    
        Parameters:
            password_entry (CTkEntry): The entry widget where the password it typed.
            show_password_button (CTkButton): The button used to toggle visibility.
    """

    if password_entry.cget("show") == "":
        # If the password is currently visible (not masked):

        # Mask password entry field with "*"
        password_entry.configure(show = "*")

        # Change the button text to "Show".
        show_password_button.configure(text = "Show")
    else:
        # if the password is currently hidden (masked):

        # Unmaskt the password entry field.
        password_entry.configure(show = "")

        # Change the button text to "Hide".
        show_password_button.configure(text = "Hide")

def confirm_exit():
    """Show a messagebox for exit confirmation."""
    
    # Opens a messagebox asking if the user wants to exit the application.
    result = CTkMessagebox(
        master = app,
        width=100,
        height=50,
        title = "Exit application",
        message= "Are you sure you want to exit?",
        icon = "question",
        option_1= "Cancel",
        option_2= "No",
        option_3= "Yes"
    )

    if result.get()=="Yes":
        # if the user chose the "Yes" option:

        # Exit the application.
        app.quit()

def confirm_reset_form():
    """Show a messagebox for reseting the form confirmation."""

    # Opens a messagebox asking if the user wants to reset the current form.
    result = CTkMessagebox(
        master=app,
        width=100,
        height=50,
        title= "Reset Form",
        message= "Are you sure you want to reset the current form?",
        icon="question",
        option_1="Cancel",
        option_2="No",
        option_3="Yes"
    )

    if result.get()=="Yes":
        # If the user chose the "Yes" option:

        # Reset the current form the user is in.
        reset_form(current_frame)

def go_to_signup():
    """Switch the current form to signup form.
    
        Hides the login frame, reset its field, displays the signup frame,
        resizes the main window accordingly, and updates the state tracking label.
    """

    # Set current_frame accessible at the global level.
    global current_frame

    # Hide the login frame.
    login_frame.pack_forget()

    # Update the state label to indicate the signup form.
    state_label.configure(text = "SIGNUP FORM")

    # Clear all fields in the login form.
    reset_form(login_frame)

    # Display the signup frame, expanding to fill the window.
    signup_frame.pack(fill="both", expand=True)

    # Resize the window to match the signup form layout.
    app.geometry("400x400")

    # Print transition for debugging.
    print("Switching to Signup screen...")

    # Track the current active frame.
    current_frame = signup_frame

def go_to_login():
    """Switch the current form to login form.
    
        Hides the signup frame, reset its field, display the login frame,
        resizs the main window accordingly, and updates the state tracking label.
    """

    # Set current_frame accessible at the global level.
    global current_frame

    # Hide the sign up frame.
    signup_frame.pack_forget()

    # Clear all fields in the singup form.
    reset_form(signup_frame)

    # Update the state label to indicate the login form.
    state_label.configure(text = "LOGIN FORM")

    # Display the login frame, expanding to fill the window.
    login_frame.pack(fill="both", expand=True)

    # Resize the window to mach the login form.
    app.geometry("400x320")

    # Print transition for debugging
    print("Switching to Login screen...")

    # Track the current active frame.
    current_frame = login_frame

def reset_form(frame):
    """Reset all fields of the form.

        Parameters:
            frame (CTkFrame): the frame where fields are remove.
    """

    if isinstance(frame, LoginFrame):
        # If the instance of the frame is LoginFrame:
        
        # Remove all characters from the username/email and password entries.
        frame.username_email_entry.delete(0, "end")
        frame.password_entry.delete(0, "end")

    elif isinstance(frame, SignupFrame):
        # If the instance of the frame is SignupFrame:

        # Remove all characters from the personal details, email, username and password entries.
        frame.firstname_entry.delete(0, "end")
        frame.middlename_entry.delete(0, "end")
        frame.lastname_entry.delete(0, "end")
        frame.email_entry.delete(0, "end")
        frame.username_entry.delete(0, "end")
        frame.password_entry.delete(0, "end")

    if(frame.password_entry.cget("show") == ""):
            # If the password entry is visible:

            # Set the password entry to its default state (masked).
            show_password_toggle(frame.password_entry, frame.show_password_button)

def light_dark_mode(button_text):
    """Set light and dark mode theme.

        Parameters:
            mode (Str): The "Light Mode" or "Dark Mode" mode.
    """


    if button_text == "Light Mode":
        # If the button text is "Light Mode":

        # Set theme to light mode.
        ctk.set_appearance_mode("light")

        # Set "forgot_password_label", "signup_label", and to "login_label" text color to blue.
        login_frame.forgot_password_label.configure(text_color="blue")
        login_frame.signup_label.configure(text_color= "blue")
        signup_frame.to_login_label.configure(text_color= "blue")

        # Set the theme menu text to "Dark Mode"
        theme_toggle_menu.configure(text = "Dark Mode")

    elif button_text == "Dark Mode":
        # If the button text is "Dark Mode":

        # Set theme to dark mode.
        ctk.set_appearance_mode("dark")

        # Set "forgot_password_label", "signup_label", and to "login_label" text color to cyan.
        login_frame.forgot_password_label.configure(text_color="cyan")
        login_frame.signup_label.configure(text_color= "cyan")
        signup_frame.to_login_label.configure(text_color= "cyan")

        # Set the theme menu text to "Light Mode"
        theme_toggle_menu.configure(text = "Light Mode")

# Create the window.
app = ctk.CTk()

# Customize the window application.
app.title("My First customtkinter App")
center_window(app, 400, 320)
app.resizable(False, False)

# Add menubar for File, Settings, About and Developer Option menus.
menubar = CTkMenuBar(app)

# Add a "File" menu with "File" and "Exit" options.
file_menu = menubar.add_cascade("File")
file_dropdown = CustomDropdownMenu(widget=file_menu)
file_dropdown.add_option("File")
file_dropdown.add_separator()
file_dropdown.add_option("Exit", command=confirm_exit)

# Add a "Settings" menu with "Reset form" option.
settings_menu = menubar.add_cascade("Settings")
settings_dropdown = CustomDropdownMenu(widget=settings_menu)
settings_dropdown.add_option("Reset Form", command=confirm_reset_form)

# Add "About" menu with "About Programmer" option.
about_menu = menubar.add_cascade("About")
about_dropdown = CustomDropdownMenu(widget= about_menu)
about_dropdown.add_option("About Programmer")

# Add a "Developer Option" menu with a "Messagebox" submenu containing "Info", "Question", and "Error" options.
developer_menu = menubar.add_cascade("Developer Option")
messagebox_dropdown = CustomDropdownMenu(widget=developer_menu)
messagebox_submenu = messagebox_dropdown.add_submenu("Messagebox")
messagebox_submenu.add_option("Info", command= lambda: CTkMessagebox(master= app, width= 100, height= 50, title="Info Testing", message="Message info test."))
messagebox_submenu.add_option("Question", command= lambda: CTkMessagebox(master=app, width= 100, height= 50, title="Question Testing", message="Yes or No or Cancel", icon= "question", option_1="Cancel", option_2="No", option_3="Yes"))
messagebox_submenu.add_option("Error", command= lambda: CTkMessagebox(master=app, width = 100, height= 50, title = "Error Testing", message="Error!", icon="cancel"))

#Add light and dark mode toggle menu button.
theme_toggle_menu = menubar.add_cascade("Light Mode", command= lambda: light_dark_mode(theme_toggle_menu.cget("text")))

# Add a state label to indicate which form the user currently viewing.
state_label = ctk.CTkLabel(app, text = "LOGIN FORM", font=("Arial", 20))
state_label.pack(pady = (3, 3))

# Initialize the signup frame.
signup_frame = SignupFrame(app, go_to_login)

# Initialize and display the login frame.
login_frame = LoginFrame(app, go_to_signup)
login_frame.pack(fill="both", expand=True)

# Initialize the tracking of current frame.
current_frame = login_frame

app.mainloop() # Keeps the GUI responsive.