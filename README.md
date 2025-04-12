# 🎮 MakerQuest: Pico Edition - Reaction Game

A fast-paced reaction game built with the Raspberry Pi Pico, where two players compete to see who reacts quickest to a buzzer cue! This project is a fun way to explore physical computing with buttons, LEDs, buzzers, and RGB lights.

## 📦 Features

- Two-player reaction gameplay
- RGB LED feedback for the winner
- Buzzer countdown and trigger
- LED progress tracking per round
- Randomized buzzer timing to increase challenge

---

## 🛠️ Hardware Required

- Raspberry Pi Pico
- 2 x Push Buttons (Player 1 and Player 2)
- 1 x Buzzer
- 1 x RGB LED (Common Anode/Cathode supported by `picozero`)
- 6 x Standard LEDs for round indication
- Jumper wires and a breadboard

---

## ⚙️ Pin Configuration

| Component       | GPIO Pin |
| --------------- | -------- |
| Buzzer          | 15       |
| Button (P1)     | 16       |
| Button (P2)     | 17       |
| RGB LED - Red   | 18       |
| RGB LED - Green | 19       |
| RGB LED - Blue  | 20       |
| LED1            | 0        |
| LED2            | 1        |
| LED3            | 2        |
| LED4            | 3        |
| LED5            | 4        |
| LED6            | 5        |

---

## 🕹️ How to Play

1. The game consists of **5 rounds**.
2. Each round starts with a buzzer beeping 3 times to prepare players.
3. After a random delay (between 5-10 seconds), the buzzer will sound continuously.
4. Players must press their button **as quickly as possible** after the buzzer starts:
   - Player 1 (Green Team): GPIO 16
   - Player 2 (Yellow Team): GPIO 17
5. The RGB LED will flash the winner’s team color:
   - Green for Player 1
   - Yellow for Player 2
6. The winner’s score increases, and the next LED lights up to mark the round.
7. After 5 rounds, final scores are displayed in the console.

---

## 🧠 Code Overview

- `tour()`: Handles a single round, including buzzer timing, input detection, and scoring.
- Main loop: Repeats the game for a total of 5 rounds.
- Uses `picozero` for simplified hardware interaction.

---

## 🚀 Getting Started

1. Install [Thonny IDE](https://thonny.org/) and set up your Raspberry Pi Pico.
2. Install `picozero` library if not already available.
3. Connect components according to the pinout table above.
4. Upload the code to your Pico and run it via Thonny or directly from the Pico filesystem.
5. Let the reaction battles begin!

---

## 📸 Demo

> _(Add a GIF or YouTube link of the game in action if available!)_

---

## 🧩 Future Improvements

- Add a display for real-time score tracking
- Introduce a penalty for false starts
- Multiplayer or "best of N" game mode
- Customizable game length via button or menu

---

## 📄 License

This project is open-source and available under the MIT License. Feel free to remix, modify, or expand it!

---
