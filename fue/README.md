# fue
Firefox Universal Extension

This extension currently copies the address bar to the clipboard then runs youtube-dl with the link and downloads the audio of the video. The extension is shown with the chain link icon. The script will download audio only from video in the .m4a format. This is the ‘-f 140’ in the ps1 file. You can get a listing of available formats by opening a prompt and use the command ‘youtube-dl -F http://example-site.com/url’ This can be changed in the fue.ps1 in the popup folder to run any Powershell script. 

Setting the Powershell execution policy. This is so you can run the Powershell “.ps1” file on your computer. 
- Press and hold the Windows key on the keyboard and press X. A menu will popup, then click Windows Powershell (Admin). Click Yes to the UAC question to open the shell. You can check the current policy with ‘Get-ExecutionPolicy’ and set it with ‘Set-ExecutionPolicy’ and choose RemoteSigned or Unrestricted. RemoteSigned with allow you to run scripts you write on your computer and Unrestricted will allow any scripts, downloaded or created. If you would like to use RemoteSigned you can just copy the contents of fue.ps1 to a new file named the same and overwrite the original file. So type ‘Set-ExecutionPolicy RemoteSigned’ to run created scripts. 

I used Firefox Developers Edition for this project. You can set Firefox DE to open files with the excel content type flag to open with powershell. Type ‘file:///C:/pathtofiles’ the address bar and click the ‘runittest.xls’ file. Select open with and browse to C:\Windows\System32\WindowsPowerShell\v1.0\ and select ‘powershell.exe’ then select the option to always use the program to open the file type. Check XLS files are set to open with Powershell in the settings.
- *Note* You may choose a different filetype just go to https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types and choose a filetype then edit the html file in the popup folder. Some file types will not work as expected.

Load the extension into Firefox DE. At the address bar type ‘about:debugging’ click This Firefox and then Load Temporary Add-On. Browse to the downloaded files folder and open the manifest.json file. 
- *Note* I was able to permanently install the extension but it did not function correctly. 
It just downloaded the .ps1 file. I believe this is due to the xpi or zip file needed to install where the temporary add-on is in a folder not compressed. If you would like to attempt this add the key below to manifest.json after copying your own temporary id under on the debugging page and put it in for the “id” value. 
    "applications": {
            "gecko": {
              "strict_min_version": "54.0a1",
              "id": "07618bf39abe14b9fd829f008eb386ea82249cde@temporary-addon"
            }
          },


The downoad directory can be changed in the fue.ps1 file line 2. You can put a drive letter and path instead of the environmental variable. 

You should put a copy of youtube-dl.exe in the popup folder. https://github.com/ytdl-org/youtube-dl

(optional) I wrote a script to automate opening Firefox DE and loading the addon by double clicking the ‘runffdevpy.bat’ file(which you may safely rename.) You will likely need to edit the time.sleep commands to go along with how long it takes your computer to process each command in the ‘openffdev.py’ file.
