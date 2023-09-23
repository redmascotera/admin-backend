"""Import CSV actions."""

from typing import (
    Iterable,
    TypeVar,
)
import csv
import logging

from app import models


logger = logging.getLogger(__name__)


Readable = TypeVar("Readable", bound=Iterable[str])


def import_csv_file(csv_file: Readable):
    """
    Import a csv file into the database for pet tags
    :param csv_file: readable file IO object, or list/iterable of strings
    :return:
    """
    logger.info("Importing csv file")
    reader = csv.reader(csv_file, delimiter=",")
    for idx, row in enumerate(reader):
        if idx == 0:
            # Skip the header row
            continue
        import_row(row)


def import_row(row: list[str]):
    """
    Import a row from the csv file creating the database model for pettag
    :param row: Row expect to have this format:
        id,chapa,codigo,mascota,email,propietario,tel1,tel2,last_modified
    :return:
    """
    # Extract the values from the row
    _, tag_str, code, pet_name, email, owner_name, phone_str, alt_phone_str, _ = row
    # Create empty placeholders
    owner: models.Owner | None = None
    pet: models.Pet | None = None
    phone: models.Phone | None = None
    alt_phone: models.Phone | None = None
    # Get or create the tag
    if not tag_str:
        logger.info("Skipping empty tag")
        return
    logger.info(f"Get or create tag {tag_str}")
    tag, _ = models.PetTag.objects.get_or_create(
        tag=tag_str,
        defaults={
            "code": code,
        },
    )
    # Prepare Phones if they exist
    if phone_str:
        logger.info(f"Get or create phone {phone_str}")
        phone, _ = models.Phone.objects.get_or_create(
            phone=phone_str,
        )
        if phone not in tag.phones.all():
            logger.info(f"Add phone {phone_str} to tag {tag_str}")
            tag.phones.add(phone)
    if alt_phone_str:
        logger.info(f"Get or create alt phone {alt_phone_str}")
        alt_phone, _ = models.Phone.objects.get_or_create(
            phone=alt_phone_str,
        )
        if alt_phone not in tag.phones.all():
            logger.info(f"Add alt phone {alt_phone_str} to tag {tag_str}")
            tag.phones.add(alt_phone)
    # Get or create the owner
    if owner_name:
        logger.info(f"Get or create owner {owner_name}")
        owner, _ = models.Owner.objects.get_or_create(
            name=owner_name,
            defaults={
                "email": email,
            },
        )
        if phone and phone not in owner.phones.all():
            logger.info(f"Add phone {phone_str} to owner {owner_name}")
            owner.phones.add(phone)
        if alt_phone and alt_phone not in owner.phones.all():
            logger.info(f"Add alt phone {alt_phone_str} to owner {owner_name}")
            owner.phones.add(alt_phone)
        tag.owner = owner
    # create the pet if present
    if pet_name:
        logger.info(f"Creating Pet {pet_name}")
        pet = models.Pet.objects.create(
            name=pet_name,
            owner=owner,
        )
        tag.pet = pet
    # Save the tag
    logger.info(f"Saving tag {tag_str}")
    tag.save()
