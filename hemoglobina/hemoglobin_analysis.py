# hemoglobin_analysis.py
# Análisis de la secuencia de la hemoglobina beta humana
# Este script:
# 1. Lee una secuencia de aminoácidos desde hemoglobin_clean.txt
# 2. Muestra información general de la secuencia
# 3. Cuenta la composición de aminoácidos
# 4. Calcula el peso molecular aproximado
# 5. Calcula el porcentaje de aminoácidos hidrofóbicos
# 6. Guarda los resultados en un archivo JSON

import json

# Nombre de la proteína
protein_name = "Hemoglobin subunit beta [Homo sapiens]"

# Leer la secuencia desde el archivo
with open("hemoglobina/hemoglobin_clean.txt", "r") as file:
    sequence = file.read().strip()

# Mostrar información básica
print("Nombre de la proteína:", protein_name)
print("Secuencia:")
print(sequence)
print("Longitud de la secuencia:", len(sequence))

# Lista de aminoácidos estándar
amino_acids = [
    "A", "R", "N", "D", "C",
    "E", "Q", "G", "H", "I",
    "L", "K", "M", "F", "P",
    "S", "T", "W", "Y", "V"
]

# Contar cuántas veces aparece cada aminoácido
amino_acid_count = {}

for aa in amino_acids:
    amino_acid_count[aa] = sequence.count(aa)

print("\nConteo de aminoácidos:")
for aa, count in amino_acid_count.items():
    print(f"{aa}: {count}")

# Diccionario con pesos moleculares aproximados de aminoácidos (Da)
amino_acid_weights = {
    "A": 89.09,
    "R": 174.20,
    "N": 132.12,
    "D": 133.10,
    "C": 121.15,
    "E": 147.13,
    "Q": 146.15,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "L": 131.17,
    "K": 146.19,
    "M": 149.21,
    "F": 165.19,
    "P": 115.13,
    "S": 105.09,
    "T": 119.12,
    "W": 204.23,
    "Y": 181.19,
    "V": 117.15
}

# Función reutilizable para calcular el peso molecular
def calculate_molecular_weight(seq, weights_dict):
    total_weight = 0

    for aa in seq:
        if aa in weights_dict:
            total_weight += weights_dict[aa]

    # Restar el peso del agua liberada en cada enlace peptídico
    if len(seq) > 1:
        total_weight -= (len(seq) - 1) * 18.015

    return total_weight

molecular_weight = calculate_molecular_weight(sequence, amino_acid_weights)

print("\nPeso molecular aproximado:", round(molecular_weight, 2), "Da")

# Aminoácidos hidrofóbicos
hydrophobic_amino_acids = ["A", "V", "I", "L", "M", "F", "W", "Y"]

hydrophobic_count = 0
for aa in sequence:
    if aa in hydrophobic_amino_acids:
        hydrophobic_count += 1

hydrophobic_percentage = (hydrophobic_count / len(sequence)) * 100

print("Cantidad de aminoácidos hidrofóbicos:", hydrophobic_count)
print("Porcentaje de aminoácidos hidrofóbicos:", round(hydrophobic_percentage, 2), "%")

# Guardar resultados en JSON
results = {
    "protein_name": protein_name,
    "sequence_length": len(sequence),
    "amino_acid_count": amino_acid_count,
    "molecular_weight": round(molecular_weight, 2),
    "hydrophobic_percentage": round(hydrophobic_percentage, 2)
}

with open("hemoglobin_results.json", "w") as json_file:
    json.dump(results, json_file, indent=4)

print("\nResultados guardados en hemoglobin_results.json")