import xml.etree.ElementTree as ET
import re
import logging
from datetime import datetime

# Configure logging for unprocessed SMS
logging.basicConfig(filename="../Logs/unprocessed_sms.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# SMS Categorization Patterns
CATEGORIES = {
    "Incoming Money": r"You have received (\d+) RWF from (.+?)\.",
    "Payments to Code Holders": r"Your payment of (\d+) RWF to (.+?) has been completed\.",
    "Transfers to Mobile Numbers": r"Transfer of (\d+) RWF to (.+?) has been processed\.",
    "Bank Deposits": r"Bank deposit of (\d+) RWF completed for (.+?)\.",
    "Airtime Bill Payments": r"Your payment of (\d+) RWF to Airtime has been completed\.",
    "Cash Power Bill Payments": r"You paid (\d+) RWF for Cash Power\.",
    "Transactions Initiated by Third Parties": r"TxId: (\d+). Transaction of (\d+) RWF initiated by (.+?)\.",
    "Withdrawals from Agents": r"withdrawn (\d+) RWF on (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\.",
    "Bank Transfers": r"You have transferred (\d+) RWF to bank account (.+?)\.",
    "Internet and Voice Bundle Purchases": r"You have purchased an internet bundle of .* for (\d+) RWF"
}

def parse_sms_data(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    parsed_sms = []

    for sms in root.findall("sms"):
        body = sms.find("body").text.strip()
        categorized = False

        for category, pattern in CATEGORIES.items():
            match = re.search(pattern, body)
            if match:
                amount = int(match.group(1))
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                parsed_sms.append((category, amount, timestamp, body))
                categorized = True
                break

        if not categorized:
            logging.info(f"Uncategorized SMS: {body}")

    return parsed_sms

if __name__ == "__main__":
    sms_data = parse_sms_data("../Data/sms_data.xml")
    print(sms_data)
