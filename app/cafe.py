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
            raise NotVaccinatedError("Visitor has no vaccine")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if expiration_date is not None:
            current_date = datetime.date.today()

            if current_date > expiration_date:
                raise OutdatedVaccineError("Visitor has no vaccine")

        if ("wearing_a_mask" not in visitor
                or visitor.get("wearing_a_mask") is False):
            raise NotWearingMaskError("Visitor have buying a mask")

        return (f"Welcome to {self.name}")
