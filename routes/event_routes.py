from flask_openapi3 import Tag
from flask import jsonify
from schemas import *
from schemas.event_schemas import *
from services.event_services import (
    add_event_service,
    get_events_service,
    get_event_service,
    delete_event_service,
    update_event_service
)

event_tag = Tag(name="Event", description="Adiciona, Visualiza, Remove e Edita um evento.")

def init_event_routes(app):
    @app.post('/api/event', tags=[event_tag],
              responses={'200': EventViewSchema, '409': ErrorSchema, '400': ErrorSchema})
    def add_event(form: EventPostSchema):
        """
        POST: Adicionar um novo evento à lista.
        """
        return add_event_service(form)

    @app.get('/api/events', tags=[event_tag],
              responses={'200': EventListSchema, '409': ErrorSchema, '404': ErrorSchema})
    def get_events():
        """
        GET: Retornar lista com TODOS os eventos.
        """
        return get_events_service()

    @app.get('/api/event', tags=[event_tag],
              responses={'200': EventViewSchema, '404': ErrorSchema})
    def get_event(query: EventSearchForId):
        """
        GET: Retornar informações de UM evento.
        """
        return get_event_service(query)

    @app.delete('/api/event', tags=[event_tag],
               responses={'200': EventDelSchema, '404': ErrorSchema})
    def del_event(query: EventSearchForId):
        """
        DELETE: Remover um evento.
        """
        return delete_event_service(query)

    @app.put('/api/event', tags=[event_tag],
              responses={'200': EventViewSchema, '404': ErrorSchema, '422': ErrorSchema})
    def update_event(query: EventSearchForId, form: EventUpdateSchema):
        """
        PUT: Atualizar informações de um evento.
        """
        return update_event_service(query, form)

