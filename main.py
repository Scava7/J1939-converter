def stampa_can_id_29bit(hex_str):
    numero = int(hex_str, 16)
    can_id_29bit = numero & 0x1FFFFFFF
    binario = format(can_id_29bit, '029b')  # MSB (bit 28) è binario[0]

    def bin_to_int(bitstr):
        return int(bitstr, 2)

    def bits(start_bit, end_bit):
        """Estrae i bit da start_bit a end_bit inclusi, secondo la numerazione J1939 (bit 28 a 0)"""
        start_idx = 28 - start_bit
        end_idx = 28 - end_bit + 1
        return binario[start_idx:end_idx]
    
    Priority        = bits(28, 26)   #Priority
    Reserved        = bits(25, 25)   #Reserved
    DataPage        = bits(24, 24)   #Data Page
    PDU_Format      = bits(23, 16)   #Parameter Group Number (PDU Format)
    PDU_Specific    = bits(15, 8)    #Parameter Group Number (PDU Specific)
    Source_Address  = bits(7, 0)      #Source Address

    # Calcolo PGN
    PDU_Format_dec = bin_to_int(PDU_Format)
    PDU_Specific_dec = bin_to_int(PDU_Specific)

    print(PDU_Format_dec)
    print(PDU_Specific_dec)
    
    if PDU_Format_dec >= 0xF0:
        pgn = (PDU_Format_dec << 8) | PDU_Specific_dec
    else:
        pgn = (PDU_Format_dec << 8)

    print(f"Hex: {hex_str} -> CAN ID J1939 (29 bit): {binario}")
    print("Bit:    28    25  24  23    16   15     8   7     0")
    print("        |     |   |   |      |   |      |   |     |")
    print("Campo:  Pri   R   DP  PF------   PS------   SA-----")
    
    print("        " + "   ".join([
        Priority,
        Reserved,
        DataPage,
        PDU_Format,
        PDU_Specific,
        Source_Address,
    ]))

    print(f"\n -> PGN: {pgn} (decimale), {hex(pgn)} (esadecimale)")

        # Informazioni aggiuntive
    print(f" -> Tipo messaggio: {'PDU2 (broadcast)' if PDU_Format_dec >= 240 else 'PDU1 (destinato)'}")
    
    if PDU_Format_dec < 240:
        print(f" -> Indirizzo destinatario: {PDU_Specific_dec}")
    else:
        print(f" -> Messaggio broadcast (PS fa parte del PGN)")

    print(f" -> Priority: {bin_to_int(Priority)}")
    print(f" -> Indirizzo sorgente (SA): {bin_to_int(Source_Address)}")


# Esempio d'uso
stampa_can_id_29bit("0x18FD9400")
