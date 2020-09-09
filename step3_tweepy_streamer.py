from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import neeraj_twitter_credentials

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """    Class for streaming and processing live tweets."""
    def __init__(self):
        pass
    
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(neeraj_twitter_credentials.CONSUMER_KEY, neeraj_twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(neeraj_twitter_credentials.ACCESS_TOKEN, neeraj_twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """    This is a basic listener that just prints received tweets to stdout."""
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True


    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list =["Product_Name", "Sony PlayStation VR", "Dell Inspiron 15 7000", "Amazon Fire 7", "Ikea Symfonisk Bookshelf WiFi Speaker", "Motorola Razr", 
                    "Moto G Stylus", "Moto G Power", "Amazon Echo", "be3D DeeGreen 3D Printer", "Amazon Echo Show 8", "LG Velvet", "Canon PIXMA MG7160", "Samsung SyncMaster 2333SW 23-inch LCD Monitor",
                    "Razer Raptor 27", "Alienware AW5520QF Monitor", "HP Envy 32 All-in-One", "Google Pixel Buds 2", "Anker Soundcore Liberty Air 2", "Apple iPhone 4S", 
                    "Dell SP2309W", "DJI Phantom 3 Advanced", "ThinkPad X1 Carbon", "Samsung Galaxy S20 5G", "Sennheiser Momentum True Wireless 2", "ImageClass MF820Cdn",
                    "H7 Series USB-C Monitor", "Yoga Tablet 10", "Motorola Razr 2019", "Samsung Sero TV 43-inch", "Apple iMac 21.5-inch (2019)", "Dell KM717 Premier Wireless Keyboard and Mouse ",
                    "HP Color Laser 150nw", "Epson Expression Home XP-5105 ", "Sony MDR-XB950N1", "Bose SoundSport Free", "Samsung Galaxy A51", "VG248QE", "Amazon Fire HD 8 Plus",
                    "Inspiron 15 5000", "Aspire One 721", "Amazon Fire 7 (2019)", "Moto G8 Plus", "Aculaser C1100", "VIZIO SmartCast SB3851 5.1 Sound Bar System review", 
                    "Vizio SB36512-F6", "Google Nest Mini", "Alienware AW2720HF", "Razer Raptor", "HL-4150CDN", "Asus ZenBook Pro Duo", "Amazon Fire HD 8 (2020)",
                    "SSD 520 Series 480GB", "LG 49WL95C", "Apple HomePod", "AirPods (2019)", "Samsung Galaxy Buds Plus", "AirPods", "Envy 5540 All-in-One Printer",
                    "Pixel Buds", "Turtle Beach Stealth 600P Gen 2 review", "Motorola One Macro", "Spectre x360 15", "Samsung Galaxy Buds Live", "Apple Music", 
                    "Acer Predator X27 review", "Acer Swift 3 (2019)", "Thunderbolt Display", "Yamaha YAS-209", "Samsung Galaxy Tab S6", 
                    "Sonos IKEA Symfonisk bookshelf speaker", "DJI Spark", "VIZIO M-Series M65-E0", "Beats PowerBeats Pro", "Google Pixel 4 XL", "LG Gram 17 (2020)",
                    "G2460P", "Microsoft Surface Laptop 3", "Lenovo Smart Display", "Jabra Elite Active 75t", "Jabra Elite 75t", "QuietComfort 35 II ", "SoundLink Revolve",
                    "Apple MacBook Pro (13-inch, 2020)", "UltraSharp UP3218K ", "Microsoft Surface Go 2", "Samsung Galaxy S10", "Samsung Galaxy Tab S6 Lite", 
                    "Anker Soundcore Liberty Air", "Samsung Galaxy S9", "Dell G5 15 SE (2020) review", "Samsung Galaxy Buds", "Audio Technica ATH-M50X", "HL-L9200CDWT",
                    "Deskjet 3630", "Lenovo ThinkPad X1 Yoga (3rd Gen)", "Dell Latitude 5300 2-in-1 laptop", "S3851W-D4", "Razer Blade Stealth 13", 
                    "Sennheiser Ambeo 3D Soundbar", "Canon Pixma TR8550 ", "Brother MFC-J5330DW", "Surface Book", "LG Gallery OLED TV", "PlayStation VR", "TCL 55R617",
                    "Sony WH-1000XM3", "Pixma MG7150", "Amazon Echo Dot (2nd Gen)", "Dell XPS 13 (2020)", "Surface Pro 3", "Surface Pro 4", "SoundLink Mini II", "MacBook Pro 16-inch (2019)",
                    "HP Spectre x360 13 (2019)", "Google Pixel 3 XL", "Samsung Galaxy Note 10 Plus", "Phantom 4", "Amazon Echo Studio", "Yoga C930", "Apple AirPods Pro",
                    "Acer Spin 5 (2020) review", "Microsoft Surface Headphones 2 review", "Bose Noise Cancelling Headphones 700", "Reference On-Ear", "Amazon Echo (2017)", 
                    "Sonos Beam", "LG HU85LA", "Vizio V-Series 2.1-Channel Soundbar", "Sonos Arc", "Sony WF-1000XM3", "Sonos One", "Dell XPS 13 (2019)", 
                    "HP Spectre x360 (2020)", "Levana Mila baby monitor", "Lenovo Mirage AR Lets You Play as Marvel's Greatest Heroes", "Acer Nitro 7 (2020) review: hands-on",
                    "Epson Runsense SF-110 GPS Watch", "Apple iCloud review", "Google Pixel USB-C Earbuds", "HP Envy 7640", "Lenovo Y27g RE", 
                    "Sony MDR-XB950BT Extra Bass Bluetooth Headset", "Samsung Galaxy A20", "Amazon Echo Show 5", "Brother MFC-J470DW", "Dell 24 Gaming Monitor S2421HGF", "AOC G2460PF", 
                    "Sennheiser GSP 370",
"Lenovo Smart Display 7",
"Sennheiser Momentum 3 Wireless review",
"Vizio 65-inch D65u-D2",
"Hisense H9F (65H9F)",
"Klipsch Gig Bluetooth Speaker Review",
"Vizio S4251w-B4 Review: Soundbar",
"Bose SoundLink Mini",
"Dell Inspiron 27 7000",
"LG UM7300PUA Review",
"Microsoft Surface Book 3",
"Moto G Stylus review",
"LG Velvet review",
"M3D Micro 3D Printer Starter Kit",
"Motorola X Pure Edition",
"Turtle Beach Stealth 600 Gen 2 review",
"Asus VivoPC",
"Microsoft Surface Pro 7",
"Lenovo Yoga Home 900",
"Samsung Galaxy Watch Active 2",
"Microsoft OneDrive review",
"Fiil Canviis Headphones",
"Samsung Galaxy A50",
"Galaxy S10e",
"Sonos Move review",
"Samsung Galaxy Watch 3",
"Audio-Technica ATH-M50xBT Wireless Over-Ear Headphones",
"Google Pixel Buds",
"Sony WF-1000xM3",
"Beats Powerbeats 4 review",
"VIZIO M65-C1 65-Inch 4K Ultra HD Smart LED TV",
"TCL 6-Series Roku TV R625",
"Vizio SmartCast P-Series 55-inch 4K Ultra HD TV",
"Yamaha YAS-209 Review: An Excellent, Affordable Alexa Soundbar",
"Bose Soundbar 500 Review",
"Samsung Galaxy Watch",
"Amazon Echo (Gen 2)",
"Ikea Symfonisk Bookshelf Speaker Review: A Bargain Sonos Speaker",
"Google Nest Hub Max",
"Apple iMac 27-inch (2020) review",
"Vizio 50-inch V505-G9",
"Vizio M-Series Quantum 65-inch",
"Samsung RU7100 50"",
"TCL 4 Series Roku TV (55S425) review",
"Samsung Galaxy Tab S6 Lite review",
"Amazon Fire HD 8",
"Microsoft Surface Go 2 review",
"Amazon Fire TV Cube (2019) Review",
"Apple MacBook Pro 2020 (13-inch)",
"Galaxy S20",
"Samsung Galaxy S20 Plus",
"Google Pixel 4 XL review",
"DJI Phantom 3 Standard",
"Alienware AW5520QF 55-Inch OLED Gaming Monitor Review",
"Bowers & Wilkins PX Headphones",
"Apple AirPods with Wireless Charging Case",
"Canon Pixma MG3620",
"Brother HL-L2390DW Laser All-In-One Printer",
"Canon Pixma TS8320 Review",
"Canon Pixma TR150",
"Acer XFA240",
"Dell XPS 8900 Special Edition Gaming PC",
"HP Stream Mini Desktop 200-010",
"Dell G5 15 SE",
"Acer Aspire E 15 Review",
"Bose QuietComfort 35 II",
"Sony a6600",
"Sony WH-1000XM3 Headphones",
"Epson Premium Expression XP-820",
"Sonos Playbase",
"DJI Mavic Mini",
"LG OLED65C9PUA",
"Apple Mac mini (2018)",
"iPhone SE",
"Apple Macbook Pro 16" (2019)",
"Moto G Power review",
"DJI Phantom 4 Drone",
"HP Color LaserJet Pro M277dw",
"Epson Expression XP-640",
"Canon ImageClass MF743Cdw Color Laser Printer Review",
"Logitech Pro X Wireless",
"Razer Blackshark V2",
"Dell XPS 17",
"Dell XPS 13 review (2020)",
"Acer Predator X34",
"Jabra Elite Active 75t review",
"Apple iPhone XR",
"Apple iPhone 11",
"TCL 65R625",
"LifeStraw",
"Samsung Galaxy S20 Ultra 5G",
"Motorola Moto G7",
"Samsung Galaxy S10E",
"Galaxy A51",
"Galaxy Note 10+",
"Sony WH-XB900N Extra Bass",
"Bose SoundSport Wireless",
"Beats Powerbeats Pro",
"Audio Technica ATH-M50x",
"Bose SoundLink Around-Ear Wireless Headphones II",
"Jabra Elite Active 65t",
"Sennheiser Ambeo Soundbar",
"Vizio V21",
"VIZIO SB3621N-E8",
"Razer Blade Stealth",
"Afinia H-Series H479",
"Google Pixel Slate"
]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
