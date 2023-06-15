import statistics
import statsmodels.api as sm
import pandas as pd
import tkinter as tk

# Load your data into a pandas DataFrame
data = pd.read_excel('RD.xlsx')
data = data.dropna()

x_options = data.columns


window = tk.Tk()

def run_regression():
    X = data[[choice for choice in x_options if vars_dict[choice].get() == 1]]
    Y = data[str(selected_choice.get())]
    X = sm.add_constant(X)
    print(Y)
    # Fit the OLS regression model
    model = sm.OLS(Y, X).fit()

    # Print the summary of the model results
    print(model.summary())
    text_widget.configure(state='normal')
    text_widget.delete("1.0", tk.END)
    # Insert the new text into the widget
    text_widget.insert(tk.END, model.summary())
    text_widget.configure(state='disabled')
# Set the window title and size
window.title("Regression tool kit")
window.geometry("1600x900")


vars_dict = {}
text_label = tk.Label(window, text="Choose independent variables:")
text_label.pack(side=tk.TOP)
# Create a function to print the selected choices


# Create a Checkbutton widget for each choice
top_button_frame = tk.Frame(window)
top_button_frame.pack(side=tk.TOP)
for choice in x_options:
    var = tk.IntVar()
    vars_dict[choice] = var
    checkbutton = tk.Checkbutton(top_button_frame, text=choice, variable=var)
    checkbutton.pack(side=tk.LEFT)
# Run the Tkinter event loop

selected_choice = tk.StringVar()

# Set the default value for the selection
selected_choice.set(x_options[0])

# Create a function to print the selected choice

text_label = tk.Label(window, text="Choose dependent variable:")
text_label.pack(side=tk.TOP)
sec_button_frame = tk.Frame(window)
sec_button_frame.pack(side=tk.TOP)
# Create a Radiobutton widget for each choice
for choice in x_options:
    radiobutton = tk.Radiobutton(sec_button_frame, text=choice, variable=selected_choice, value=choice)
    radiobutton.pack(side=tk.LEFT)

run_button = tk.Button(window, text="Run regression", command=run_regression)
run_button.pack(side=tk.TOP)

text_widget = tk.Text(window, height=10,state='disabled')
text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
window.mainloop()

