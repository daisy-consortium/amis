; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "AMIS"
!define PRODUCT_VERSION "3.0 Beta 1"
!define PRODUCT_PUBLISHER "DAISY for All Project"
!define PRODUCT_WEB_SITE "http://amisproject.org"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\AMIS.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

; MUI 1.67 compatible ------
!include "MUI.nsh"

;SAPI page
!include "sapipage.nsh"

;Windows and DirectX versions
!include "getversions.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!insertmacro MUI_PAGE_LICENSE "lgpl.txt"
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
 
;this function is in the sapipage.nsh header
Page custom SapiPage
 
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\AMIS.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

; MUI end ------

;**********custom defines**********
;set the AMIS language pack code here (also the name of the language pack folder)
!define DEFAULT_LANGPACK "eng-US"

;this is the name of the language
!define LANG_NAME "U.S. English"

;this is the path to where the AMIS executable lives
!define BIN_DIR	"..\..\bin"

;this is the path to the logo file
!define LOGO_DIR "..\..\logo"

;this is the path to your windows system 32 directory
!define WIN32_DIR "c:\windows\system32"

;**********end custom defines*******

Name "${PRODUCT_NAME} ${PRODUCT_VERSION} (${LANG_NAME})"
;this is the name of the installer that gets created.  
;for some reason, i vaguely remember that it shouldn't have spaces in the filename.
OutFile "Setup-amis3-beta1-${DEFAULT_LANGPACK}.exe"
InstallDir "$PROGRAMFILES\AMIS"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Section "MainSection" SEC01

  SetOutPath "$INSTDIR"
  SetOverwrite try
  File "${BIN_DIR}\AMIS.exe"
  CreateDirectory "$SMPROGRAMS\AMIS"
  CreateShortCut "$SMPROGRAMS\AMIS\AMIS.lnk" "$INSTDIR\AMIS.exe"
  CreateShortCut "$DESKTOP\AMIS.lnk" "$INSTDIR\AMIS.exe"
  
  ;copy the DLLs
  File "${BIN_DIR}\libambulant_shwin32.dll"
  File "${BIN_DIR}\xerces-c_2_8.dll"
  File "${BIN_DIR}\libamplugin_pdtb.dll"
  File "${BIN_DIR}\PdtbIePlugin.dll"
  File "${BIN_DIR}\TransformSample.ax"
  
  ;copy the bookmark readme file
  SetOutPath "$INSTDIR\settings\bmk"
  File "${BIN_DIR}\settings\bmk\readme.txt"
  
  ;copy the default settings
  SetOutPath "$INSTDIR\settings"
  File "${BIN_DIR}\settings\amisPrefs.xml"
  File "${BIN_DIR}\settings\amisHistory.xml"
  File "${BIN_DIR}\settings\defaultToolbar.xml"
  File "${BIN_DIR}\settings\basicToolbar.xml"
  File "${BIN_DIR}\settings\resource.h.ini"
  
  ;copy the css files
  SetOutPath "$INSTDIR\settings\css"
  File "${BIN_DIR}\settings\css\*.css"
  SetOutPath "$INSTDIR\settings\css\customStyles"
  File "${BIN_DIR}\settings\css\customStyles\*.css"
  SetOutPath "$INSTDIR\settings\css\font"
  File "${BIN_DIR}\settings\css\font\*.css"
  
  ;copy the images
  SetOutPath "$INSTDIR\settings\img"
  File "${BIN_DIR}\settings\img\*.ico"
  SetOutPath "$INSTDIR\settings\img\defaultToolbar"
  File "${BIN_DIR}\settings\img\defaultToolbar\*.ico"
  SetOutPath "$INSTDIR\settings\img\basicToolbar"
  File "${BIN_DIR}\settings\img\basicToolbar\*.ico"
  
  
  ;copy a few default recordings, which give the version and release date
  SetOutPath "$INSTDIR\settings\lang"
  File "${BIN_DIR}\settings\lang\version.mp3"
  File "${BIN_DIR}\settings\lang\releasedate.mp3"
  
  ;copy the lang directory readme file
  SetOutPath "$INSTDIR\settings\lang"
  File "${BIN_DIR}\settings\lang\readme.txt"

  ;copy the MSVC redistributables exe
  SetOutPath ${INSTDIR}\temp
  ;TODO: make c:\program files a variable
  File "c:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\BootStrapper\Packages\vcredist_x86\vcredist_x86.exe"
	
	  
  ;TODO: ask the user if they want to change their registry to support Thai books
  ;TODO: if so, add this key in HKLM
  ;Software\Classes\MIME\Database\Charset\TIS-620 and set AliasForCharset to windows-874
   
