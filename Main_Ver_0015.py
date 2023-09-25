import tkinter as tk
from tkinter import ttk
from tkinter import filedialog  # Import filedialog for file selection
from tkinter import messagebox  # Import messagebox for displaying messages
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk  # Import Pillow for image handling

# Declare global variables for selected start and end time
start_year_var = None
start_month_var = None
start_day_var = None
start_hour_var = None
start_minute_var = None
start_second_var = None

end_year_var = None
end_month_var = None
end_day_var = None
end_hour_var = None
end_minute_var = None
end_second_var = None

# Function to handle button click
def on_button_click():
    selected_file = file_var.get()
    query_option = query_var.get()
    get_data_option = get_data_var.get()
    visualization_option = visualization_var.get()

    # Implement functionality based on the selected options
    print(f"File Option: {selected_file}")
    print(f"Query Option: {query_option}")
    print(f"Get Data Option: {get_data_option}")
    print(f"Visualization Option: {visualization_option}")

# Function to automatically open a file selection dialog when an option is selected
def select_file(event):
    selected_file = file_var.get()
    file_type = ""
    if selected_file == "Load SAC file":
        file_type = [("SAC files", "*.sac")]
    elif selected_file == "Load mseed File":
        file_type = [("MSeed files", "*.mseed")]
    elif selected_file == "Load SESAME file":
        file_type = [("SESAME files", "*.sesame")]

    file_path = filedialog.askopenfilename(filetypes=file_type)
    if file_path:
        selected_file_label.config(text=f"Selected File: {file_path}")
        # Show a message box indicating the file was selected
        messagebox.showinfo("File Selected", f"The selected file is: {file_path}")

# Function to handle the "Start/End time" option in the second dropdown
def select_start_end_time():
    global start_year_var, start_month_var, start_day_var, start_hour_var, start_minute_var, start_second_var
    global end_year_var, end_month_var, end_day_var, end_hour_var, end_minute_var, end_second_var

    start_end_window = tk.Toplevel(root)
    start_end_window.title("Select Start/End Time")

    # Create labels and entry fields for date and time selection
    start_label = ttk.Label(start_end_window, text="Start Time:")
    start_label.grid(row=0, column=0, padx=5, pady=5)

    end_label = ttk.Label(start_end_window, text="End Time:")
    end_label.grid(row=1, column=0, padx=5, pady=5)

    # Define variables to store the selected date and time
    start_year_var = tk.StringVar(value="2023")
    start_month_var = tk.StringVar(value="1")
    start_day_var = tk.StringVar(value="1")
    start_hour_var = tk.StringVar(value="00")
    start_minute_var = tk.StringVar(value="00")
    start_second_var = tk.StringVar(value="00")

    end_year_var = tk.StringVar(value="2023")
    end_month_var = tk.StringVar(value="1")
    end_day_var = tk.StringVar(value="1")
    end_hour_var = tk.StringVar(value="00")
    end_minute_var = tk.StringVar(value="00")
    end_second_var = tk.StringVar(value="00")

    # Create dropdowns for date and time selection
    date_labels = ["Year", "Month", "Day", "Hour", "Minute", "Second"]
    start_vars = [start_year_var, start_month_var, start_day_var, start_hour_var, start_minute_var, start_second_var]
    end_vars = [end_year_var, end_month_var, end_day_var, end_hour_var, end_minute_var, end_second_var]

    for i, label in enumerate(date_labels):
        ttk.Label(start_end_window, text=label).grid(row=0, column=i * 2, padx=5, pady=5)
        ttk.Label(start_end_window, text=label).grid(row=1, column=i * 2, padx=5, pady=5)
        if label == "Year":
            values = list(range(2000, 2031))
        elif label == "Month":
            values = list(range(1, 13))
        elif label == "Day":
            values = list(range(1, 32))
        elif label in ["Hour", "Minute", "Second"]:
            values = ["{:02d}".format(i) for i in range(60)]  # Add leading zeros
        ttk.Combobox(start_end_window, textvariable=start_vars[i], values=values).grid(row=0, column=i * 2 + 1, padx=5, pady=5)
        ttk.Combobox(start_end_window, textvariable=end_vars[i], values=values).grid(row=1, column=i * 2 + 1, padx=5, pady=5)

    # Create a "Proceed" button to confirm the selection
    proceed_button = ttk.Button(start_end_window, text="Proceed", command=lambda: on_proceed_click(start_end_window))
    proceed_button.grid(row=2, column=0, columnspan=12, padx=5, pady=10)

