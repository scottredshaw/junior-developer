from pydantic import BaseModel, computed_field
from urllib.parse import urlparse


class Source(BaseModel):
    id: str
    title: str
    source: str
    
    @computed_field
    @property
    def favicon_url(self) -> str:
        domain = urlparse(self.source).hostname or ""
        return f"https://www.google.com/s2/favicons?domain={domain}&sz=32"


class Data(BaseModel):
    category: str
    question: str
    sources: list[Source]
    content: str
