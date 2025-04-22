"""Add disease records with symptoms, prevention, and treatment

Revision ID: acbf82665ce2
Revises: b32d7749b838
Create Date: 2024-11-12 16:05:19.573503

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.sql import table, column  # Make sure these are imported
from sqlalchemy import Integer, String

# revision identifiers, used by Alembic.
revision: str = 'acbf82665ce2'
down_revision: Union[str, None] = 'b32d7749b838'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Disease table representation
disease_table = table(
    'disease',
    column('DiseaseID', Integer),
    column('DiseaseName', String),
    column('Symptoms', String),
    column('Prevention', String),
    column('Treatment', String)
)

# Disease data
DISEASE_DATA = [
    {
        "DiseaseID": 0,
        "DiseaseName": "Apple Scab Leaf",
        "Symptoms": "Dark, olive-green spots on leaves; curling of leaves.",
        "Prevention": "Apply fungicide sprays; prune trees for better air circulation.",
        "Treatment": "Use sulfur or captan fungicides; remove infected leaves."
    },
    {
        "DiseaseID": 1,
        "DiseaseName": "Apple leaf",
        "Symptoms": "Yellowing and spotting of leaves.",
        "Prevention": "Ensure proper fertilization and watering.",
        "Treatment": "Apply appropriate fertilizers; manage pests if needed."
    },
    {
        "DiseaseID": 2,
        "DiseaseName": "Apple rust leaf",
        "Symptoms": "Bright orange spots on leaves and defoliation.",
        "Prevention": "Avoid planting near junipers; apply protective fungicides.",
        "Treatment": "Use fungicides like myclobutanil; remove infected leaves."
    },
    {
        "DiseaseID": 3,
        "DiseaseName": "Bell_pepper leaf",
        "Symptoms": "Spots and holes in leaves; yellowing.",
        "Prevention": "Avoid overhead watering; use resistant varieties.",
        "Treatment": "Apply copper-based fungicides; control aphids and mites."
    },
    {
        "DiseaseID": 4,
        "DiseaseName": "Bell_pepper leaf spot",
        "Symptoms": "Small dark spots with yellow halos on leaves.",
        "Prevention": "Use certified seeds; avoid leaf wetness.",
        "Treatment": "Apply chlorothalonil or mancozeb fungicides."
    },
    {
        "DiseaseID": 5,
        "DiseaseName": "Blueberry leaf",
        "Symptoms": "Red or brown spots on leaves; leaf drop.",
        "Prevention": "Prune for better air flow; use resistant varieties.",
        "Treatment": "Apply fungicides such as propiconazole."
    },
    {
        "DiseaseID": 6,
        "DiseaseName": "Cherry leaf",
        "Symptoms": "Yellowing, wilting, and premature leaf drop.",
        "Prevention": "Water adequately; avoid root stress.",
        "Treatment": "Apply fungicides; prune dead branches."
    },
    {
        "DiseaseID": 7,
        "DiseaseName": "Corn Gray leaf spot",
        "Symptoms": "Long, narrow gray lesions on leaves.",
        "Prevention": "Use resistant hybrids; rotate crops.",
        "Treatment": "Apply strobilurin or triazole fungicides."
    },
    {
        "DiseaseID": 8,
        "DiseaseName": "Corn leaf blight",
        "Symptoms": "Lesions that start as small spots and become large tan patches.",
        "Prevention": "Use resistant varieties; rotate crops.",
        "Treatment": "Apply fungicides if severe."
    },
    {
        "DiseaseID": 9,
        "DiseaseName": "Corn rust leaf",
        "Symptoms": "Small, brownish-red pustules on leaves.",
        "Prevention": "Use resistant varieties; timely planting.",
        "Treatment": "Apply fungicides like azoxystrobin if necessary."
    },
    {
        "DiseaseID": 10,
        "DiseaseName": "Peach leaf",
        "Symptoms": "Red spots and curled leaves.",
        "Prevention": "Apply dormant sprays in early spring.",
        "Treatment": "Use sulfur or chlorothalonil fungicides."
    },
    {
        "DiseaseID": 11,
        "DiseaseName": "Potato leaf",
        "Symptoms": "Yellowing and necrosis on leaves.",
        "Prevention": "Use certified seed; avoid overhead watering.",
        "Treatment": "Apply appropriate fungicides."
    },
    {
        "DiseaseID": 12,
        "DiseaseName": "Potato leaf early blight",
        "Symptoms": "Small brown spots with concentric rings.",
        "Prevention": "Crop rotation; use resistant varieties.",
        "Treatment": "Use chlorothalonil or mancozeb fungicides."
    },
    {
        "DiseaseID": 13,
        "DiseaseName": "Potato leaf late blight",
        "Symptoms": "Water-soaked lesions that turn brown and necrotic.",
        "Prevention": "Use resistant varieties; avoid wet conditions.",
        "Treatment": "Apply fungicides like mancozeb or metalaxyl."
    },
    {
        "DiseaseID": 14,
        "DiseaseName": "Raspberry leaf",
        "Symptoms": "Yellow or purple spots on leaves.",
        "Prevention": "Maintain proper spacing; prune infected canes.",
        "Treatment": "Use fungicides as needed."
    },
    {
        "DiseaseID": 15,
        "DiseaseName": "Soybean leaf",
        "Symptoms": "Brown spots and yellowing of leaves.",
        "Prevention": "Rotate crops; use resistant varieties.",
        "Treatment": "Apply fungicides if necessary."
    },
    {
        "DiseaseID": 16,
        "DiseaseName": "Squash Powdery mildew leaf",
        "Symptoms": "White, powdery spots on leaves.",
        "Prevention": "Ensure good air circulation; avoid overhead watering.",
        "Treatment": "Apply sulfur or potassium bicarbonate sprays."
    },
    {
        "DiseaseID": 17,
        "DiseaseName": "Strawberry leaf",
        "Symptoms": "Red or purple spots on leaves.",
        "Prevention": "Avoid overhead watering; remove infected leaves.",
        "Treatment": "Apply fungicides if necessary."
    },
    {
        "DiseaseID": 18,
        "DiseaseName": "Tomato Early blight leaf",
        "Symptoms": "Dark, concentric spots on leaves; leaf yellowing.",
        "Prevention": "Rotate crops; use resistant varieties.",
        "Treatment": "Apply fungicides like chlorothalonil."
    },
    {
        "DiseaseID": 19,
        "DiseaseName": "Tomato Septoria leaf spot",
        "Symptoms": "Small, circular spots with dark borders on leaves.",
        "Prevention": "Avoid overhead watering; use resistant varieties.",
        "Treatment": "Apply fungicides such as copper or mancozeb."
    },
    {
        "DiseaseID": 20,
        "DiseaseName": "Tomato leaf",
        "Symptoms": "Yellowing and spotting of leaves.",
        "Prevention": "Maintain good sanitation; avoid overhead watering.",
        "Treatment": "Use fungicides if necessary."
    },
    {
        "DiseaseID": 21,
        "DiseaseName": "Tomato leaf bacterial spot",
        "Symptoms": "Small, dark, water-soaked spots on leaves.",
        "Prevention": "Use disease-free seeds; avoid leaf wetness.",
        "Treatment": "Apply copper-based bactericides."
    },
    {
        "DiseaseID": 22,
        "DiseaseName": "Tomato leaf late blight",
        "Symptoms": "Large, water-soaked lesions on leaves and stems.",
        "Prevention": "Use resistant varieties; avoid wet foliage.",
        "Treatment": "Apply fungicides like mancozeb."
    },
    {
        "DiseaseID": 23,
        "DiseaseName": "Tomato leaf mosaic virus",
        "Symptoms": "Mosaic pattern of light and dark green on leaves.",
        "Prevention": "Remove infected plants; avoid tobacco contact.",
        "Treatment": "No chemical treatment; manage by sanitation."
    },
    {
        "DiseaseID": 24,
        "DiseaseName": "Tomato leaf yellow virus",
        "Symptoms": "Yellowing of leaves; stunted growth.",
        "Prevention": "Control whiteflies; use resistant varieties.",
        "Treatment": "No direct treatment; control whitefly populations."
    },
    {
        "DiseaseID": 25,
        "DiseaseName": "Tomato mold leaf",
        "Symptoms": "Grayish mold on leaves; leaf drop.",
        "Prevention": "Provide adequate ventilation; avoid wet foliage.",
        "Treatment": "Apply fungicides such as chlorothalonil."
    },
    {
        "DiseaseID": 26,
        "DiseaseName": "Tomato two spotted spider mites leaf",
        "Symptoms": "Yellow speckling and webbing on leaves.",
        "Prevention": "Use predatory mites; avoid over-fertilization.",
        "Treatment": "Apply miticides if infestation is severe."
    },
    {
        "DiseaseID": 27,
        "DiseaseName": "Grape leaf",
        "Symptoms": "Yellowing and spotting of leaves.",
        "Prevention": "Maintain proper airflow; avoid overcrowding.",
        "Treatment": "Apply fungicides if necessary."
    },
    {
        "DiseaseID": 28,
        "DiseaseName": "Grape leaf black rot",
        "Symptoms": "Brown spots with black margins on leaves.",
        "Prevention": "Use resistant varieties; prune infected parts.",
        "Treatment": "Apply fungicides like myclobutanil or mancozeb."
    }
]

def upgrade():
    # Insert data for each disease
    op.bulk_insert(disease_table, DISEASE_DATA)

def downgrade():
    # Delete the inserted data based on DiseaseIDs
    op.execute("DELETE FROM Disease WHERE DiseaseID BETWEEN 0 AND 28")
