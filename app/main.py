from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    masks_to_buy = 0
    vaccinated = True

    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)

        except VaccineError:
            vaccinated = False

        except NotWearingMaskError:
            masks_to_buy += 1

    out_txt = f"Friends can go to {cafe.name}"

    if vaccinated is False:
        out_txt = "All friends should be vaccinated"

    elif masks_to_buy:
        out_txt = f"Friends should buy {masks_to_buy} masks"

    return out_txt
