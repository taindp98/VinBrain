from botbuilder.schema import AudioCard,CardAction,ActionTypes,MediaUrl
from botbuilder.core import CardFactory

def create_audio_card():
    card = AudioCard(
        # media=[MediaUrl(url="https://wavlist.com/wav/father.wav")],
        media = [MediaUrl(url='/home/taindp/VINBRAIN_INTERNSHIP/audio/test.wav')]
        # title="I am your father",
        # subtitle="Star Wars: Episode V - The Empire Strikes Back",
        # text="The Empire Strikes Back (also known as Star Wars: Episode V – The Empire Strikes "
        # "Back) is a 1980 American epic space opera film directed by Irvin Kershner. Leigh "
        # "Brackett and Lawrence Kasdan wrote the screenplay, with George Lucas writing the "
        # "film's story and serving as executive producer. The second installment in the "
        # "original Star Wars trilogy, it was produced by Gary Kurtz for Lucasfilm Ltd. and "
        # "stars Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony "
        # "Daniels, David Prowse, Kenny Baker, Peter Mayhew and Frank Oz.",
        # image=ThumbnailUrl(
        #     url="https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg"
        # ),
        # buttons=[
            # CardAction(
                # type=ActionTypes.open_url,
                # title="Play",
                # value="/home/taindp/VINBRAIN_INTERNSHIP/audio/test.wav",
            )
        # ]
    # )
    return CardFactory.audio_card(card)