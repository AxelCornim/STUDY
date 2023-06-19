import tkinter as tk

def on_checkbox_click(checkbox):
    if checkbox.get() == 0:
        checkbox.set(1)
    else:
        checkbox.set(0)

def create_checklist_window():
    # Cria a janela principal
    window = tk.Tk()
    window.title('Checklist Diária')

    # Cria a tabela
    table = []
    
    # Título
    title_row = ['Título', 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5']
    table.append(title_row)
    
    # Dias da semana e horários
    weekdays = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    for i, day in enumerate(weekdays):
        row = [day]
        for j in range(5):
            checkbox = tk.IntVar()
            checkbox.set(0)
            checkbox_widget = tk.Checkbutton(window, variable=checkbox, command=lambda checkbox=checkbox: on_checkbox_click(checkbox))
            checkbox_widget.grid(row=i+1, column=j+1)
            row.append(checkbox)
        table.append(row)
    
    # Exibe a tabela
    for i, row in enumerate(table):
        for j, cell in enumerate(row):
            label = tk.Label(window, text=str(cell))
            label.grid(row=i, column=j)

    # Inicia o loop do tkinter
    window.mainloop()

if __name__ == '__main__':
    create_checklist_window()
