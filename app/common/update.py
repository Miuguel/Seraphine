import subprocess

bat = '''
# Wait for Seraphine.exe to exit
while ((Get-Process Seraphine -ErrorAction SilentlyContinue) -ne $null) {
    Write-Host "Seraphine is running, waiting..."
    Start-Sleep -Seconds 1
}

$fileList = Get-Content -Path "filelist.txt"

# Iterate through the file list
foreach ($file in $fileList) {
    # Check if the file or directory exists
    if (Test-Path -Path $file) {
        # Delete the file or directory
        Remove-Item -Path $file -Recurse -Force
        Write-Output "Removed: $file"
    } else {
        Write-Output "NotFound: $file"
    }
}

# Set the source path
$src = "$env:AppData\\Seraphine\\temp"

# Move directories
Get-ChildItem -Path $src -Directory | ForEach-Object {
    Move-Item -Path $_.FullName -Destination '.' -Force
}

# Move files
Get-ChildItem -Path $src -File | ForEach-Object {
    Move-Item -Path $_.FullName -Destination '.' -Force
}

# Delete the temporary folder used for update extraction
Remove-Item -Path $src -Recurse -Force

# Start the new version of Seraphine.exe
Start-Process -FilePath ".\Seraphine.exe" -NoNewWindow

# Delete the script file itself
Remove-Item -Path $MyInvocation.MyCommand.Definition -Force
'''



def runUpdater():
    with open("updater.ps1", 'w', encoding='utf-8') as f:
        f.write(bat)

    subprocess.Popen("PowerShell.exe -ExecutionPolicy Bypass -File updater.ps1")
