import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor does not have a vaccination.")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if expiration_date is not None:
            current_date = datetime.date.today()

            if current_date > expiration_date:
                raise OutdatedVaccineError(
                    "Visitor's vaccination has expired."
                )

        if ("wearing_a_mask" not in visitor
                or visitor.get("wearing_a_mask") is False):
            raise NotWearingMaskError(
                "Visitor should buy or wear a mask to enter the cafe."
            )

        return (f"Welcome to {self.name}")
