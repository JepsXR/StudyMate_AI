from sqlalchemy import String, create_engine, Enum, CheckConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from typing import Literal

# DATABASE CREATION

engine = create_engine("DATABASE_URL")
SessionLocal = sessionmaker(bind=engine)

base = DeclarativeBase()

session = SessionLocal()

class User(base):
    __tablename__ = "Users"
    id = Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int]
    strongest_learning_style: Mapped[Literal[
        "Visual", "Auditory", "Kinesthetic", "Reading/Writing", "Other"]] = mapped_column(
            Enum("Visual", "Auditory", "Kinesthetic", "Reading/Writing", "Other"), default="Other")
    info_learning_style: Mapped[str] = mapped_column(String(100))
    available_hours_per_day: Mapped[float]
    study_subjects: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    concentration_level: Mapped[Literal[
        "Low", "Moderate", "High"]] = mapped_column(
            Enum("Low", "Moderate", "High"), default="Moderate"
        )
    info_exam: Mapped[str] = mapped_column(String(100))

    __table_args__ = (
        CheckConstraint("age >= 10 AND age <= 100", name="chk_age_range"),
        CheckConstraint("available_hours_per_day >= 0 AND available_hours_per_day <= 24", name="chk_hours_range"),
        CheckConstraint("cardinality(study_subjects) <= 4", name="chk_subjects_max")
    )