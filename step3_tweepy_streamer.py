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
    hash_tag_list =["SonyPlayStationVR", "DellInspiron15", "AmazonFire7", "IkeaSymfonisk", "MotorolaRazr", "MotoGStylus", "MotoGPower", "AmazonEcho", "be3DDeeGreen3DPrinter", "AmazonEchoShow8", "LGVelvet", "CanonPIXMAMG7160", "SamsungSyncMaster2333SW23-inchLCDMonitor", "RazerRaptor27", "AlienwareAW5520QFMonitor", "HPEnvy32All-in-One", "GooglePixelBuds2", "AnkerSoundcoreLibertyAir2", "AppleiPhone4S", "DellSP2309W", "DJIPhantom3Advanced", "ThinkPadX1Carbon", "SamsungGalaxyS205G", "SennheiserMomentumTrueWireless2", "ImageClassMF820Cdn", "H7SeriesUSB-CMonitor", "YogaTablet10", "MotorolaRazr2019", "SamsungSeroTV43-inch", "AppleiMac21.5-inch(2019)", "DellKM717PremierWirelessKeyboardandMouse", "HPColorLaser150nw", "EpsonExpressionHomeXP-5105", "SonyMDR-XB950N1", "BoseSoundSportFree", "SamsungGalaxyA51", "VG248QE", "AmazonFireHD8Plus", "Inspiron155000", "AspireOne721", "AmazonFire7(2019)", "MotoG8Plus", "AculaserC1100", "VIZIOSmartCastSB3851", "VizioSB36512", "GoogleNestMini",  "AlienwareAW2720HF", "RazerRaptor", "HL-4150CDN", "AsusZenBookProDuo", "AmazonFireHD8(2020)", "SSD520Series480GB", "LG49WL95C", "AppleHomePod", "AirPods(2019)", "SamsungGalaxyBudsPlus", "AirPods", "Envy5540All-in-OnePrinter", "PixelBuds", "TurtleBeachStealth600PGen2review", "MotorolaOneMacro", "Spectrex36015", "SamsungGalaxyBudsLive", "AppleMusic", "AcerPredatorX27review", "AcerSwift3(2019)", "ThunderboltDisplay", "YamahaYAS-209", "SamsungGalaxyTabS6", "SonosIKEASymfoniskbookshelfspeaker", "DJISpark", "VIZIOM-SeriesM65-E0", "BeatsPowerBeatsPro",  "GooglePixel4XL", "LGGram17(2020)", "G2460P", "MicrosoftSurfaceLaptop3", "LenovoSmartDisplay", "JabraEliteActive75t", "JabraElite75t", "QuietComfort35II", "SoundLinkRevolve", "AppleMacBookPro(13-inch,2020)", "UltraSharpUP3218K", "MicrosoftSurfaceGo2", "SamsungGalaxyS10", "SamsungGalaxyTabS6Lite", "AnkerSoundcoreLibertyAir", "SamsungGalaxyS9", "DellG515SE(2020)review", "SamsungGalaxyBuds", "AudioTechnicaATH-M50X", "HL-L9200CDWT", "Deskjet3630", "LenovoThinkPadX1Yoga(3rdGen)", "DellLatitude53002-in-1laptop", "S3851W-D4", "RazerBladeStealth13", "SennheiserAmbeo3DSoundbar", "CanonPixmaTR8550", "BrotherMFC-J5330DW", "SurfaceBook", "LGGalleryOLEDTV", "PlayStationVR", "TCL55R617", "SonyWH-1000XM3", "PixmaMG7150", "AmazonEchoDot(2ndGen)", "DellXPS13(2020)", "SurfacePro3", "SurfacePro4", "SoundLinkMiniII", "MacBookPro16-inch(2019)", "HPSpectrex36013(2019)", "GooglePixel3XL", "SamsungGalaxyNote10Plus", "Phantom4", "AmazonEchoStudio", "YogaC930", "AppleAirPodsPro", "AcerSpin5(2020)review", "MicrosoftSurfaceHeadphones2review", "BoseNoiseCancellingHeadphones700", "ReferenceOn-Ear", "AmazonEcho(2017)", "SonosBeam", "LGHU85LA", "VizioV-Series2.1-ChannelSoundbar", "SonosArc", "SonyWF-1000XM3", "SonosOne", "DellXPS13(2019)", "HPSpectrex360(2020)", "LevanaMilababymonitor", "LenovoMirageARLetsYouPlayasMarvel'sGreatestHeroes", "AcerNitro7(2020)review:hands-on", "EpsonRunsenseSF-110GPSWatch", "AppleiCloudreview", "GooglePixelUSB-CEarbuds", "HPEnvy7640", "LenovoY27gRE", "SonyMDR-XB950BTExtraBassBluetoothHeadset", "SamsungGalaxyA20", "AmazonEchoShow5", "BrotherMFC-J470DW", "Dell24GamingMonitorS2421HGF", "AOCG2460PF", "SennheiserGSP370", "LenovoSmartDisplay7", "SennheiserMomentum3Wirelessreview", "Vizio65-inchD65u-D2", "HisenseH9F(65H9F)", "KlipschGigBluetoothSpeakerReview", "VizioS4251w-B4Review:Soundbar", "BoseSoundLinkMini", "DellInspiron277000", "LGUM7300PUAReview", "MicrosoftSurfaceBook3", "MotoGStylusreview", "LGVelvetreview", "M3DMicro3DPrinterStarterKit", "MotorolaXPureEdition", "TurtleBeachStealth600Gen2review", "AsusVivoPC", "MicrosoftSurfacePro7", "LenovoYogaHome900", "SamsungGalaxyWatchActive2", "MicrosoftOneDrivereview", "FiilCanviisHeadphones", "SamsungGalaxyA50", "GalaxyS10e", "SonosMovereview", "SamsungGalaxyWatch3", "Audio-TechnicaATH-M50xBTWirelessOver-EarHeadphones", "GooglePixelBuds", "SonyWF-1000xM3", "BeatsPowerbeats4review", "VIZIOM65-C165-Inch4KUltraHDSmartLEDTV", "TCL6-SeriesRokuTVR625", "VizioSmartCastP-Series55-inch4KUltraHDTV", "YamahaYAS-209Review:AnExcellent,AffordableAlexaSoundbar", "BoseSoundbar500Review", "SamsungGalaxyWatch", "AmazonEcho(Gen2)", "IkeaSymfoniskBookshelfSpeakerReview:ABargainSonosSpeaker", "GoogleNestHubMax", "AppleiMac27-inch(2020)review", "Vizio50-inchV505-G9", "VizioM-SeriesQuantum65-inch", "SamsungRU710050", "TCL4SeriesRokuTV(55S425)review", "SamsungGalaxyTabS6Litereview", "AmazonFireHD8", "MicrosoftSurfaceGo2review", "AmazonFireTVCube(2019)Review", "AppleMacBookPro2020(13-inch)", "GalaxyS20", "SamsungGalaxyS20Plus", "GooglePixel4XLreview", "DJIPhantom3Standard", "AlienwareAW5520QF55-InchOLEDGamingMonitorReview", "Bowers&WilkinsPXHeadphones", "AppleAirPodswithWirelessChargingCase", "CanonPixmaMG3620", "BrotherHL-L2390DWLaserAll-In-OnePrinter", "CanonPixmaTS8320Review", "CanonPixmaTR150", "AcerXFA240", "DellXPS8900SpecialEditionGamingPC", "HPStreamMiniDesktop200-010", "DellG515SE", "AcerAspireE15Review", "BoseQuietComfort35II", "Sonya6600", "SonyWH-1000XM3Headphones", "EpsonPremiumExpressionXP-820", "SonosPlaybase", "DJIMavicMini", "LGOLED65C9PUA", "AppleMacmini(2018)", "iPhoneSE", "AppleMacbookPro16(2019)", "MotoGPowerreview", "DJIPhantom4Drone", "HPColorLaserJetProM277dw", "EpsonExpressionXP-640", "CanonImageClassMF743CdwColorLaserPrinterReview", "LogitechProXWireless", "RazerBlacksharkV2", "DellXPS17", "DellXPS13review(2020)", "AcerPredatorX34", "JabraEliteActive75treview", "AppleiPhoneXR", "AppleiPhone11", "TCL65R625", "LifeStraw", "SamsungGalaxyS20Ultra5G", "MotorolaMotoG7", "SamsungGalaxyS10E", "GalaxyA51", "GalaxyNote10+", "SonyWH-XB900NExtraBass", "BoseSoundSportWireless", "BeatsPowerbeatsPro", "AudioTechnicaATH-M50x", "BoseSoundLinkAround-EarWirelessHeadphonesII", "JabraEliteActive65t", "SennheiserAmbeoSoundbar", "VizioV21", "VIZIOSB3621N-E8", "RazerBladeStealth", "AfiniaH-SeriesH479", "GooglePixelSlate"]
    
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
