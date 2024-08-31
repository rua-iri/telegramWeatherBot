

class User():
    def __init__(
            self,
            first_name: str,
            last_name: str,
            id: int,
            username: str,
    ) -> None:
        self.id = id,
        self.name = f"{first_name} {last_name}",
        self.username = username,

    def __repr__(self) -> str:
        return f"""
        Name: {self.name},
        ID: {self.id},
        Username: {self.username}
"""
