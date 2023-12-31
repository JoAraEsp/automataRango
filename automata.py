import tkinter as tk

def delta(current_state, char):
    transitions = {
    ("q0", '1'): "q1", ("q0", '2'): "q2", ("q0", '3'): "q2", ("q0", '4'): "q2",
    ("q0", '5'): "q2", ("q0", '6'): "q2", ("q0", '7'): "q2", ("q0", '8'): "q3",
    
    ("q1", '-'): "q4",

    ("q4", 'N'): "q5", ("q4", 'O'): "q5", ("q4", 'P'): "q5", ("q4", 'Q'): "q5",
    ("q4", 'R'): "q5", ("q4", 'S'): "q5", ("q4", 'T'): "q5", ("q4", 'U'): "q5",
    ("q4", 'V'): "q5", ("q4", 'W'): "q5", ("q4", 'X'): "q5", ("q4", 'Y'): "q5",
    ("q4", 'Z'): "q5",
    
    ("q5", 'G'): "q6", ("q5", 'H'): "q6", ("q5", 'I'): "q6", ("q5", 'J'): "q6",
    ("q5", 'K'): "q6", ("q5", 'L'): "q6", ("q5", 'M'): "q6", ("q5", 'N'): "q6",
    ("q5", 'O'): "q6", ("q5", 'P'): "q6", ("q5", 'Q'): "q6", ("q5", 'R'): "q6",
    ("q5", 'S'): "q6", ("q5", 'T'): "q6", ("q5", 'U'): "q6", ("q5", 'V'): "q6",
    ("q5", 'W'): "q6", ("q5", 'X'): "q6", ("q5", 'Y'): "q6", ("q5", 'Z'): "q6",

    ("q6", '-'): "q7",
    
    ("q7", '0'): "q8", ("q7", '1'): "q8", ("q7", '2'): "q8", ("q7", '3'): "q8",
    ("q7", '4'): "q8", ("q7", '5'): "q8", ("q7", '6'): "q8", ("q7", '7'): "q8",
    ("q7", '8'): "q8", ("q7", '9'): "q8",
    
    ("q8", '1'): "q9", ("q8", '2'): "q9", ("q8", '3'): "q9", ("q8", '4'): "q9",
    ("q8", '5'): "q9", ("q8", '6'): "q9", ("q8", '7'): "q9", ("q8", '8'): "q9",
    ("q8", '9'): "q9",

    ("q9", 'B'): "q10", ("q9", 'C'): "q10", ("q9", 'D'): "q10", ("q9", 'E'): "q10",
    ("q9", 'F'): "q10", ("q9", 'G'): "q10", ("q9", 'H'): "q10", ("q9", 'I'): "q10",
    ("q9", 'J'): "q10", ("q9", 'K'): "q10", ("q9", 'L'): "q10", ("q9", 'M'): "q10",
    ("q9", 'N'): "q10", ("q9", 'O'): "q10", ("q9", 'P'): "q10", ("q9", 'Q'): "q10",
    ("q9", 'R'): "q10", ("q9", 'S'): "q10", ("q9", 'T'): "q10", ("q9", 'U'): "q10",
    ("q9", 'V'): "q10", ("q9", 'W'): "q10", ("q9", 'X'): "q10", ("q9", 'Y'): "q10",
    ("q9", 'Z'): "q10",
    
    ("q2", '-'): "q11",
    
    ("q11", 'A'): "q12", ("q11", 'B'): "q12", ("q11", 'C'): "q12", ("q11", 'D'): "q12",
    ("q11", 'E'): "q12", ("q11", 'F'): "q12", ("q11", 'G'): "q12", ("q11", 'H'): "q12",
    ("q11", 'I'): "q12", ("q11", 'J'): "q12", ("q11", 'K'): "q12", ("q11", 'L'): "q12",
    ("q11", 'M'): "q12", ("q11", 'N'): "q12", ("q11", 'O'): "q12", ("q11", 'P'): "q12",
    ("q11", 'Q'): "q12", ("q11", 'R'): "q12", ("q11", 'S'): "q12", ("q11", 'T'): "q12",
    ("q11", 'U'): "q12", ("q11", 'V'): "q12", ("q11", 'W'): "q12", ("q11", 'X'): "q12",
    ("q11", 'Y'): "q12", ("q11", 'Z'): "q12",

    ("q12", 'A'): "q13", ("q12", 'B'): "q13", ("q12", 'C'): "q13", ("q12", 'D'): "q13",
    ("q12", 'E'): "q13", ("q12", 'F'): "q13", ("q12", 'G'): "q13", ("q12", 'H'): "q13",
    ("q12", 'I'): "q13", ("q12", 'J'): "q13", ("q12", 'K'): "q13", ("q12", 'L'): "q13",
    ("q12", 'M'): "q13", ("q12", 'N'): "q13", ("q12", 'O'): "q13", ("q12", 'P'): "q13",
    ("q12", 'Q'): "q13", ("q12", 'R'): "q13", ("q12", 'S'): "q13", ("q12", 'T'): "q13",
    ("q12", 'U'): "q13", ("q12", 'V'): "q13", ("q12", 'W'): "q13", ("q12", 'X'): "q13",
    ("q12", 'Y'): "q13", ("q12", 'Z'): "q13",

    ("q13", '-'): "q14",

    ("q14", '0'): "q15", ("q14", '1'): "q15", ("q14", '2'): "q15", ("q14", '3'): "q15",
    ("q14", '4'): "q15", ("q14", '5'): "q15", ("q14", '6'): "q15", ("q14", '7'): "q15",
    ("q14", '8'): "q15", ("q14", '9'): "q15",

    ("q15", '0'): "q16", ("q15", '1'): "q16", ("q15", '2'): "q16", ("q15", '3'): "q16",
    ("q15", '4'): "q16", ("q15", '5'): "q16", ("q15", '6'): "q16", ("q15", '7'): "q16",
    ("q15", '8'): "q16", ("q15", '9'): "q16",

    ("q16", 'A'): "q17", ("q16", 'B'): "q17", ("q16", 'C'): "q17", ("q16", 'D'): "q17",
    ("q16", 'E'): "q17", ("q16", 'F'): "q17", ("q16", 'G'): "q17", ("q16", 'H'): "q17",
    ("q16", 'I'): "q17", ("q16", 'J'): "q17", ("q16", 'K'): "q17", ("q16", 'L'): "q17",
    ("q16", 'M'): "q17", ("q16", 'N'): "q17", ("q16", 'O'): "q17", ("q16", 'P'): "q17",
    ("q16", 'Q'): "q17", ("q16", 'R'): "q17", ("q16", 'S'): "q17", ("q16", 'T'): "q17",
    ("q16", 'U'): "q17", ("q16", 'V'): "q17", ("q16", 'W'): "q17", ("q16", 'X'): "q17",
    ("q16", 'Y'): "q17", ("q16", 'Z'): "q17",

    ("q3", '-'): "q18",
    
    ("q18", 'A'): "q19", ("q18", 'B'): "q19", ("q18", 'C'): "q19", ("q18", 'D'): "q19",
    ("q18", 'E'): "q19", ("q18", 'F'): "q19", ("q18", 'G'): "q19", ("q18", 'H'): "q19",
    ("q18", 'I'): "q19", ("q18", 'J'): "q19", ("q18", 'K'): "q19", ("q18", 'L'): "q19",
    ("q18", 'M'): "q19", ("q18", 'N'): "q19",

    ("q19", 'A'): "q20", ("q19", 'B'): "q20", ("q19", 'C'): "q20", ("q19", 'D'): "q20",
    ("q19", 'E'): "q20", ("q19", 'F'): "q20", ("q19", 'G'): "q20", ("q19", 'H'): "q20",
    ("q19", 'I'): "q20", ("q19", 'J'): "q20", ("q19", 'K'): "q20", ("q19", 'L'): "q20",
    ("q19", 'M'): "q20", ("q19", 'N'): "q20", ("q19", 'O'): "q20", ("q19", 'P'): "q20",
    ("q19", 'Q'): "q20", ("q19", 'R'): "q20",
    
    ("q20", '-'): "q21",
    
    ("q21", '0'): "q22", ("q21", '1'): "q22", ("q21", '2'): "q22", ("q21", '3'): "q22",
    ("q21", '4'): "q22", ("q21", '5'): "q22", ("q21", '6'): "q22", ("q21", '7'): "q22",
    ("q21", '8'): "q22", ("q21", '9'): "q22",
    
    ("q22", '0'): "q23", ("q22", '1'): "q23", ("q22", '2'): "q23", ("q22", '3'): "q23",
    ("q22", '4'): "q23", ("q22", '5'): "q23", ("q22", '6'): "q23", ("q22", '7'): "q23",
    ("q22", '8'): "q23", ("q22", '9'): "q23",

    ("q23", 'A'): "q24", ("q23", 'B'): "q24", ("q23", 'C'): "q24", ("q23", 'D'): "q24",
    ("q23", 'E'): "q24", ("q23", 'F'): "q24", ("q23", 'G'): "q24", ("q23", 'H'): "q24",
    ("q23", 'I'): "q24", ("q23", 'J'): "q24"
}

    return transitions.get((current_state, char.upper()))  

def validate_string(s):
    current_state = "q0"
    states_sequence = [current_state]
    
    for char in s:
        current_state = delta(current_state, char)
        if current_state is None:
            return False, states_sequence
        states_sequence.append(current_state)
    
    return current_state in ["q10", "q17", "q24"], states_sequence

def on_validate():
    s = entry.get()
    valid, states_sequence = validate_string(s)
    
    if valid:
        result_var.set("Placa válida")
    else:
        result_var.set("Placa inválida")
    
    states_sequence_var.set(" -> ".join(states_sequence))

root = tk.Tk()
root.title("Validador de Placas")

instruction_label = tk.Label(root, text="Por favor, ingrese una placa vehicular en la forma X-XX-XXX")
instruction_label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

validate_button = tk.Button(root, text="Validar", command=on_validate)
validate_button.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14))
result_label.pack(pady=10)

states_sequence_var = tk.StringVar()
states_sequence_label = tk.Label(root, textvariable=states_sequence_var, font=("Arial", 10))
states_sequence_label.pack(pady=10)

root.mainloop()
