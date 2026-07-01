# Project 1: Rule-Based AI Chatbot 🤖

**DecodeLabs Industrial Training Kit | Batch 2026**

---

## 📌 Overview

A rule-based chatbot that responds to predefined user inputs using **Control Flow and Logic** — no machine learning involved. This is the foundation phase of the AI Engineering internship track, focused on mastering programmatic decision-making before moving to supervised learning.

The chatbot simulates basic human interaction through a continuous digital loop powered by pure if-else logic and dictionary-based intent matching.

---

## 🎯 Goal

Create a simple rule-based chatbot that responds to predefined user inputs.

---

## ✅ Key Requirements Met

| Requirement | Implementation |
|---|---|
| Handle greetings and exit commands | `hello`, `hi`, `bye`, `exit`, `quit` all handled |
| Use if-else logic for responses | Dictionary `.get()` lookup (professional approach) |
| Run in a continuous loop | `while True` loop with `break` on exit command |

---

## ⚙️ How It Works (IPO Model)

**INPUT** → Raw user text captured via `input()`

**PROCESS** → Sanitization: `.lower().strip()` normalizes casing and whitespace → Dictionary `.get()` matches intent and returns response

**OUTPUT** → Bot prints the matched response, or a fallback if unrecognized

---

## 🧠 Key Design Decisions

- **Dictionary over if-elif ladder** — dictionary lookup is O(1) constant time vs O(n) linear scan. The if-elif "anti-pattern" was explicitly warned against in the brief.
- **Sanitization first** — `HELLO`, `hello`, ` Hello ` all match the same key after `.lower().strip()`
- **Fallback response** — unknown inputs return `"I do not understand"` instead of crashing

---

## 🚀 How to Run

```bash
python project1.py
```

No dependencies needed — pure Python only.

---

## 📸 Output Screenshot

![Project 1 - Chatbot Terminal Output](chatbot_run.png)

**What the screenshot demonstrates:**
- `hello` → greeted correctly
- `HELLO` → same response (`.lower()` sanitization working ✅)
- ` HI ` with spaces → matched correctly (`.strip()` working ✅)
- `what is your name?` → fallback triggered (punctuation not stripped — expected, shows fallback works ✅)
- `what is your name` → correct match ✅
- `bye` → clean goodbye and program exits ✅

---

## 💬 Supported Intents

| Input | Response |
|---|---|
| `hello` / `hi` | Greeting response |
| `how are you` | Status response |
| `what is your name` | Identity response |
| `what can you do` | Capability response |
| `help` | Lists available commands |
| `thanks` / `thank you` | Acknowledgement |
| `bye` / `exit` / `quit` | Exits the program |
| *anything else* | Fallback: "I do not understand" |

---

## 🛠 Tech Stack

- Python 3.11
- No external libraries

---

## ✍️ Author

Aliza Mazher — AI Engineering Intern, DecodeLabs (Batch 2026)
