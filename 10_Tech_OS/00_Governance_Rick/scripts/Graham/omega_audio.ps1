# Omega Audio Module - Strategic Status Signals (V1.1 - Fallback Edition)
# Author: Rick Supreme

$AudioDir = "C:\Aspace00\resources\audio"

function Play-SovereignSound {
    param([string]$SoundName)
    
    $SoundFile = "$AudioDir\$SoundName.wav"
    if (Test-Path $SoundFile) {
        $Player = New-Object System.Media.SoundPlayer
        $Player.SoundLocation = $SoundFile
        $Player.Play()
    } else {
        # Fallback to Windows System Sounds
        switch ($SoundName) {
            "success" { [System.Media.SystemSounds]::Asterisk.Play() }
            "alert"   { [System.Media.SystemSounds]::Hand.Play() }
            "notify"  { [System.Media.SystemSounds]::Exclamation.Play() }
            default   { [System.Media.SystemSounds]::Beep.Play() }
        }
    }
}
