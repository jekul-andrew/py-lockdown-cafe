from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    masks_to_buy = 0
    vaccinated = True

    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)

        except VaccineError:
            vaccinated = False

        except NotWearingMaskError:
            masks_to_buy += 1

    # Out part

    if vaccinated is False:
        return "All friends should be vaccinated"

    elif masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
