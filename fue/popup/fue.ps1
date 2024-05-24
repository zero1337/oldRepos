$cb = Get-Clipboard
$args = "-f 140 -o %USERPROFILE%/Music/%(title)s.%(ext)s $cb"
$ytdl = 'youtube-dl.exe'
Start-Process $ytdl -ArgumentList $args
