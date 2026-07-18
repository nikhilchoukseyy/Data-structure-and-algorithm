# ### Short Problem Statement

# **Convert a time given in 12-hour AM/PM format to 24-hour (military) format.**

# **Input:** A string in the format `hh:mm:ssAM` or `hh:mm:ssPM`.

# **Output:** Return the equivalent time in 24-hour format (`HH:MM:SS`).

# **Rules:**

# * `12:xx:xx AM` → `00:xx:xx`
# * `12:xx:xx PM` → `12:xx:xx`
# * `01–11 AM` → unchanged
# * `01–11 PM` → add 12 to the hour

# **Example:**

# ```
# Input:  07:05:45PM
# Output: 19:05:45

def timeConversion() : 
  time_input = input()
  hour = int(time_input[:2])
  time = time_input[2:-2]
  period = time_input[-2:]

  if period == "AM": 
    if hour == 12 : 
      hour = 0 
  else : 
    if hour != 12 : 
      hour+= 12 
    
  return f"{hour:02d}{time}"

print(timeConversion())