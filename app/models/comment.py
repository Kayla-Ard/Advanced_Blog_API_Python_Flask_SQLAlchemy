from app.database import db
from sqlalchemy.orm import Mapped, mapped_column

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    body: Mapped[str] = mapped_column(db.String(1000))
    user_id: Mapped[str] = mapped_column(db.Integer, nullable=False)
    
    def __str__(self):
        return self.id

    def __repr__(self):
        return f"<Comment {self.user_id}|{self.title}|{self.body}>"