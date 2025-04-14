from pydantic import BaseModel, Field
from typing import List

from model.event_model import Event


class EventSchema(BaseModel):
    id: int = 1
    title: str = 'Calendário de Reuniões'
    date: str = '2025-04-08'
    hour: str = '10:00'  # Formato de data e hora


class EventViewSchema(BaseModel):
    """Schema para visualização de um evento"""
    id: int = 1
    title: str = 'Calendário de Reuniões'
    date: str = '2025-04-08'
    hour: str = '10:00'  # Formato de data e hora
    

class EventPostSchema(BaseModel):
    """Schema para adicionar de um evento"""
    title: str = Field(..., max_length=200, description='Título do evento')
    date: str = Field(..., description='Data do evento no formato YYYY-MM-DD')
    hour: str = Field(..., description='Hora do evento no formato HH:MM')

class EventUpdateSchema(BaseModel):
    """Schema para atualização de um evento"""
    title: str = Field(None, max_length=200, description='Título do evento')
    date: str = Field(None, description='Data do evento no formato YYYY-MM-DD')
    hour: str = Field(None, description='Hora do evento no formato HH:MM')

class EventListSchema(BaseModel):
    """Schema para lista de eventos"""
    events: List[EventViewSchema]

class EventDelSchema(BaseModel):
    """Schema para deleção de um evento"""
    message: str
    id: int
class EventSearchForId(BaseModel):
    """Schema para busca de um evento por ID"""
    id: int = Field(..., description='ID do evento')

def show_events(events:List[Event]):
    """Representação dos eventos em lista"""
    result = []
    for event in events:
        result.append({
            'id': event.id,
            'title': event.title,
            'date': event.date,
            'hour': event.hour,
        })
    return {'events': result}, 200

def show_event(event: Event):
    """Representação de um evento"""
    return {
        'id': event.id,
        'title': event.title,
        'date': event.date,
        'hour': event.hour,
    }