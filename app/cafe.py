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

        if datetime.date.today() > expiration_date:
            raise OutdatedVaccineError(
                "Visitor's vaccination has expired."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "Visitor should buy or wear a mask to enter the cafe."
            )

        return (f"Welcome to {self.name}")
