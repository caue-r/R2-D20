# R2-D20 Discord Bot

R2-D20 is a **Discord** bot developed to assist in RPG games, mainly for initiative rolls and various dice rolls. It allows you to register player initiatives and perform custom dice rolls, following rules such as disadvantage, advantage, normal rolls, and critical rolls.

## Features

- **!iniciativa**: Starts listening for initiative messages in the chat.  
  - Registers initiatives in the format `D+X character_name`, `V+X character_name`, or `i+X character_name`.  
  - X is the bonus (or penalty) to be added or subtracted from the roll.  
  - `D` and `V` indicate disadvantage and advantage, respectively.  
  - `i` indicates a simple dice roll.  

- **!stop**: Ends the initiative registration and displays the list of results sorted in descending order.  

- **!roll**: Performs custom dice rolls.  
  - Accepted formats:  
    - `xdy`: Rolls X dice with Y sides and sums the results (e.g., `3d6`).  
    - `xdy+z`: Rolls X dice with Y sides and adds modifier Z (e.g., `1d20+3`).  
    - `x#dy`: Rolls X dice with Y sides and displays each result separately (e.g., `3#d20`).  
  - Additional features:  
    - On `1d20` rolls, if the result is 1, the bot shows a **Critical Failure** message with a red box.  
    - If the result is 20, the bot shows a **Critical Success** message with a green box.  
    - Other results appear in a blue box.  

## How to Use

1. Add the bot to your Discord server.  
2. Use the `!iniciativa` command to start registering initiatives.  
3. Players must send their initiatives in the format:  

   - `D+X character_name` (Disadvantage)  
   - `V+X character_name` (Advantage)  
   - `i+X character_name` (Normal roll)  

4. To roll custom dice, use the `!roll` command as shown in the examples.  
5. When all players have sent their initiatives, use the `!stop` command to see the organized list.  

## Requirements

To run the bot locally, you will need:  

- **Python 3.11** or higher  
- **discord.py** (to interact with the Discord API)  

## Installation Steps (Windows)

### 1. Download the Repository

Download the repository directly as a ZIP by clicking the **Code** button on the GitHub page and selecting **Download ZIP**. [Click here to download the ZIP file](https://github.com/caue-r/R2-D20/archive/refs/heads/main.zip).  

After downloading, extract the contents into a folder of your choice.  

### 2. Create a Virtual Environment

In the terminal, inside the folder where you extracted the contents, create a virtual environment:  

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

```bash
.env\Scriptsctivate
```

After activating the virtual environment, you will see the environment name in parentheses in the terminal, like:  

```scss
(venv) C:\path\to\project>
```

### 4. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set the Bot Token in the Code

Open the `.env` file in the text editor of your choice. In the file, you will see a line where the bot token is loaded. Replace INSERT YOUR TOKEN HERE KEEPING THE QUOTES with your real token:  

```bash
DISCORD_TOKEN="INSERT YOUR TOKEN HERE KEEPING THE QUOTES"
```

### 6. Run the Bot

```bash
python bot.py
```

### Disclaimer

R2-D20 does not collect any personal user information and is not officially related to Discord or any specific RPG system. It is an open-source project created for entertainment purposes and to enhance the gaming experience.
