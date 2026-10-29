import json
import re
from pathlib import Path

from fastapi import APIRouter

from app.models import Data

router = APIRouter(tags=["data"])

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "mock.json"

full_names: list[str] = ["Daniel Okafor", "Sarah Jones", "Priya Shah", "Tom Reid"]
first_names: list[str] = ["Daniel", "Sarah", "Priya", "Tom"]
last_names: list[str] = ["Okafor", "Jones", "Shah", "Reid"]
numbers: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

@router.get("/data")
def get_data() -> list[Data]:
    items = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    result = []
    for item in items:
        data = redact_data(item)
        data_object = Data.model_validate(data)
        data_object.content = add_links(
            data_object.content,
            data_object.sources
        )
        result.append(data_object)
    return result

def redact_data(item) -> dict:
    """Method to remove names from question"""
    # what I am thinking is adding a new method for model_validate to acc change the information
    # and redact it
    for key, value in item.items():
        if key == "question":
            value = redact_name(value)
            value = redact_phone(value)
            value =redact_email(value)
            item["question"] = value
    return item

def redact_name(sentence:str) -> str:
    """Method to remove names from question"""
    redacted_sentence = sentence
    # this is under the assumption everyone in the database has both first and last names
    for index in range(len(full_names)):
        # order goes full names first, to stop repeating of [NAME]
        if full_names[index] in sentence:
            redacted_sentence = redacted_sentence.replace(full_names[index], "[NAME]")
        if first_names[index] in sentence:
            redacted_sentence = redacted_sentence.replace(first_names[index], "[NAME]")
        if last_names[index] in sentence:
            redacted_sentence = redacted_sentence.replace(last_names[index], "[NAME]")
    return redacted_sentence

def redact_email(sentence:str) -> str:
    """Method to remove email from question"""
    redacted_sentence = sentence
    words = sentence.split()
    for word in words:
        if "@" in word:
            redacted_sentence = redacted_sentence.replace(word, "[EMAIL]")
    return redacted_sentence

def redact_phone(sentence: str) -> str:
    """Method to remove phone from question"""
    return re.sub(r"\b\d[\d ]{3,}\d\b", "[PHONE]", sentence)

def add_links(content: str, sources: list[Source]) -> str:
    """Method to add links from source class to the content given the id.
       Making links be bold and italic
    """
    for source in sources:
        if source.id in content:
            link = (
                f'<i><b><a href="{source.source}">{source.title}</a></b></i>'
            )
            content = content.replace(
                f"<ref>{source.id}</ref>",
                link
            )
    return content
