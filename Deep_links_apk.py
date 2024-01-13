import zipfile
import re
def extract_deep_links(apk_or_ipa_file):
  """Extracts deep links from an APK or IPA file.
  Args:
    apk_or_ipa_file: The path to the APK or IPA file.
  Returns:
    A list of deep links.
  """
  # Extract the AndroidManifest.xml file from the APK file.
  with zipfile.ZipFile(apk_or_ipa_file, 'r') as apk_or_ipa:
    manifest_file = apk_or_ipa.read('AndroidManifest.xml')
  # Parse the AndroidManifest.xml file for deep links.
  deep_links = []
  for line in manifest_file.splitlines():
    match = re.search(r'android:scheme="(.*?)"', line)
    if match:
      deep_links.append(match.group(1))
  return deep_links
if __name__ == '__main__':
  # Get the path to the APK or IPA file.
  apk_or_ipa_file = input('Enter the path to the APK or IPA file: ')
  # Extract the deep links from the APK or IPA file.
  deep_links = extract_deep_links(apk_or_ipa_file)
  # Print the deep links.
  for deep_link in deep_links:
    print(deep_link)

