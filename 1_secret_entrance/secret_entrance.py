import math


def read_file(filename: str) -> list[str]:
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def parse_instruction(instruction: str) -> tuple[str, int]:
    return (instruction[0], int(instruction[1:]))


def count_zero_cross(dial: int, instruction: tuple[str, int]) -> int:
    side, clicks = instruction
    zero_cross = math.floor(clicks / 100)
    if side == 'L' and dial < (clicks % 100) and dial != 0:
        zero_cross += 1
    if side == 'R' and (100 - dial) < (clicks % 100) and dial != 0:
        zero_cross += 1
    return zero_cross


def apply_instructions(instructions: tuple[str, int]) -> int:
    zero_count = 0
    dial = 50
    print(f"Staring with dial at - {50}")
    for side, clicks in instructions:
        prev_dial = dial
        zero_cross = count_zero_cross(dial, (side, clicks))
        if side == 'L':
            dial -= clicks

        elif side == 'R':
            dial += clicks

        dial = dial % 100
        print(f"Instruction {side} - {clicks} | Prev Dial: {prev_dial} |"
              f" New dial: {dial} | Crossed zero - {zero_cross} times")

        if dial == 0:
            print("#### Zero found!")
            zero_count += 1

        zero_count += zero_cross

    return zero_count


if __name__ == '__main__':
    file_input = read_file('secret_entrance.txt')
    print(f"Total instructions: {len(file_input)}")

    instructions = map(lambda x: parse_instruction(x), file_input)
    password = apply_instructions(instructions)
    print(f"Password: {password}")
