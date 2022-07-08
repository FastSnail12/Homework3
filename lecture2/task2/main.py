from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        delta = timedelta(days=1)
        for period in self.dates:
            start_period = period[0]
            end_period = period[1]
            while start_period <= end_period:
                yield start_period
                start_period += delta
