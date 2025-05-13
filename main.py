import mido
import time
from pynput.keyboard import Key, Controller

print("Starting MIDI to Keyboard Mapper...\n")

# List available MIDI input devices
midi_input = mido.get_input_names()
if not midi_input:
    print("No MIDI input devices found!")
    print("Please connect a MIDI device and try again!")
    exit()
for i, device in enumerate(midi_input):
    print(f"{i}: {device}")

# Get user input for MIDI device selection
while True:
    try:
        device_index = int(input("\nEnter the number of the MIDI device you want to use: "))
        if 0 <= device_index < len(midi_input): # Check if the input is within the valid range
            midi_device = midi_input[device_index]
            break
        else:
            print("Invalid selection. Please try again.")
    except ValueError: # If the input is not a number
        print("Invalid input. Please enter a number.")

# Open the selected MIDI input port
midi_port = mido.open_input(midi_device)
keyboard = Controller()

print(f"\nListening for MIDI messages on {midi_device}...\n")
print("Please press the MIDI button you want to use as the UP ARROW!")
with midi_port:
    for msg1 in midi_port:
        if 'note_on' in str(msg1):
            up = msg1
            print(f"UP ARROW MIDI message: {up}")
        break
time.sleep(0.5) # Give some time before asking for the next button
midi_port.close()
midi_port = mido.open_input(midi_device)

print("\nPlease press the MIDI button you want to use as the DOWN ARROW!")
with midi_port:
    for msg2 in midi_port:
        if 'note_on' in str(msg2):
            down = msg2
            print(f"DOWN ARROW MIDI message: {down}")
        break
time.sleep(0.5)
midi_port.close()
midi_port = mido.open_input(midi_device)

print("\nSuccessfully mapped MIDI buttons to keyboard arrows!")
print("Now you can use your MIDI device to control the UP and DOWN arrows on your keyboard!\n")

with midi_port:
    for msg in midi_port:
        if msg == up:
            print("UP ARROW pressed")
            keyboard.press(Key.up)
        elif msg == down:
            print("DOWN ARROW pressed")
            keyboard.press(Key.down)