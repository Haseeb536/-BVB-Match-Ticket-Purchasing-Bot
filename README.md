# ⚽ BVB Match Ticket Purchasing Bot

A Python-based automation script using **SeleniumBase** to automate the ticket purchasing process for Borussia Dortmund matches. The bot navigates the official BVB ticket shop, logs in, selects a match, chooses seats, and captures DOM/SVG snapshots for verification.
s

---

## ✨ Features

- **🎫 Automated Navigation** – Logs into the BVB ticket shop and navigates to the match selection page.
- **🪑 Seat Selection** – Automatically clicks the seat selection button.
- **📝 DOM & SVG Capture** – Saves the page's DOM and SVG content for debugging and verification.
- **🚀 Undetectable Mode** – Uses SeleniumBase's `uc=True` (undetected‑Chrome) to avoid bot detection.
- **⏱️ Configurable Delays** – Adjustable `time.sleep()` waits to handle page loading.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** (3.8+) | Core programming language |
| **SeleniumBase** | Enhanced Selenium framework with undetectable mode |
| **Selenium** | WebDriver for browser automation |
| **ChromeDriver** | Managed automatically by SeleniumBase |

---

## 📁 Project Structure

BVB-Match-Ticket-Purchasing-Bot/
├── BVB_bot.py          # Main automation script
├── requirements.txt    # Python dependencies
└── README.md           # This file

---

## 🚀 Getting Started

### Prerequisites

- **Python** 3.8 or later – [Download](https://python.org)
- **Google Chrome** browser installed
- **BVB Ticket Shop Account** – Valid credentials for the official BVB ticket portal

### Installation

1. Clone the repository:
   git clone https://github.com/Haseeb536/-BVB-Match-Ticket-Purchasing-Bot.git
   cd -BVB-Match-Ticket-Purchasing-Bot

2. Create a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure credentials:
   - Open `BVB_bot.py` and replace `"email"` and `"password"` with your actual BVB ticket shop credentials.
   - For security, use environment variables (e.g., `os.getenv("BVB_EMAIL")`) instead of hardcoding.

5. Run the bot:
   python BVB_bot.py

---

## ⚙️ Configuration

| Setting | Purpose |
|---------|---------|
| `email` | Your BVB ticket shop login email (hardcoded – update before running) |
| `password` | Your BVB ticket shop password (hardcoded – update before running) |
| `cookieConsentAgree` | XPath for the cookie consent button |
| `login-link` | XPath for the login link |
| `menu-item-1543` | XPath for the match selection menu |
| `choose-seat-button` | XPath for the seat selection button |

> **Note:** XPath selectors may change if the BVB ticket shop updates its website. Update them in the script as needed.

---

## 📖 Usage

1. Launch the bot – Run `python BVB_bot.py`.
2. Login – The bot automatically logs in using your credentials.
3. Select Match – Navigates to the desired match and selects it.
4. Choose Seats – Clicks the seat selection button.
5. Capture Output – Prints the DOM and SVG content of the current page to the console.

Example Output:
DOM content captured:
<!DOCTYPE html>...
SVG content captured:
<svg>...</svg>

---

## 🧩 Customisation

### Updating XPath Selectors
- Inspect the BVB ticket shop website and copy the new XPath for any changed elements.
- Update the corresponding `driver.find_element(By.XPATH, ...)` calls in `BVB_bot.py`.

### Adjusting Wait Times
- Modify the `time.sleep()` values to match your internet speed and page load times.
- Consider replacing fixed sleeps with explicit waits (`WebDriverWait`) for more robust automation.

### Adding Checkout Automation
- Extend the script to automatically complete the purchase (select payment method, confirm order) – currently the bot stops after seat selection.

### Error Handling & Retries
- Wrap critical actions in `try-except` blocks and implement retry logic for flaky elements.

---

## ⚠️ Important Disclaimers

- **⚠️ This bot is for educational purposes only.** Automated ticket purchasing may violate the terms of service of the BVB ticket shop.
- **🛡️ Use at your own risk.** The author is not responsible for any account bans, legal issues, or financial losses.
- **🔒 Never share your credentials.** Always use environment variables or encrypted config files instead of hardcoding.

---

## 📤 Deployment

### Run on a Scheduled Basis
- Use `cron` (Linux/macOS) or Task Scheduler (Windows) to run the bot at specific times (e.g., when tickets are released).

### Run on a VPS
- Deploy to a cloud server (DigitalOcean, AWS, etc.) for 24/7 operation.
- Use `screen` or `tmux` to keep the bot running in the background.

### Docker Support
- Create a `Dockerfile` with Python and Chrome installed.
- Run the container with environment variables for credentials.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## 📄 License

This project is open‑source and available under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgements

- [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) – Enhanced Selenium framework with undetectable mode.
- [Selenium](https://www.selenium.dev/) – Browser automation framework.

---

**Happy automating!** ⚽🤖
