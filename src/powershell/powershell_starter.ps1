# Definieer een lijst van getallen
$lijst = 2, 3, 4, 5

# Roep het Python-script aan en converteer JSON-output naar een PowerShell-hash
$json_result = python functions.py $lijst | ConvertFrom-Json

# Toon het resultaat
Write-Output "Resultaat als PowerShell hash:"
$json_result

# Definieer een lijst met woorden
$woorden = "Python", "PowerShell", "Script", "Automatisering"

# Roep het Python-script aan en converteer JSON-output naar een PowerShell-hash
$json_result = python script.py $woorden | ConvertFrom-Json

# Toon het resultaat
Write-Output "Resultaat als PowerShell hash:"
$json_result

# Toegang tot individuele waarden
Write-Output "`nVoorbeeld: lengte van 'Python' is $( $json_result.Python.lengte )"

# Definieer een lijst met woorden
$woorden = "Python", "PowerShell", "Script", "Automatisering"

# Roep het Python-script aan en converteer JSON-output naar een PowerShell-hash
$json_result = python script2.py $woorden | ConvertFrom-Json

# Toon het resultaat
Write-Output "Resultaat als PowerShell hash:"
$json_result

# Toegang tot individuele waarden
Write-Output "`nVoorbeeld: lengte van 'Python' is $( $json_result.Python.lengte )"
Write-Output "Voorbeeld: 'PowerShell' omgekeerd is $( $json_result.PowerShell.omgekeerd )"