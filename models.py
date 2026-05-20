from extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from typing import List

mechanic_service = db.Table(
    'mechanic_service',
    db.Column('ticket_id', db.ForeignKey('service_tickets.id')),
    db.Column('mechanic_id', db.ForeignKey('mechanics.id'))
)

class Customer(db.Model):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    email: Mapped[str] = mapped_column(db.String(360), nullable=False, unique=True)
    DOB: Mapped[date]
    address: Mapped[str] = mapped_column(db.String(255), nullable=False)

    service_tickets: Mapped[List['ServiceTicket']] = db.relationship(back_populates='customer')

class Mechanic(db.Model):
    __tablename__ = 'mechanics'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    position: Mapped[str] = mapped_column(db.String(200), nullable=False)


    service_tickets: Mapped[List['ServiceTicket']] = db.relationship(secondary=mechanic_service, back_populates='mechanics')

class ServiceTicket(db.Model):
    __tablename__ = 'service_tickets'

    id: Mapped[int] = mapped_column(primary_key=True)
    booking_date: Mapped[date]
    days_required: Mapped[int] = mapped_column(nullable=False)
    issue_reported: Mapped[str] = mapped_column(db.Text, nullable=False)
    jobs_done: Mapped[str] = mapped_column(db.Text, nullable=False)
    pickup_dropoff: Mapped[bool] = mapped_column(nullable=False)
    followup_reqd: Mapped[bool] = mapped_column(nullable=False)
    job_completed: Mapped[bool] = mapped_column(nullable=False)

    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))

    customer: Mapped['Customer'] = db.relationship(back_populates='service_tickets')
    mechanics: Mapped[List['Mechanic']] = db.relationship(secondary=mechanic_service, back_populates='service_tickets')