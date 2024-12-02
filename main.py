import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

# Car data with detailed information and image file paths
cars_data = {
    "BMW": {
        "Make": "BMW",
        "Models": ["3 Series", "5 Series", "7 Series", "X Series (SUVs)", "M Series (performance)"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["Inline", "V-type", "electric", "hybrid"],
        "Transmission": ["Manual", "automatic", "CVT"],
        "Color": "Various",
        "Image": "bmw.png"
    },
    "Mercedes-Benz": {
        "Make": "Mercedes-Benz",
        "Models": ["A-Class", "C-Class", "E-Class", "S-Class", "G-Class (SUVs)", "AMG (performance)"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["Inline", "V-type", "electric", "hybrid"],
        "Transmission": ["Manual", "automatic", "CVT"],
        "Color": "Various",
        "Image": "mercedes.png"
    },
    "Audi": {
        "Make": "Audi",
        "Models": ["A3", "A4", "A5", "A6", "Q5 (SUV)", "Q7 (SUV)", "RS (performance)"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["Inline", "V-type", "electric", "hybrid"],
        "Transmission": ["Automatic", "CVT"],
        "Color": "Various",
        "Image": "audi.png"
    },
    "Bentley": {
        "Make": "Bentley",
        "Models": ["Continental GT", "Flying Spur", "Bentayga (SUV)", "Mulsanne"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["V8", "W12"],
        "Transmission": ["Automatic"],
        "Color": "Various",
        "Image": "bentley.png"
    },
    "McLaren": {
        "Make": "McLaren",
        "Models": ["720S", "765LT", "GT", "Artura (hybrid)", "Senna", "Speedtail"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["V8", "V6 (hybrid)"],
        "Transmission": ["Automatic"],
        "Color": "Various",
        "Image": "mclaren.png"
    },
    "Ferrari": {
        "Make": "Ferrari",
        "Models": ["488", "812 Superfast", "Portofino", "Roma", "SF90 Stradale (hybrid)", "Purosangue (SUV)"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["V8", "V12", "hybrid"],
        "Transmission": ["Automatic"],
        "Color": "Various",
        "Image": "ferrari.png"
    },
    "Porsche": {
        "Make": "Porsche",
        "Models": ["911", "718", "Panamera", "Macan (SUV)", "Cayenne (SUV)", "Taycan (electric)"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["Flat-six", "V6", "V8", "electric"],
        "Transmission": ["Manual", "automatic", "PDK"],
        "Color": "Various",
        "Image": "porsche.png"
    },
    "Lamborghini": {
        "Make": "Lamborghini",
        "Models": ["Huracán", "Aventador", "Urus (SUV)", "Revuelto (hybrid)"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["V10", "V12", "hybrid"],
        "Transmission": ["Automatic"],
        "Color": "Various",
        "Image": "lamborghini.png"
    },
    "Rolls-Royce": {
        "Make": "Rolls-Royce",
        "Models": ["Phantom", "Ghost", "Wraith", "Dawn", "Cullinan (SUV)", "Spectre (electric)"],
        "Year": "Various (e.g., 2024 models)",
        "Engine Type": ["V12", "electric"],
        "Transmission": ["Automatic"],
        "Color": "Various",
        "Image": "rolls_royce.png"
    },
}

# Function to display car information
def display_car_info(car_name):
    """
    This function displays the car information and image when a user selects a car.
    Args:
    car_name (str): The name of the car selected by the user.
    """
    # Look for the car in the cars_data dictionary
    result = cars_data.get(car_name)
    
    if result:
        # Display the car information
        result_label.config(text=f"Make: {result['Make']}\n"
                                 f"Models: {', '.join(result['Models'])}\n"
                                 f"Year: {result['Year']}\n"
                                 f"Engine Type: {', '.join(result['Engine Type'])}\n"
                                 f"Transmission: {', '.join(result['Transmission'])}\n"
                                 f"Color: {result['Color']}")
        
        # Load and display the car image
        try:
            image = Image.open(result["Image"])
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            car_image_label.config(image=photo)
            car_image_label.image = photo  # Keep reference to avoid garbage collection
        except FileNotFoundError:
            car_image_label.config(image='', text="Image not available")
    else:
        result_label.config(text="Car not found.")
        car_image_label.config(image='', text="")  # Clear previous image or text

# Function to handle the search button click
def search_car():
    """
    This function searches for a car by its name, either manually or via the combobox.
    """
    search_term = entry_search.get().strip().lower()
    result = None

    # Case-insensitive search for the car in the dictionary
    for car in cars_data:
        if car.lower() == search_term:
            result = cars_data[car]
            break

    if result:
        display_car_info(result['Make'])  # Display the info using the Make name
    else:
        result_label.config(text="Car not found. Please try again.")
        car_image_label.config(image='', text="")

# Function to handle when a car is selected from the combo box
def on_car_selected(event):
    """
    This function is called when a car is selected from the combobox.
    It updates the display with the selected car's information.
    """
    selected_car = combo_suggestions.get()
    display_car_info(selected_car)

# Function to switch between frames
def show_frame(frame):
    """
    Switch between frames in the Tkinter GUI.
    Args:
    frame (tk.Frame): The frame to be displayed.
    """
    frame.tkraise()

# Function to sort the car names alphabetically
def sort_car_names():
    """
    Returns the list of car names sorted alphabetically.
    """
    return sorted(cars_data.keys())

# Create Tkinter window
root = tk.Tk()
root.title("Car Information App")
root.geometry("500x500")  # Increased window size

# Create frames (pages)
lobby_frame = tk.Frame(root)
search_frame = tk.Frame(root)

for frame in (lobby_frame, search_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# --- Lobby Frame (Welcome Page) ---
# Load and set the background image for the welcome page
welcome_background = Image.open("welcome background.png")  # Update with your background image file path
welcome_background = welcome_background.resize((500, 500), Image.Resampling.LANCZOS)
welcome_background_image = ImageTk.PhotoImage(welcome_background)

background_label = tk.Label(lobby_frame, image=welcome_background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the entire frame with the background

# Add welcome text with a custom style and smaller box
welcome_text = tk.Label(lobby_frame, text="Welcome", font=("Arial", 16, "bold"), fg="white", bg="black", padx=10, pady=5)
welcome_text.place(relx=0.5, rely=0.2, anchor="n")

# Open button at the bottom
btn_open = tk.Button(lobby_frame, text="Open", command=lambda: show_frame(search_frame), font=("Helvetica", 12), bg="white")
btn_open.place(relx=0.5, rely=0.9, anchor="s")

# --- Search Frame ---
# Label to guide the user for input
search_label = tk.Label(search_frame, text="Enter Car Name or Select from the List", font=("Arial", 12))
search_label.pack(pady=20)

# Entry widget for searching
entry_search = tk.Entry(search_frame, font=("Arial", 12))
entry_search.pack(pady=10)

# Button to search for a car
btn_search = tk.Button(search_frame, text="Search", command=search_car, font=("Arial", 12))
btn_search.pack(pady=10)

# Car selection combobox for quick access
combo_suggestions = ttk.Combobox(search_frame, values=sort_car_names(), state="readonly", font=("Arial", 12))
combo_suggestions.pack(pady=10)
combo_suggestions.bind("<<ComboboxSelected>>", on_car_selected)

# Car info display area
result_label = tk.Label(search_frame, text="Car information will be displayed here.", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Car image display
car_image_label = tk.Label(search_frame)
car_image_label.pack(pady=10)

# Go back to the welcome screen button
btn_back = tk.Button(search_frame, text="Back to Welcome", command=lambda: show_frame(lobby_frame), font=("Arial", 12))
btn_back.pack(side="bottom", pady=10)

# Show the lobby frame first
show_frame(lobby_frame)

# Run the Tkinter event loop
root.mainloop()
