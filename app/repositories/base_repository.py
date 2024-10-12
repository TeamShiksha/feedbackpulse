from typing import TypeVar, Generic, Optional, List, Dict, Any
from sqlalchemy.orm import Session
from app.models import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    """
    Base repository for CRUD inside any model

    Args:
        model (Model_Type): The model class to work with
    """

    def __init__(self, model: ModelType) -> None:
        """
        Constructor

        Args:
            model (ModelType): To work with any model
        """
        self.model = model

    def get(self, session: Session, _id: int | str) -> Optional[ModelType]:
        """
        Get a single record based on the provided ID.

        Args:
            session (Session): DB session object for query.
            _id (int | str): ID of the record.

        Returns:
            Optional[ModelType]: The record if found, otherwise None.
        """
        return session.query(self.model).filter(self.model.id == _id).first()

    def get_all(self, session: Session, skip: int = 0,\
                limit: int = 10) -> List[ModelType]:
        """
        Get multiple records from a table with pagination.

        Args:
            session (Session): DB session object for query.
            skip (int): Offset for the query.
            limit (int): Maximum number of records to retrieve.

        Returns:
            List[ModelType]: A list of records.
        """
        return session.query(self.model).offset(skip).limit(limit).all()

    def post(self, session: Session, create_obj: Dict[str, Any]) -> ModelType:
        """
        Create a new record in the table.

        Args:
            session (Session): DB session object for query.
            create_obj (Dict[str, Any]): Dictionary of data to create the record.

        Returns:
            ModelType: The created model instance.
        """
        db_model_obj = self.model(**create_obj)
        session.add(db_model_obj)
        session.commit()
        session.refresh(db_model_obj)
        return db_model_obj

    def put(self, session: Session, _id: int | str,\
            update_object: Dict[str, Any]) -> Optional[ModelType]:
        """
        Update an existing record in the table based on the ID.

        Args:
            session (Session): DB session object for query.
            _id (int | str): ID of the record to update.
            update_object (Dict[str, Any]): Data to update the record.

        Returns:
            Optional[ModelType]: The updated record if successful, otherwise None.
        """
        session.query(self.model).filter(self.model.id == _id).update(update_object)
        session.commit()
        return self.get(session, _id)

    def delete(self, session: Session, _id: int | str):
        """
        Delete a record from table based on id

        Args:
            session [Session]: DB session object for query
            _id [int | str]: id of the record
        """
        delete_obj = session.query(self.model).filter(self.model.id == _id).first()
        session.delete(delete_obj)
        session.commit()
        return delete_obj
