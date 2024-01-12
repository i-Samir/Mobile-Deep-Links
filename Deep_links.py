import os
import sys
from androguard.core.bytecodes.apk import APK
from biplist import *

# Function to extract deep links from APK files
def extract_deep_links_from_apk(apk_path):
    try:
        apk = APK(apk_path)
        deep_links = apk.get_intent_filters('android.intent.action.VIEW')
        return deep_links
    except Exception as e:
        print("Error extracting deep links from APK: {e}")
        return []

# Function to extract deep links from iOS applications
def extract_deep_links_from_ios(ipa_path):
    try:
        plist = readPlist(ipa_path)
        deep_links = plist.get("CFBundleURLTypes")
        return deep_links
    except Exception as e:
        print("Error extracting deep links from iOS application: {e}")
        return []

# Main function
def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_deep_links.py <file>")
        return

    file_path = sys.argv[1]
    file_extension = os.path.splitext(file_path)[1]

    if not os.path.isfile(file_path):
        print("File not found: {file_path}")
        return

    if file_extension == ".apk":
        deep_links = extract_deep_links_from_apk(file_path)
    elif file_extension == ".ipa":
        deep_links = extract_deep_links_from_ios(file_path)
    else:
        print("Unsupported file format. Only APK and IPA files are supported.")
        return

    if deep_links:
        print("Deep links:")
        for link in deep_links:
            print(link)
    else:
        print("No deep links found.")

if __name__ == "__main__":
    main()
