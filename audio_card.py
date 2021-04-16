from botbuilder.core import CardFactory, MessageFactory
from botbuilder.schema import (
    ActionTypes,
    Attachment,
    AnimationCard,
    AudioCard,
    HeroCard,
    OAuthCard,
    VideoCard,
    ReceiptCard,
    SigninCard,
    ThumbnailCard,
    MediaUrl,
    CardAction,
    CardImage,
    ThumbnailUrl,
    Fact,
    ReceiptItem,
    AttachmentLayoutTypes,
)

def create_audio_card(audio_url_custom):
    card = AudioCard(
        # media=[MediaUrl(url="https://wavlist.com/wav/father.wav")],
        media = [MediaUrl(url=audio_url_custom)],
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
        buttons=[
            CardAction(
                type=ActionTypes.open_url
                # title="Read more",
                # value="https://en.wikipedia.org/wiki/The_Empire_Strikes_Back",
            )
        ],
    )
    return CardFactory.audio_card(card)