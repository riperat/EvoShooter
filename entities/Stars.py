import urllib.request
import urllib.parse


def extract_string(source_string, start_string, end_string):
    start_index = source_string.find(start_string)
    if start_index == -1:
        return None

    start_index += len(start_string)
    end_index = source_string.find(end_string, start_index)
    if end_index == -1:
        return None

    return source_string[start_index:end_index]


artist_name = "rammstein"
artist_ID = ''


def get_artist_tags():
    url = 'http://musicbrainz.org/ws/2/artist/?query=artist:' + str(artist_name)

    response = urllib.request.urlopen(url).read().decode()

    print("===TAGS===")

    start_tag = '<name>'
    end_tag = '</name>'

    start_index = response.find("<tag-list>", 0)
    end_index = response.find("</tag-list>", 0)
    parse_xml(end_index, end_tag, response, start_index, start_tag)
    print()
    return extract_string(response, "<artist id=\"", "\"")


def get_artist_songs():
    global artist_ID
    url = "http://musicbrainz.org/ws/2/artist/" + str(artist_ID) + "?inc=works"
    response = urllib.request.urlopen(url).read().decode()

    print("===WORKS===")

    start_tag = '<title>'
    end_tag = '</title>'

    start_index = response.find("<work-list count=\"119\">", 0)
    end_index = response.find("</work-list>", start_index)

    parse_xml(end_index, end_tag, response, start_index, start_tag)


def parse_xml(end_index, end_tag, response, start_index, start_tag):
    tag_names = []
    while True:
        start = response.find(start_tag, start_index)
        if start >= end_index or start == -1:
            break

        start += len(start_tag)
        end = response.find(end_tag, start)
        tag_name = response[start:end].strip()
        tag_names.append(tag_name)

        start_index = end + len(end_tag)
    for tag in tag_names:
        print(tag)


artist_ID = get_artist_tags()
get_artist_songs()
