# 🍪 Cookie Clicker Automation  

**Cookie Clicker Automation** is a Python project that plays the online **[Cookie Clicker Game](https://orteil.dashnet.org/experiments/cookie/)** automatically. Using Selenium, this script clicks cookies, evaluates upgrades, and purchases the best available options to maximize your cookies-per-second (CPS). Perfect for showcasing your automation skills and having fun!

## 🚀 Features
- 🔄 **Automated Cookie Clicking**: No more manual clicks!
- 💡 **Smart Upgrade Strategy**: Evaluates and purchases the best affordable upgrade every 5 seconds.
- ⏱️ **Time-Limited Execution**: Runs for 5 minutes by default, but can be customized.
- 📈 **Performance Display**: Outputs cookies-per-second (CPS) at the end of the session.

## 📋 Requirements

- **Python**: Version 3.8 or higher.
- **Browser**: Google Chrome installed and up to date.
- **Dependencies**: 
  - [`selenium`](https://pypi.org/project/selenium/)
  - [`webdriver-manager`](https://pypi.org/project/webdriver-manager/)
 
## 🛠️ Installation & Setup

- Clone this repository:
```
git clone https://github.com/your-username/cookie-clicker-automation.git
cd cookie-clicker-automation
```

- Install dependencies:
```
pip install -r requirements.txt
```

- Run the script:
```
python automated-game-bot.py
```

## 🕹️ How It Works 

- Starts the Game:
  * Opens Cookie Clicker in a Chrome browser.

- Continuous Clicking:
  * Clicks the cookie as fast as possible using Selenium.
- Smart Upgrades:
  * Every 5 seconds, checks all available upgrades.
  * Purchases the most expensive upgrade that can be afforded with the current cookies.
- Ends After 5 Minutes:
  * Stops execution and displays the final CPS rate


## 🌟 Highlights
This project showcases:

- Web scraping and browser automation with Selenium.
- Real-time decision-making for upgrades.
- Effective use of Python for time-sensitive tasks.

## 📸 Demo 
[`Demonstration`](https://drive.google.com/file/d/18170-vK9eQJP0tPGVrabDJc__bCZc7z4/view?usp=sharing)



