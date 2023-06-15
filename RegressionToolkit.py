import statistics
import statsmodels.api as sm
import pandas as pd
import tkinter as tk
import os

# Load your data into a pandas DataFrame



window = tk.Tk()
window.title("Regression tool kit")
window.geometry("1600x900")

def reload():
    path = "RegressionSorces"
    file_list = os.listdir(path)

    selected_excel = tk.StringVar()
    selected_excel.set(None)
    excel_frame = tk.Frame(window, name="excel")
    excel_frame.pack(side=tk.TOP)


    def choose_file():
        for child in window.winfo_children():
            if isinstance(child, tk.Frame) and child.winfo_name() != "excel":
                child.destroy()
        excel_name = selected_excel.get()
        excel_frame = tk.Frame(window)
        excel_frame.pack(side=tk.TOP)
        if excel_name != "None":
            data = pd.read_excel(f'RegressionSorces/{excel_name}')
            data = data.dropna()
            x_options = data.columns
            def run_regression():
                X = data[[choice for choice in x_options if vars_dict[choice].get() == 1]]
                Y = data[str(selected_choice.get())]
                X = sm.add_constant(X)
                model = sm.OLS(Y, X).fit()
                text_widget.configure(state='normal')
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, model.summary())
                text_widget.configure(state='disabled')
            vars_dict = {}
            text_label = tk.Label(excel_frame, text="Choose independent variables:")
            text_label.pack(side=tk.TOP)
            top_button_frame = tk.Frame(excel_frame)
            top_button_frame.pack(side=tk.TOP)
            for choice in x_options:
                var = tk.IntVar()
                vars_dict[choice] = var
                checkbutton = tk.Checkbutton(top_button_frame, text=choice, variable=var)
                checkbutton.pack(side=tk.LEFT)
            selected_choice = tk.StringVar()
            selected_choice.set(x_options[0])
            text_label = tk.Label(excel_frame, text="Choose dependent variable:")
            text_label.pack(side=tk.TOP)
            sec_button_frame = tk.Frame(excel_frame)
            sec_button_frame.pack(side=tk.TOP)
            for choice in x_options:
                radiobutton = tk.Radiobutton(sec_button_frame, text=choice, variable=selected_choice, value=choice)
                radiobutton.pack(side=tk.LEFT)
            run_button = tk.Button(excel_frame, text="Run regression", command=run_regression)
            run_button.pack(side=tk.TOP)
            text_widget = tk.Text(excel_frame, height=40,state='disabled')
            text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    for choice in file_list:
        radiobutton = tk.Radiobutton(excel_frame, text=choice, variable=selected_excel, value=choice, command=choose_file)
        radiobutton.pack(side=tk.LEFT)
    choose_file()    

reload_button = tk.Button(window, text="Reload", command=reload)
reload_button.pack(side=tk.TOP)


window.mainloop()