import mido
from pynput.keyboard import Key, Controller

print("Starting MIDI to Keyboard Mapper...\n")
print("Please select a MIDI input device")

# List available MIDI input devices
midi_input = mido.get_input_names()
for i, device in enumerate(midi_input):
    print(f"{i}: {device}")

# Get user input for MIDI device selection
while True:
    try:
        device_index = int(input("\nEnter the number of the MIDI device you want to use: "))
        if 0 <= device_index < len(midi_input): # Check if the input is within the valid range
            midi_device = midi_input[device_index]
            print(f"\nSelected MIDI device: {midi_device}")
            break
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Open the selected MIDI input port
midi_port = mido.open_input(midi_device)
keyboard = Controller()
print(f"\nListening for MIDI messages on {midi_device}...\n")