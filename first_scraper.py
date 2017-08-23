import urllib.request

def get_page(file_path):
    open_file = open(file_path, "wb")

    html_file = urllib.request.urlopen("http://econpy.pythonanywhere.com/ex/001.html")
    html_file = html_file.read()

    open_file.write(html_file)
    open_file.close()

if __name__ == "__main__":
    file_path = "tmp.html"

    get_page(file_path)