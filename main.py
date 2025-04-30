import tkinter as tk
from tkinter import ttk

def pgn_to_canid():
    try:
        pgn_input = entry_pgn.get().strip()
        base = 16 if pgn_input_base.get() == 'hex' else 10
        pgn = int(pgn_input, base)

        if pgn < 0 or pgn > 0xFFFF:
            output_var.set("PGN fuori range valido (0–65535)")
            return

        priority = 3
        source_address = 0

        pf = (pgn >> 8) & 0xFF
        ps = pgn & 0xFF

        if pf < 240:
            output_var.set("Il PGN fornito non è broadcast (PF < 240)")
            return

        can_id = (priority << 26) | (pf << 16) | (ps << 8) | source_address
        output_var.set(f"CAN ID = {hex(can_id)} ({can_id})")
    except ValueError:
        output_var.set("Input PGN non valido")

def canid_to_pgn():
    try:
        canid_input = entry_canid.get().strip()
        base = 16 if canid_input_base.get() == 'hex' else 10
        canid = int(canid_input, base)

        pf = (canid >> 16) & 0xFF
        ps = (canid >> 8) & 0xFF

        if pf >= 240:
            pgn = (pf << 8) | ps
        else:
            pgn = pf << 8

        output_var.set(f"PGN = {hex(pgn)} ({pgn})")
    except ValueError:
        output_var.set("Input CAN ID non valido")

# Interfaccia grafica
root = tk.Tk()
root.title("Convertitore PGN ⇄ CAN ID")

# Selettori esadecimale/decimale
pgn_input_base = tk.StringVar(value='hex')
canid_input_base = tk.StringVar(value='hex')

# PGN input
ttk.Label(root, text="PGN:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_pgn = ttk.Entry(root)
entry_pgn.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(root, text="→ CAN ID", command=pgn_to_canid).grid(row=0, column=2, padx=5)

ttk.Radiobutton(root, text="Hex", variable=pgn_input_base, value='hex').grid(row=0, column=3)
ttk.Radiobutton(root, text="Dec", variable=pgn_input_base, value='dec').grid(row=0, column=4)

# CAN ID input
ttk.Label(root, text="CAN ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_canid = ttk.Entry(root)
entry_canid.grid(row=1, column=1, padx=5, pady=5)
ttk.Button(root, text="→ PGN", command=canid_to_pgn).grid(row=1, column=2, padx=5)

ttk.Radiobutton(root, text="Hex", variable=canid_input_base, value='hex').grid(row=1, column=3)
ttk.Radiobutton(root, text="Dec", variable=canid_input_base, value='dec').grid(row=1, column=4)

# Output
output_var = tk.StringVar()
ttk.Label(root, textvariable=output_var, foreground="blue").grid(row=2, column=0, columnspan=5, pady=10)

root.mainloop()
