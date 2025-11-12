import tkinter as tk
import random
import string
import pygame

pygame.mixer.init()


def get_char_weight(char):
    if char in string.digits:
        return int(char)
    else:
        return ord(char) - ord('A') + 1


# Calculate average weight of a block
def calculate_avg_weight(block):
    weight_sum = sum(get_char_weight(c) for c in block)
    return weight_sum / len(block)


# Generate block
def generate_block(length,target_avg_min,target_avg_max):
    max_attempts = 1000 # To avoid the loop
    for _ in range(max_attempts):
        # Randomly generate character block
        chars = []
        for _ in range(length):
            if random.choice([True, False]):
                chars.append(random.choice(string.ascii_uppercase))
            else:
                chars.append(random.choice(string.digits))
        block = ''.join(chars)
        avg_weight = calculate_avg_weight(block)

        # If average is in range
        if target_avg_min <= avg_weight <= target_avg_max:
            return block

        # If not,randomly select one position and replace
        if avg_weight < target_avg_min:
            # Low average,randomly select one position and replace digit with letter
            pos = random.randint(0, len(block) - 1)
            if block[pos] in string.digits:
                chars = list(block)
                chars[pos] = random.choice(string.ascii_uppercase)
                block = ''.join(chars)
        else:
            # High average,randomly select one position and replace letter with digit
            pos = random.randint(0, len(block) - 1)
            if block[pos] in string.ascii_uppercase:
                chars = list(block)
                chars[pos] = random.choice(string.digits)
                block = ''.join(chars)
        avg_weight = calculate_avg_weight(block)
        if target_avg_min <= avg_weight <= target_avg_max:
            return block
    # If still unsuccessfully,return the closest value
    return


# Key generation
def generate_key():
    target_avg_min = 10
    target_avg_max = 15

    # Generate three blocks
    block1 = generate_block(5,target_avg_min,target_avg_max)
    block2 = generate_block(4,target_avg_min,target_avg_max)
    block3 = generate_block(4,target_avg_min,target_avg_max)

    key = f"{block1}-{block2}-{block3}"

    key_label.config(text=key)


# Main window
root = tk.Tk()
root.title("Welcome to FCB")
root.geometry("1080x1080")

bg_photo = tk.PhotoImage(file="window.png")
canvas = tk.Canvas(root, width=1080, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")


button = tk.Button(root, text="Please click here <3", command=generate_key, bg="GhostWhite")
canvas.create_window((540, 250), window=button)

key_label = tk.Label(root, font=("Arial", 30), bg="Azure")
canvas.create_window((540, 350), window=key_label)


# Animation
def animate_button_breath():
    if not hasattr(animate_button_breath, 'growing'):
        animate_button_breath.growing = True
        animate_button_breath.size = 14  # Initial font

    if animate_button_breath.growing:
        animate_button_breath.size += 1
        if animate_button_breath.size >= 18:  # The largest size
            animate_button_breath.growing = False
    else:
        animate_button_breath.size -= 1
        if animate_button_breath.size <= 14:  # The smallest size
            animate_button_breath.growing = True

    button.config(font=("Arial", animate_button_breath.size, "bold"))

    root.after(100, animate_button_breath)

animate_button_breath()


# Color
def animate_text():
    colors = ["HotPink", "RoyalBlue", "Lime", "DarkViolet", "Moccasin", "Turquoise", "Coral"]
    key_label.config(fg=random.choice(colors))
    root.after(400, animate_text)

animate_text()

# Music
def play_background_music():
    pygame.mixer.music.load("8bit_music.wav")
    pygame.mixer.music.play()

play_background_music()


root.mainloop()