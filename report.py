class Report:
    items = {}
    def __init__(self, items) -> None:
        self.items = items
        
    def generate_report(self) -> None:
        for item in self.items():
            item.to_string()