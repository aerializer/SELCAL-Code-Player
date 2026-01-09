# SELCAL-Code-Player
A lightweight and cross-platform SELCAL code audio player that generates and plays dual-tone SELCAL signals with pure Python, no complex dependencies.

## ✨ Features
- 🎵 Generate & play standard SELCAL dual-frequency audio signals
- 🌍 **Cross-platform support**: Works perfectly on Windows, macOS and Linux
- ✅ **3 Input Formats Supported**: `ABCD` / `AB-CD` / `AB CD` (super flexible)
- ✅ Case-insensitive input (supports both uppercase/lowercase SELCAL codes)
- 🧹 Auto clean up temporary audio files after playback
- ⚡ Stable playback without `simpleaudio` dependency (uses system native audio players)

## 📋 Supported SELCAL Format & Characters
3 flexible valid formats for 4 official SELCAL characters:
✅ Pure characters: `ABCD`
✅ Hyphen separated: `AB-CD`
✅ Space separated: `AB CD`

**Supported Characters**: A,B,C,D,E,F,G,H,J,K,L,M,P,Q,R,S,T,U,V,W,X,Y,Z & 1,2,3,4,5,6,7,8,9
(Note: No I, O, 0 in official SELCAL standard)

## 🚀 Quick Start
### Install Dependencies
```bash
pip install pydub
