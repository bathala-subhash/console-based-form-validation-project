# 🧾 Console-Based User Input Validator

This is a beginner-friendly Python project designed to validate and format user inputs from the console using **Regular Expressions (Regex)** and built-in Python modules. It’s an ideal reference for those learning input validation, string manipulation, and basic use of the `re` and `calendar` modules.

The program runs interactively in the terminal, prompting the user to enter:

- 👤 **Full Name**
- 🎂 **Date of Birth** in `dd-mm-yyyy` format
- 📧 **Email ID** (restricted to Gmail)
- 📱 **Mobile Number** in `XXX-XXX-XXXX` format

It then processes and displays the cleaned and formatted data.

---

## 📌 Features

✅ **Name Validation**  
- Accepts only alphabetic characters and spaces.  
- Rejects numbers or special characters.

✅ **DOB Validation**  
- Ensures the date follows `dd-mm-yyyy` format.  
- Extracts and displays **Day**, **Month (as word)**, and **Year** using `calendar` module.

✅ **Email Validation**  
- Checks that the input is a valid Gmail address using lowercase characters.

✅ **Mobile Number Formatting**  
- Accepts mobile numbers in the format `123-456-7890`.  
- Removes dashes before displaying the final number.

---

## 🧠 Use Cases

This project is perfect for:
- 💡 **Learning Regex** in a practical way.
- 🧪 **Testing user input sanitization** in CLI-based apps.
- 📚 **Teaching validation logic** in Python courses.
- 🔐 Practicing **input security** for real-world applications.

---



