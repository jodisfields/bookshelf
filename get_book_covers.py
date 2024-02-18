import requests
from bs4 import BeautifulSoup

# List of Goodreads URLs
urls = [
    "https://www.goodreads.com/book/show/9361589-the-night-circus",
    "https://www.goodreads.com/book/show/31434883-eleanor-oliphant-is-completely-fine",
    "https://www.goodreads.com/book/show/35959740-circe",
    "https://www.goodreads.com/book/show/32620332-the-seven-husbands-of-evelyn-hugo",
    "https://www.goodreads.com/book/show/36809135-where-the-crawdads-sing",
    "https://www.goodreads.com/book/show/11250317-the-song-of-achilles",
    "https://www.goodreads.com/book/show/41057294-normal-people",
    "https://www.goodreads.com/book/show/50623864-the-invisible-life-of-addie-larue",
    "https://www.goodreads.com/book/show/17333223-the-goldfinch",
    "https://www.goodreads.com/book/show/49127718-anxious-people",
    "https://www.goodreads.com/book/show/34273236-little-fires-everywhere",
    "https://www.goodreads.com/book/show/44318414-the-dutch-house",
    "https://www.goodreads.com/book/show/19063.The_Book_Thief",
    "https://www.goodreads.com/book/show/21853621-the-nightingale",
    "https://www.goodreads.com/book/show/34912895-the-great-alone",
    "https://www.goodreads.com/book/show/25883848-the-hating-game",
    "https://www.goodreads.com/book/show/18774964-a-man-called-ove",
    "https://www.goodreads.com/book/show/35133922-educated",
    "https://www.goodreads.com/book/show/38746485-becoming",
    "https://www.goodreads.com/book/show/13158800-the-light-between-oceans",
    "https://www.goodreads.com/book/show/16181775-the-rosie-project",
    "https://www.goodreads.com/book/show/19486412-big-little-lies",
    "https://www.goodreads.com/book/show/32051912-the-alice-network",
    "https://www.goodreads.com/book/show/43801204-the-giver-of-stars",
    "https://www.goodreads.com/book/show/23309634-before-we-were-strangers",
    "https://www.goodreads.com/book/show/41150287-the-flatshare",
    "https://www.goodreads.com/book/show/40097951-the-silent-patient",
    "https://www.goodreads.com/book/show/38819868-my-sister-the-serial-killer",
    "https://www.goodreads.com/book/show/34189556-the-wife-between-us",
    "https://www.goodreads.com/book/show/50646695-the-lost-apothecary",
    "https://www.goodreads.com/book/show/52578297-the-midnight-library",
    "https://www.goodreads.com/book/show/45047384-the-house-in-the-cerulean-sea",
    "https://www.goodreads.com/book/show/56025591-the-ex-hex",
    "https://www.goodreads.com/book/show/50093834-the-book-of-lost-names",
    "https://www.goodreads.com/book/show/52867387-beach-read",
    "https://www.goodreads.com/book/show/34189556-the-last-mrs-parrish",
    "https://www.goodreads.com/book/show/51933429-the-guest-list",
    "https://www.goodreads.com/book/show/39863488-the-huntress",
    "https://www.goodreads.com/book/show/50008321-the-paris-library",
    "https://www.goodreads.com/book/show/49374439-the-wife-upstairs",
    "https://www.goodreads.com/book/show/38259130-one-day-in-december",
    "https://www.goodreads.com/book/show/42201431-the-unhoneymooners",
    "https://www.goodreads.com/book/show/35523006-the-tattooist-of-auschwitz",
    "https://www.goodreads.com/book/show/18293427-the-storied-life-of-a-j-fikry",
    "https://www.goodreads.com/book/show/45754981-the-glass-hotel",
    "https://www.goodreads.com/book/show/45885644-the-sun-down-motel",
    "https://www.goodreads.com/book/show/43822805-the-family-upstairs",
    "https://www.goodreads.com/book/show/51791252-the-vanishing-half",
    "https://www.goodreads.com/book/show/43575115-the-starless-sea",
    "https://www.goodreads.com/book/show/54985743-people-we-meet-on-vacation",
]

# Function to get the image URL from a Goodreads page
def get_image_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tag = soup.find('img', class_='ResponsiveImage')
    if image_tag and 'src' in image_tag.attrs:
        return image_tag['src']
    return None

# Get and print the image URLs
for url in urls:
    image_url = get_image_url(url)
    print(f"image: {image_url},")


