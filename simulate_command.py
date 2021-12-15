def make_date_condition(month: str, year: int):
    return f'Date+=+[{month}+{year}]'

def make_age_condition(age: int):
    return f'Crop.Age+=+5'

def make_dos_condition(mm: float):
    return f'Crop.MeanLiftDOS+>+{mm}'

class SimulateCommand:
    def __init__(self, condition: str, event: dict) -> None:
        self.condition = condition
        self.event=event