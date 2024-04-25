<h1 align="center">WACheckmate</h1>
<h3 align="center">WhatsApp Bulk Number Checker & Validator Tool</h3>

WACheckmate is a bulk WhatsApp number checking tool crafted with Python and utilizing Selenium.

It serves the fundamental purpose of verifying the availability of a number on WhatsApp. This tool can validate whether a given number is registered on WhatsApp or not, enabling you to efficiently verify large lists of multiple numbers through automation.

<p align="center">
    <a href="http://github.com/anooppushpad/WACheckmate" alt="Made with Python">
        <img src="https://forthebadge.com/images/badges/made-with-python.svg" /></a>
</p>

## Features

- [x] Bulk WhatsApp Number Validation
- [x] Country Code Validation
- [x] CSV Result Export

## Requirements
```bash
pip install selenium
```
## How to Use it ? (Usage)

Follow the steps below to use this tool:

1. Ensure you have Python installed on your Windows system. If not, you can download and install it from [here](https://www.python.org/downloads/). Additionally, I have already included the Windows chromedriver with the repository. However, if you are not using Windows, you can download the appropriate chromedriver from [here](https://googlechromelabs.github.io/chrome-for-testing/) for your system.

2. After installing Python and the setting up the chromedriver, you need to input the numbers within the `numbers.txt` file along with the country code. For example, `+912903372794`, where `+91` is the country code.

3. Once you have input the numbers, run the `main.py` script, and follow the instructions provided.

4. Once the checking is complete, the results will be saved in a CSV file within the folder.

## Pull requests are welcome!

If you spot an error or something doesn't make sense, feel free to send me a pull request. Thanks for your contribution!

## Bug Reports and Feedback

If you encounter any bugs or have any feedback, please raise them under Github issues. Pull requests are also more than welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

MIT  © [Anoop Pushpad](https://github.com/anooppushpad)
