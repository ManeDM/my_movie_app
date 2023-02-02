from models.actor import Actor as ActorMoldel

class ActorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_actors(self) -> ActorMoldel:
        result = self.db.query(ActorMoldel).all()
        return result

    def get_movie_by_id(self, id: int):
        result = self.db.query(ActorMoldel).filter(ActorMoldel.id == id).first()
        return result

    def create_actor(self,actor:ActorMoldel):
        new_actor = ActorMoldel(
        actor_first_name = actor.actor_first_name ,
        actor_last_name = actor.actor_last_name,
        actor_gender = actor.actor_gender,    
        )
        self.db.add(new_actor)
        self.db.commit()
        return

    def update_actor(self,id:int, actor:ActorMoldel):
        actor_entity = self.db.query(ActorMoldel).filter(ActorMoldel.id == id).first()
        actor_entity.actor_first_name = actor.actor_first_name
        actor_entity.actor_last_name = actor.actor_last_name
        actor_entity.actor_gender = actor.actor_gender     
        self.db.commit()
        return

    def delete_actor(self, id: int):
        actor = self.get_actor_by_id(id)
        if not actor:
            return None
        self.db.delete(actor)
        self.db.commit()
        return actor

    def get_actor_by_id(self, id: int):
        return self.db.query(ActorMoldel).filter(ActorMoldel.id == id).first()