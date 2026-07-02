from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = ""
    priority: str = "media"
    status: str = "pendiente"
    due_date: Optional[str] = None
    notes: Optional[str] = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())