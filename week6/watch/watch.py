import sys
import re




def main():
    print(parse(input("HTML: ")))




def parse(s):

    try:
        pattern = (
            r'<iframe[^>]*'
            r'src="https?://(?:www\.)?youtube\.com/embed/'
            r'([A-Za-z0-9_-]+)"'
        )
        match = re.search(pattern, s)
        if not match:
            return None
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"





    except:
        print("except")
        sys.exit(1)




if __name__ == "__main__":
    main()