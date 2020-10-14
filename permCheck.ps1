$ErrorActionPreference = 'SilentlyContinue'
#enter output file here
#todo: add an input option
$OutFile = ""
$Header = "Folder Path,IdentityReference,AccessControlType,IsInherited,InheritanceFlags,PropagationFlags"
Del $OutFile
Add-Content -Value $Header -Path $OutFile 
$RootPath = Read-Host "Input folder to check permissions of. UNC's fine"

#add -Recurse after 'dir' if you want the scan to get all the things 
$Folders = dir $RootPath | where {$_.psiscontainer -eq $true}

foreach ($Folder in $Folders){
	$ACLs = get-acl $Folder.fullname | ForEach-Object { $_.Access  }
	Foreach ($ACL in $ACLs){
	$OutInfo = $Folder.Fullname + "," + $ACL.IdentityReference  + "," + $ACL.AccessControlType + "," + $ACL.IsInherited + "," + $ACL.InheritanceFlags + "," + $ACL.PropagationFlags
	Add-Content -Value $OutInfo -Path $OutFile
	}}