# Function to handle the "Proceed" button click in the date and time selection window
def on_proceed_click(window):
    global start_year_var, start_month_var, start_day_var, start_hour_var, start_minute_var, start_second_var
    global end_year_var, end_month_var, end_day_var, end_hour_var, end_minute_var, end_second_var

    start_time = f"{start_year_var.get()}-{start_month_var.get()}-{start_day_var.get()} " \
                 f"{start_hour_var.get()}:{start_minute_var.get()}:{start_second_var.get()}"
    end_time = f"{end_year_var.get()}-{end_month_var.get()}-{end_day_var.get()} " \
               f"{end_hour_var.get()}:{end_minute_var.get()}:{end_second_var.get()}"

    selected_file_label.config(text=f"Start Time: {start_time}, End Time: {end_time}")
    messagebox.showinfo("Start/End Time Selected", f"Start Time and End Time selected: {start_time} - {end_time}")
    window.destroy()  # Close the date and time selection window

# Create the main window
root = tk.Tk()
root.title("HSV by HyXiao")

# Create a themed style
style = ThemedStyle(root)
style.set_theme("plastik")  # You can change the theme as per your preference

# Create a frame to hold the dropdowns and image
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Load and resize the logo image
logo_image = Image.open("./img/HVSR_GUI.jpeg")  # Assuming HVSR_GUI.jpeg is a 500x500 JPEG image
# Resize the image to fit within a 500x500 pixel area
logo_image.thumbnail((500, 500), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(frame, image=logo_photo)
logo_label.grid(row=0, column=0, columnspan=4)

# Create and configure the dropdowns
file_label = ttk.Label(frame, text="File:")
file_label.grid(row=1, column=0, padx=5, pady=5)
file_var = tk.StringVar()
file_dropdown = ttk.Combobox(frame, textvariable=file_var, values=["Load SAC file", "Load mseed File", "Load SESAME file"])
file_dropdown.grid(row=1, column=1, padx=5, pady=5)
file_dropdown.bind("<<ComboboxSelected>>", select_file)  # Bind the select_file function to the selection event

# Label to display the selected file
selected_file_label = ttk.Label(frame, text="Selected File: None")
selected_file_label.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

# Create and configure the other dropdowns
query_label = ttk.Label(frame, text="Query options:")
query_label.grid(row=2, column=0, padx=5, pady=5)
query_var = tk.StringVar()
query_dropdown = ttk.Combobox(frame, textvariable=query_var, values=["Start/End time", "Stations options", "Event options", "Distance options"])
query_dropdown.grid(row=2, column=1, padx=5, pady=5)
query_dropdown.bind("<<ComboboxSelected>>", lambda event: select_start_end_time())  # Bind the select_start_end_time function to the selection event

get_data_label = ttk.Label(frame, text="Get data:")
get_data_label.grid(row=3, column=0, padx=5, pady=5)
get_data_var = tk.StringVar()
get_data_dropdown = ttk.Combobox(frame, textvariable=get_data_var, values=["SAVE to xml", "SAVE to csv", "SAVE to txt"])
get_data_dropdown.grid(row=3, column=1, padx=5, pady=5)

visualization_label = ttk.Label(frame, text="Visualization:")
visualization_label.grid(row=4, column=0, padx=5, pady=5)
visualization_var = tk.StringVar()
visualization_dropdown = ttk.Combobox(frame, textvariable=visualization_var, values=["Show data", "Show HVSR", "Show processes output"])
visualization_dropdown.grid(row=4, column=1, padx=5, pady=5)

# Create a button with the text "Calculate HVSR"
button = ttk.Button(root, text="Calculate HVSR", command=on_button_click, style='AccentButton.TButton')
button.pack(padx=20, pady=10)

# Start the GUI main loop
root.mainloop()

