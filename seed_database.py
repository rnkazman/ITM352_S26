"""
Database initialization and seed script for BNP Mobile App
Creates tables, loads sample park zones and species data
"""
import json
import os
from app import create_app
from backend.models import (
    db, User, UserTypeEnum, ParkZone, ZoneTypeEnum,
    AnimalSpecies, DangerLevelEnum, ConservationStatusEnum
)


def init_database():
    """Create all tables"""
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database tables created.")
        return app


def seed_admin(app):
    """Create default control centre user"""
    with app.app_context():
        if User.find_by_phone('+256700000001'):
            print("Admin user already exists, skipping.")
            return

        admin = User(
            phone_number='+256700000001',
            first_name='Control',
            last_name='Center',
            password='BNPcontrol2026!',
            user_type=UserTypeEnum.CONTROL
        )
        admin.is_verified = True
        admin.badge_number = 'CC-001'
        admin.department = 'Park Operations'
        admin.save()
        print(f"Admin user created: {admin.phone_number}")

        # Also create a sample guide
        guide = User(
            phone_number='+256700000002',
            first_name='Samuel',
            last_name='Okello',
            password='BNPguide2026!',
            user_type=UserTypeEnum.GUIDE
        )
        guide.is_verified = True
        guide.badge_number = 'GD-001'
        guide.department = 'Wildlife Guides'
        guide.save()
        print(f"Guide user created: {guide.phone_number}")

        # Sample medical staff
        medic = User(
            phone_number='+256700000003',
            first_name='Grace',
            last_name='Nakato',
            password='BNPmedic2026!',
            user_type=UserTypeEnum.MEDICAL
        )
        medic.is_verified = True
        medic.badge_number = 'MD-001'
        medic.department = 'Medical Services'
        medic.save()
        print(f"Medical staff created: {medic.phone_number}")


def seed_species(app):
    """Load animal species from data/animal_species.json"""
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'animal_species.json')
    if not os.path.exists(data_path):
        print(f"Species data file not found at {data_path}, skipping.")
        return

    with open(data_path, 'r') as f:
        species_data = json.load(f)

    with app.app_context():
        species_list = species_data if isinstance(species_data, list) else species_data.get('species', [])
        for sp in species_list:
            if AnimalSpecies.query.filter_by(name=sp['name']).first():
                print(f"  Species '{sp['name']}' already exists, skipping.")
                continue

            danger = DangerLevelEnum(sp.get('danger_level', 'low'))
            conservation = None
            if sp.get('conservation_status'):
                try:
                    conservation = ConservationStatusEnum(sp['conservation_status'])
                except ValueError:
                    pass

            species = AnimalSpecies(
                name=sp['name'],
                scientific_name=sp['scientific_name'],
                danger_level=danger
            )
            species.description = sp.get('description')
            species.safety_distance = sp.get('safety_distance')
            species.safety_notes = sp.get('safety_notes')
            species.behavior_notes = sp.get('behavior_notes')
            species.habitat_preferences = sp.get('habitat_preferences')
            species.identification_tips = sp.get('identification_tips')
            species.best_viewing_times = sp.get('best_viewing_times')
            species.rarity_score = sp.get('rarity_score', 5)
            species.population_in_park = sp.get('population_in_park')
            if conservation:
                species.conservation_status = conservation
            species.save()
            print(f"  Added species: {sp['name']}")

    print("Species seeding complete.")


def seed_zones(app):
    """Load park zones from data/park_zones.geojson"""
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'park_zones.geojson')
    if not os.path.exists(data_path):
        print(f"Zone data file not found at {data_path}, skipping.")
        return

    with open(data_path, 'r') as f:
        geojson = json.load(f)

    with app.app_context():
        for feature in geojson.get('features', []):
            props = feature.get('properties', {})
            name = props.get('name')
            if not name:
                continue

            if ParkZone.query.filter_by(name=name).first():
                print(f"  Zone '{name}' already exists, skipping.")
                continue

            try:
                zone_type = ZoneTypeEnum(props.get('zone_type', 'savanna'))
            except ValueError:
                zone_type = ZoneTypeEnum.SAVANNA

            zone = ParkZone(
                name=name,
                zone_type=zone_type,
                boundary_geojson=json.dumps(feature.get('geometry', {})),
                max_vehicles=props.get('max_vehicles', 20)
            )
            zone.zone_code = props.get('zone_code')
            zone.ecosystem_info = props.get('ecosystem_info')
            zone.terrain_difficulty = props.get('terrain_difficulty', 'easy')
            zone.danger_level = props.get('danger_level', 'low')
            zone.safety_notes = props.get('safety_notes')
            zone.requires_guide = props.get('requires_guide', False)
            zone.is_public = props.get('is_public', True)
            zone.attractions = props.get('attractions')
            zone.save()
            print(f"  Added zone: {name}")

    print("Zone seeding complete.")


def seed_all():
    """Run full database init + seed"""
    print("=== BNP Database Initialization ===")
    app = init_database()
    print("\n--- Seeding staff users ---")
    seed_admin(app)
    print("\n--- Seeding animal species ---")
    seed_species(app)
    print("\n--- Seeding park zones ---")
    seed_zones(app)
    print("\n=== Done ===")


if __name__ == '__main__':
    seed_all()
