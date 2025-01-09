# Ref reeds ingevuld?
if not record.default_code:
    # Haal categorie
    category = record.categ_id

    # Cat ingevuld?
    if category:
        # Zoek de hoofdcategorie in hiërarchie
        parent_category_name = category.complete_name or category.name  # Gebruik volledige naam voor hiërarchie

        # Controleer hoofdcategorie in de naam
        sequence_mapping = {
            'Kantoormateriaal': 'product_kantoormateriaal_sequence',
            'Afvalzakken': 'product_afvalzakken_sequence',
            'Medisch Materiaal': 'product_medisch_materiaal_sequence',
            'Onderhoudsproducten': 'product_onderhoudsproducten_sequence',
            'Toiletartikelen': 'product_toiletartikelen_sequence',
        }

        # Controleer of categorie in de mapping zit
        sequence_code = None
        for key, value in sequence_mapping.items():
            if key in parent_category_name:
                sequence_code = value
                break

        if sequence_code:
            # Genereer volgende nummer uit reeks
            new_ref = env['ir.sequence'].next_by_code(sequence_code)
            if new_ref:
                # schrijf ref weg
                record.write({'default_code': new_ref})

# Ref reeds ingevuld?
if record.default_code:
    return

# Haal categorie
category = record.categ_id
if not category:
    return

# Zoek de hoofdcategorie in hiërarchie
parent_category_name = category.complete_name or category.name  # Gebruik volledige naam voor hiërarchie

# Controleer hoofdcategorie in de naam
sequence_mapping = {
            'Kantoormateriaal': 'product_kantoormateriaal_sequence',
            'Afvalzakken': 'product_afvalzakken_sequence',
            'Medisch Materiaal': 'product_medisch_materiaal_sequence',
            'Onderhoudsproducten': 'product_onderhoudsproducten_sequence',
            'Toiletartikelen': 'product_toiletartikelen_sequence',
        }

# Controleer of categorie in de mapping zit
sequence_code = None
for key, value in sequence_mapping.items():
if key in parent_category_name:
    sequence_code = value
        break

    if sequence_code:
            # Genereer volgende nummer uit reeks
            new_ref = env['ir.sequence'].next_by_code(sequence_code)
            if new_ref:
                # schrijf ref weg
                record.write({'default_code': new_ref})

