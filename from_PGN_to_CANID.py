def calcola_can_id(pgn_dec, source_address, priority=6):
    pf = (pgn_dec >> 8) & 0xFF
    ps = pgn_dec & 0xFF
    can_id = (priority << 26) | (0 << 24) | (pf << 16) | (ps << 8) | source_address
    return can_id

def calcola_can_id_da_lista(pgn_input, source_address, priority=6):
    pgn_list = [p.strip() for p in pgn_input.split(',')]
    
    for pgn_str in pgn_list:
        if not pgn_str.isdigit():
            print(f"[!] Errore: '{pgn_str}' non è un numero decimale valido.")
            continue
        pgn = int(pgn_str)
        if not (0 <= pgn <= 0xFFFF):
            print(f"[!] Errore: PGN {pgn} fuori dal range 0–65535")
            continue

        can_id = calcola_can_id(pgn, source_address, priority)
        print(f"PGN: {pgn:<6} -> CAN ID: {format(can_id, '08X')}")

# Esempio d'uso
input_pgns = "64948, 64923, 65110"
source_address = 0
calcola_can_id_da_lista(input_pgns, source_address)
