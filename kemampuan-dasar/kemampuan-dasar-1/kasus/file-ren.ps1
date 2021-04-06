$Folder = 'D:\Files\Git\praxis-academy\kemampuan-dasar\kemampuan-dasar-1'
$ChildItem = Get-ChildItem $Folder -Filter *.java -Recurse | % { $_.Fullname }
$ExistFiles = Test-Path $ChildItem -IsValid
# $ExistFiles
Foreach ($Item in $ChildItem) {
	"`n"
	Write-Host 'There are .java files in: '
	$Item
	"`n"
	If ($ExistFiles -eq $True) {
		$Promp_rename = Read-Host "Do you want to rename the file? [Y] Yes, [N] No"
		If ($Promp_rename -eq "y") {
			"`n"
			$New_name = Read-Host "Input new name"
			Rename-Item $Item -NewName "$new_name.java"
		}
	}
}



