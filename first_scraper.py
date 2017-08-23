import urllib.request

def get_page(file_path):
    open_file = open(file_path, "wb")

    html_file = urllib.request.urlopen("http://econpy.pythonanywhere.com/ex/001.html")
    html_file = html_file.read()

    open_file.write(html_file)
    open_file.close()


def get_title(file_path):
    open_file = open(file_path, "r")

    regex = '<div title="buyer-name">'
    regex_end = '</div>'

    for line in open_file.readlines():
        sentence = line.strip('\n')

        if regex in sentence:
            initial_pos = sentence.find(regex) + len(regex)
            final_pos = sentence.find(regex_end)

            print(sentence[initial_pos: final_pos])


if __name__ == "__main__":
    file_path = "tmp.html"

    get_page(file_path)
    get_title(file_path)