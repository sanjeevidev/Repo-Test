def print_chess_instructions():
    instructions = [
        "1. Each player starts with 16 pieces: 8 pawns, 2 rooks, 2 knights, 2 bishops, 1 queen, and 1 king",
        "2. White pieces always move first",
        "3. Players take turns moving one piece at a time",
        "4. Pieces cannot move through other pieces (except for knights)",
        "5. Kings can only move one square in any direction",
        "6. If a king is under attack (in check), the player must move to protect it",
        "7. Pawns can only move forward one square at a time (except for their first move)",
        "8. Pawns capture diagonally one square at a time",
        "9. A pawn reaching the opposite end of the board can be promoted to any piece except a king",
        "10. The game ends when one king is in checkmate (cannot escape capture)"
    ]
    
    for instruction in instructions:
        print(instruction)

# Call the function to display the instructions
print_chess_instructions()