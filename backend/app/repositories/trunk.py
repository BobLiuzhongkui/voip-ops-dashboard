"""Repository for Trunk CRUD operations."""
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.trunk import Trunk, TrunkStatus
from app.schemas.trunk import TrunkCreate, TrunkUpdate


class TrunkRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, trunk_id: int) -> Optional[Trunk]:
        return self.db.query(Trunk).filter(Trunk.id == trunk_id).first()

    def get_all(
        self,
        skip: int = 0,
        limit: int = 50,
        status: Optional[TrunkStatus] = None,
    ) -> tuple[List[Trunk], int]:
        q = self.db.query(Trunk)
        if status is not None:
            q = q.filter(Trunk.status == status)
        total = q.count()
        items = q.order_by(Trunk.created_at.desc()).offset(skip).limit(limit).all()
        return items, total

    def create(self, data: TrunkCreate) -> Trunk:
        trunk = Trunk(**data.model_dump())
        self.db.add(trunk)
        self.db.commit()
        self.db.refresh(trunk)
        return trunk

    def update(self, trunk: Trunk, data: TrunkUpdate) -> Trunk:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(trunk, field, value)
        self.db.commit()
        self.db.refresh(trunk)
        return trunk

    def delete(self, trunk: Trunk) -> None:
        self.db.delete(trunk)
        self.db.commit()
