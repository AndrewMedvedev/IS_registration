from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base, str_uniq, int_pk, str_nullable 

    
class Security(Base):
    id: Mapped[int_pk]
    first_name: Mapped[str_nullable]
    last_name: Mapped[str_nullable]
    first_name_fa: Mapped[str_nullable]
    birthday: Mapped[str_nullable]
    city_birthday: Mapped[str_nullable]
    phone_number: Mapped[str_uniq]
    email: Mapped[str_uniq]
    hash_password: Mapped[str_nullable]
    
   
    def __str__(self):
            return (f"{self.__class__.__name__}(id={self.id}, "
                    f"first_name={self.first_name!r},"
                    f"last_name={self.last_name!r})")


    def __repr__(self):
        return str(self)