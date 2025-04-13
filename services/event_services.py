from model import Session, Event
from schemas import show_events, show_event


def add_event_service(form):
    """
    Adicionar um novo evento à lista.
    """

    event = Event(
        title=form.title,
        date=form.date,
        hour=form.hour
    )

    try:
        session = Session()
        session.add(event)
        session.commit()
        return show_event(event), 200
    except Exception:
        error_msg = 'Não foi possível adicionar o evento.'
        return {'message': error_msg}, 400
    
def get_events_service():
    """
    Retornar lista com TODOS os eventos.
    """
    session = Session()
    events = session.query(Event).all()

    return show_events(events)

def get_event_service(query):
    """
    Retornar informações de UM evento a partir do seu ID.
    """
    session = Session()
    event = session.query(Event).filter(Event.id == query.id).first()
    return show_event(event) if event else {'message': 'Evento inexistente'}, 404

def delete_event_service(query):
    """
    Deletar um evento a partir do ID.
    """
    session = Session()
    count = session.query(Event).filter(Event.id == query.id).delete()
    session.commit()
    if count:
        return {'message': 'Evento removido', 'id': query.id}, 200
    else:
        return {'message': 'Evento não encontrado'}, 404

def update_event_service(query, form):
    """
    Atualizar informações de um evento a partir do ID.
    """
    session = Session()
    event = session.query(Event).filter(Event.id == query.id).first()
    
    if not event:
        return {'message': 'Evento não encontrado'}, 404

    event.title = form.title if form.title else event.title
    event.date = form.date if form.date else event.date
    event.hour = form.hour if form.hour else event.hour

    try:
        session.commit()
        return show_event(event), 200
    except Exception:
        error_msg = 'Não foi possível atualizar este evento'
        return {'message': error_msg}, 400

