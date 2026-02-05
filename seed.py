from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from heroes import HEROES


def seed_db():
    # Crée une session de base de données
    db = SessionLocal()
    try:
        print("Vérification de la base de données...")

        # On vérifie si la table est déjà remplie pour éviter les doublons
        existing_count = db.query(models.Heroes).count()
        if existing_count > 0:
            print(f"La table contient déjà {existing_count} héros. On ne rajoute rien.")
            return

        print("Insertion des héros en cours...")
        for h in HEROES:
            # Correction automatique pour l'ID 9 (le set {'...'} devient un string)
            name = h.full_name
            if isinstance(name, set):
                name = list(name)[0]

            # Création de l'objet SQLAlchemy
            new_hero = models.Heroes(
                id=h.id,
                nick_name=h.nick_name,
                full_name=name,
                occupation=h.occupation,
                powers=h.powers,
                hobby=h.hobby,
                type=h.type,
                rank=h.rank
            )
            db.add(new_hero)

        # SAUVEGARDE FINALE
        db.commit()
        print("✅ Succès ! Tes 9 héros sont maintenant dans la base de données.")

    except Exception as e:
        print(f"❌ Erreur lors de l'insertion : {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_db()