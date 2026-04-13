# Orba — AI Studio

A responsive, browser-based AI chat interface built with HTML, CSS, and JavaScript as a front-end web development assignment.

## Overview

Orba is a single-page chat application that simulates an AI assistant experience. It features an earthy, organic design aesthetic using warm parchment and terracotta tones, with a collapsible sidebar, theme switching, voice input, synthesized sound effects, and smooth animations — all in a single `.html` file with no back-end required.

## Features

- **AI Chat Interface** — Send and receive messages with a simulated AI assistant (Orba)
- **Voice Input** — Speak your message using the microphone button; transcribed automatically via the Web Speech API and sent to the chat
- **Sound Effects** — Unique send and receive sounds synthesized in real time using the Web Audio API — no audio files needed
- **Dark / Light Theme** — Toggle between dark and light modes with smooth colour transitions
- **Responsive Layout** — Fully functional on desktop and mobile; sidebar slides in/out on smaller screens
- **Chat History Sidebar** — Displays previous sessions and allows starting a new session
- **Suggestion Cards** — Four quick-start prompt cards on the welcome screen to get started instantly
- **Export Chat** — Download the full conversation as a `.txt` file
- **Typing Indicator** — Animated dots while Orba is "thinking"
- **Markdown-style Formatting** — AI responses support bold, italic, inline code, and code blocks

## Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Structure and layout |
| CSS3 | Custom properties, Flexbox, keyframe animations |
| JavaScript (ES6+) | App logic, Web Audio API, Web Speech API |
| jQuery 3.7 | DOM manipulation and event handling |
| Bootstrap 5.3 | Responsive grid and utilities |
| Font Awesome 6.4 | Icons throughout the UI |
| Google Fonts | Fraunces (serif) + Plus Jakarta Sans |

## File Structure

```
Python-Assignment-/
├── orba.html        # Main application — entire app in one file
├── screenshots/     # UI screenshots for documentation
└── README.md        # This file
```

## How to Run

1. Download or clone the repository
2. Open `orba.html` in any modern browser (Chrome or Edge recommended)
3. No server, no install, no dependencies — it runs entirely in the browser

> **Note:** Voice input requires microphone permission and works best in Chrome or Edge. The browser must be served over `http://` or `https://` for mic access (not `file://` in some browsers).


## Author

**Ayesha** — Front-End Web Development Assignment  
GitHub: [@SyedaAyesha-28](https://github.com/SyedaAyesha-28/Python-Assignment-)
