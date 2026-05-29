from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey,BigInteger,DateTime
from sqlalchemy.sql import func
from database import Base
# from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
    
class User1(Base):
    __tablename__ = "tableemployee"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(255), nullable=False)   
    email = Column(String(255), unique=True, nullable=False)
    phonenumber=Column(BigInteger,nullable=False)
    city=Column(String(255),nullable=False)
    state=Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

class User2(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(255), nullable=False)   
    email = Column(String(255), unique=True, nullable=False)
    phonenumber=Column(BigInteger,nullable=False)
    city=Column(String(255),nullable=False)
    state=Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Updated Time
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

 


class User4(Base):
    __tablename__ = "student_attendance"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(255), nullable=False)   
    email = Column(String(255), unique=True, nullable=False)
    phonenumber=Column(BigInteger,nullable=False)
    city=Column(String(255),nullable=False)
    state=Column(String(255),nullable=False)
    # string=Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Updated Time
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

 
