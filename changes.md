```ahk
:Ro?:qul::0
:Ro?:qll::00
:Ro?:qlll::000
:Ro?:qull::00
:Ro?:qulll::000
```


```
SC00A:: {
    if A_ComputerName = 'Omen' {
        /*
        		powershell_exe := 'ahk_exe pwsh.exe'
        'powershell_path := "C:\Program Files\PowerShell\7\pwsh.exe"
        */
        powershell_exe := 'ahk_exe WindowsTerminal.exe'
        powershell_path := "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerShell\PowerShell 7 (x64)"
    } else if A_ComputerName = 'Laptop_Marijn' {
        powershell_exe := 'ahk_exe WindowsTerminal.exe'
        powershell_path := "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerShell\PowerShell 7 (x64)"
    }
```
```


```autohotkey
/*PGADMIN*/
#Hotif WinActive("ahk_exe pgAdmin4.exe")
:R?:selasfrom::SELECT * FROM
:R?:select::SELECT
:R?:from::FROM
:R?:as::AS
:R?:on::ON
:R?:truncate::TRUNCATE
:R?:delete::DELETE
:R?:cascade::CASCADE
:R?:stringagg::STRING_AGG
:R?:string_agg::STRING_AGG
:R?:constraint::CONSTRAINT
:R?:unique::UNIQUE
:R?:concat::CONCAT
:R?:null::NULL
:R?:default::DEFAULT
:R?:inner::INNER
:R?:left::LEFT
:R?:join::JOIN
:R?:where::WHERE
:R?:qgen::GENERATED ALWAYS AS IDENTITY PRIMARY KEY
#Hotif
```