SectionEnd

;******************************
;copy the files for the given langpack
Section -CopyDefaultLangpack
  
  ;copy the langpack root files
  SetOutPath "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}"
  File "${BIN_DIR}\settings\lang\${DEFAULT_LANGPACK}\*"
  
  ;copy the langpack audio
  SetOutPath "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\audio"
  File "${BIN_DIR}\settings\lang\${DEFAULT_LANGPACK}\audio\*"
  
  ;copy the langpack help book files (and images)
  SetOutPath "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\help"
  File "${BIN_DIR}\settings\lang\${DEFAULT_LANGPACK}\help\*"
  SetOutPath "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\help\img"
  File "${BIN_DIR}\settings\lang\${DEFAULT_LANGPACK}\help\img\*"
  
  ;copy the start book files
  SetOutPath "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\start"
  File "${BIN_DIR}\settings\lang\${DEFAULT_LANGPACK}\start\*"
 
 End:
SectionEnd

;************************
;make some icons
Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\AMIS\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\AMIS\Uninstall.lnk" "$INSTDIR\Uninstall-AMIS.exe"
SectionEnd

;*******************************
;post-install stuff
Section -Post
  WriteUninstaller "$INSTDIR\Uninstall-AMIS.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\AMIS.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\Uninstall-AMIS.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\AMIS.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
  
  Call RunMSVCRuntimeSetup

SectionEnd

;******************************
;install init
Function .onInit

	;load the sapi install screen file, as we may need it
	!insertmacro MUI_INSTALLOPTIONS_EXTRACT "sapipage.ini"
	!insertmacro MUI_INSTALLOPTIONS_EXTRACT "filebrowse.ini"

	;show the splash screen
	File /oname=$PLUGINSDIR\splash.bmp "${LOGO_DIR}\amis.bmp"
	splash::show 1000 $PLUGINSDIR\splash

	; $0 has '1' if the user closed the splash screen early,
	; '0' if everything closed normally, and '-1' if some error occurred.
	Pop $0 
			
	;check that the OS is XP, 2000, or Vista
	Call GetWindowsVersion
	Pop $R0

	CheckWinXP:
		StrCmp $R0 "XP" End CheckWin2K
	CheckWin2K:
		StrCmp $R0 "2000" End CheckVista
	CheckVista:
		StrCmp $R0 "Vista" End OSNotSupported

	;the OS is not supported; warn the user instead of aborting
	OSNotSupported:
		MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Warning: operating system not supported.  AMIS may not work.  Do you want to continue?" IDYES +2
		Abort

	;check for the directx version
	Call GetDXVersion
	Pop $R3
	IntCmp $R3 900 +3 0 +3
	MessageBox "MB_OK" "Requires DirectX 9.0 or later.  Aborting installation."
	Abort

End:
FunctionEnd

;**************************
;uninstall success
Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd

;**************************
;unintall init
Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd

;***************************
;uninstall process
Section Uninstall
;todo: backup bookmarks
  Delete "$INSTDIR\*"
  RMDir "$INSTDIR"
  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  Delete "$SMPROGRAMS\AMIS\AMIS.lnk" 
  Delete "$DESKTOP\AMIS.lnk" 
  SetAutoClose true
SectionEnd

;uninstall the default langpack
Section -un.CopyDefaultLangpack
	Delete "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\*"
  Delete "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\start\*"
  Delete "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\help\*"
  Delete "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\help\img\*"
  Delete "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\audio\*"
  
  RMDir "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\start"
  RMDir "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\help\img"
  RMDir "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\help"
  RMDir "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}\audio"
  RMDir "$INSTDIR\settings\lang\${DEFAULT_LANGPACK}"
SectionEnd


;*********************
;install the MSVC runtimes setup
Function RunMSVCRuntimeSetup
  Var /GLOBAL MSVC_RUNTIME_INSTALLER
	
  StrCpy $MSVC_RUNTIME_INSTALLER "$INSTDIR\temp\vcredist_x86.exe"
   
  ExecWait "$MSVC_RUNTIME_INSTALLER" $0
  StrCmp $0 "0" End Error
  Error:
    MessageBox MB_ICONEXCLAMATION "There was an error encountered while attempting to install the Microsoft runtime files.  Please download from http://www.microsoft.com/downloads/details.aspx?FamilyID=200B2FD9-AE1A-4A14-984D-389C36F85647&displaylang=en and install manually."
    Goto End
  End:
FunctionEnd