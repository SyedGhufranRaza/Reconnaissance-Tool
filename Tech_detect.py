import sys
from Wappalyzer import Wappalyzer, WebPage

def detect_with_wappalyzer(url):
    try:
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        technologies = wappalyzer.analyze(webpage)
        return technologies
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tech_detect.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    print(f"[*] Scanning: {url}")
    result = detect_with_wappalyzer(url)

    print("\n--- Detected Technologies ---")
    if isinstance(result, set):
        print(', '.join(result))
    else:
        print(result)
