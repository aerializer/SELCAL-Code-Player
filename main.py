from pydub import AudioSegment
from pydub.generators import Sine
import subprocess
import platform
import os
import time

selcal_freq_map = {
    'A': 312.6, 'B': 346.7, 'C': 384.6, 'D': 426.6, 'E': 473.2,
    'F': 524.8, 'G': 582.1, 'H': 645.7, 'J': 716.1, 'K': 794.3,
    'L': 881, 'M': 977.2, 'P': 1083.9, 'Q': 1202.3, 'R': 1333.5,
    'S': 1479.1, 'T': 329.2, 'U': 365.2, 'V': 405, 'W': 449.3,
    'X': 498.3, 'Y': 552.7, 'Z': 613.1, '1': 680, '2': 754.2,
    '3': 836.6, '4': 927.9, '5': 1029.2, '6': 1141.6, '7': 1266.2,
    '8': 1404.4, '9': 1557.8
}

def play_dual_frequencies(freq1, freq2, duration=1000, filename="temp"):
    sound1 = Sine(freq1).to_audio_segment(duration=duration)
    sound2 = Sine(freq2).to_audio_segment(duration=duration)
    combined_sound = sound1.overlay(sound2)
    temp_file = f"temp_combined_{filename}.wav"
    try:
        combined_sound.export(temp_file, format="wav")
        if platform.system() == "Windows":
            subprocess.run(["powershell", "-Command", f"(New-Object Media.SoundPlayer '{temp_file}').PlaySync()"], 
                          check=True, shell=True)
        elif platform.system() == "Darwin":
            subprocess.run(["afplay", temp_file], check=True)
        else:
            subprocess.run(["aplay", temp_file], check=True)
    except Exception as e:
        print(f"Playback error: {e}")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def play_selcal_code(selcal_str):
    clean_code = selcal_str.replace('-','').replace(' ','').upper()
    if len(clean_code) != 4:
        raise ValueError("Invalid format! Please enter 4 valid SELCAL characters (supports: ABCD, AB-CD, AB CD)")
    
    def get_freq(char):
        if char not in selcal_freq_map:
            raise ValueError(f"Invalid SELCAL character: {char}, please check your input")
        return selcal_freq_map[char]
    
    freq1_1 = get_freq(clean_code[0])
    freq1_2 = get_freq(clean_code[1])
    freq2_1 = get_freq(clean_code[2])
    freq2_2 = get_freq(clean_code[3])
    
    play_dual_frequencies(freq1_1, freq1_2)
    time.sleep(0.2)
    play_dual_frequencies(freq2_1, freq2_2)

def main():
    print("="*74)
    print("SELCAL Code Audio Player | Format: AB-CD / AB CD / ABCD | Case Insensitive")
    print("="*74)
    while True:
        selcal_input = input("\nEnter SELCAL code (enter Q to exit): ").strip()
        
        if selcal_input.lower() == 'q':
            print("Thanks for using, program exited!")
            break
        
        if not selcal_input:
            print("Input cannot be empty, please re-enter!")
            continue
        
        try:
            play_selcal_code(selcal_input)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()