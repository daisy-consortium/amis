#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1342740194.778917
__CHEETAH_genTimestamp__ = 'Thu Jul 19 16:23:14 2012'
__CHEETAH_src__ = 'SetupAmis3NsiTemplate.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jul 19 16:22:58 2012'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class SetupAmis3NsiTemplate(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(SetupAmis3NsiTemplate, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u''';******\r
; Usage:\r
; makensis /DCUSTOM_LANG_NAME="language name" /DCUSTOM_LANG_ID="lang-code" /DCUSTOM_HELP help_file.html setup-amis3.nsi\r
;\r
; example:\r
; makensis /DCUSTOM_LANG_NAME="U.S. English" /DCUSTOM_LANG_ID="eng-US" /DCUSTOM_HELP="amishelp.html" setup-amis3.nsi\r
;\r
;/DCUSTOM_LANG_NAME = Identifies the installer EXE and the name of the product during installation\r
;/DCUSTOM_LANG_ID = The language pack identifier.  If other than "eng-US", both the custom and default language packs are included\r
;/DCUSTOM_HELP = The name of the help file for the custom language pack.\r
;**\r
\r
;******\r
; product information\r
;**\r
!define PRODUCT_NAME "AMIS"\r
!define PRODUCT_VERSION "3.1.4 beta"\r
!define PRODUCT_PUBLISHER "DAISY Consortium"\r
!define PRODUCT_WEB_SITE "http://daisy.org/amis"\r
!define PRODUCT_DIR_REGKEY "Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\AMIS.exe"\r
!define PRODUCT_UNINST_KEY "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${PRODUCT_NAME}"\r
!define PRODUCT_UNINST_ROOT_KEY "HKLM"\r
\r
\r
;******\r
; pages, components, and script includes\r
;**\r
\r
!include "Registry.nsh"\r
!include WinVer.nsh\r
\r
; required for InstallLib\r
!include "Library.nsh"\r
\r
; MUI 1.67 compatible ------\r
!include "MUI.nsh"\r
\r
; Support for conditional logic (should be in c:\\program files\\nsis\\include by default)\r
!include "LogicLib.nsh"\r
\r
;Windows and DirectX versions\r
!include "..\\main\\getversions.nsh"\r
!include "WinVer.nsh"\r
\r
; MUI Settings\r
!define MUI_ABORTWARNING\r
!define MUI_ICON "${NSISDIR}\\Contrib\\Graphics\\Icons\\modern-install.ico"\r
!define MUI_UNICON "${NSISDIR}\\Contrib\\Graphics\\Icons\\modern-uninstall.ico"\r
\r
; Welcome page\r
!insertmacro MUI_PAGE_WELCOME\r
\r
; License page\r
!insertmacro MUI_PAGE_LICENSE "lgpl.txt"\r
\r
; Directory page\r
!insertmacro MUI_PAGE_DIRECTORY\r
 \r
; Instfiles page\r
!insertmacro MUI_PAGE_INSTFILES\r
\r
; Finish page\r
!define MUI_FINISHPAGE_RUN "$INSTDIR\\AMIS.exe"\r
!insertmacro MUI_PAGE_FINISH\r
\r
; Uninstaller pages\r
!insertmacro MUI_UNPAGE_INSTFILES\r
\r
; Language files\r
!insertmacro MUI_LANGUAGE "''')
        _v = VFFSL(SL,"nsis_language",True) # u'$nsis_language' on line 70, col 28
        if _v is not None: write(_filter(_v, rawExpr=u'$nsis_language')) # from line 70, col 28.
        write(u'''"\r
\r
; MUI end ------\r
\r
;******\r
; custom defines\r
;**\r
;this is the path to where the AMIS executable lives\r
!define BIN_DIR\t"..\\..\\bin"\r
\r
;this is the path to the logo file\r
!define LOGO_DIR "..\\..\\logo"\r
\r
;the default language setting\r
!define DEFAULT_LANG_ID "eng-US"\r
!define DEFAULT_LANG_NAME "''')
        _v = VFFSL(SL,"text123",True) # u'$text123' on line 85, col 28
        if _v is not None: write(_filter(_v, rawExpr=u'$text123')) # from line 85, col 28.
        write(u'''"\r
\r
;this is the path to your windows system 32 directory\r
!define WIN32_DIR "c:\\windows\\system32"\r
\r
;this is the path to your Application Data directory\r
!define LOCAL_APP_DATA "C:\\Documents and Settings\\All Users\\Application Data"\r
\r
;this is the path to your Visual Studio redistributables directory\r
!define VS_DIR "C:\\Program Files\\Microsoft Visual Studio 8\\SDK\\v2.0\\BootStrapper\\Packages\\vcredist_x86"\r
\r
;******\r
; directory, installer exe name, etc\r
;**\r
Name "${PRODUCT_NAME} ${PRODUCT_VERSION} (${CUSTOM_LANG_NAME})"\r
;this is the name of the installer that gets created.  \r
OutFile "..\\build\\Setup-amis-${CUSTOM_LANG_NAME}.exe"\r
InstallDir "$PROGRAMFILES\\AMIS"\r
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""\r
ShowInstDetails show\r
ShowUnInstDetails show\r
\r
;******\r
; installer init\r
;**\r
Function .onInit\r
    SetOutPath "$INSTDIR"\r
    \r
    LogEx::Init true "$INSTDIR\\install.log"\r
    LogEx::Write "${PRODUCT_NAME} ${PRODUCT_VERSION} (${CUSTOM_LANG_NAME})"  \r
    \t\r
\t;show the splash screen\r
\tFile /oname=$PLUGINSDIR\\splash.bmp "${LOGO_DIR}\\amis.bmp"\r
\tsplash::show 1000 $PLUGINSDIR\\splash\r
\tPop $0 \r
\r
    ; the recommendation is at least WinXP SP3\r
    ${If} ${AtLeastWinXP}\r
      ${AndIf} ${AtLeastServicePack} 3\r
      ${OrIf} ${AtLeastWinVista}\r
          LogEx::Write "Using Windows XP SP3 or higher"\r
          Goto DxCheck\r
      \r
    ; XP SP2 is acceptable but not as good as SP3\r
    ${ElseIf} ${AtLeastWinXP}\r
      ${AndIf} ${AtMostWinXP}\r
      ${AndIf} ${AtMostServicePack} 2\r
      ${AndIf} ${AtLeastServicePack} 2\r
         LogEx::Write "Using Windows XP SP2, warning user"\r
\t\t IfSilent DxCheck\r
         MessageBox MB_OK "''')
        _v = VFFSL(SL,"text101",True) # u'$text101' on line 135, col 28
        if _v is not None: write(_filter(_v, rawExpr=u'$text101')) # from line 135, col 28.
        write(u'''"\r
         Goto DxCheck\r
         \r
    ; Other versions of windows are unsupported  \r
    ; (though Win2K SP4 and various 64 bit versions of windows might work, they have not been tested at this time)\r
    ; so give the user a chance to abort installation\r
    ${Else}\r
          ;find out exactly which OS version was detected\r
          Push $R0\r
          Call GetWindowsVersion\r
          Pop $R0\r
          LogEx::Write "Operating system not supported.  $R0"\r
\t\t  IfSilent DxCheck\r
          MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "''')
        _v = VFFSL(SL,"text102",True) # u'$text102' on line 148, col 62
        if _v is not None: write(_filter(_v, rawExpr=u'$text102')) # from line 148, col 62.
        write(u'''" IDYES DxCheck\r
          LogEx::Write "User chose to abort installation (wrong OS)"\r
          Abort\r
      ${EndIf}\r
        \r
DxCheck:\r
    ;check for the directx version\r
    Call GetDXVersion\r
    Pop $0\r
    LogEx::Write "DirectX version $0"\r
    ${If} $0 < 900\r
      LogEx::Write "Warning user, wrong DX version"\r
      IfSilent IeCheck\r
      MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "''')
        _v = VFFSL(SL,"text103",True) # u'$text103' on line 161, col 58
        if _v is not None: write(_filter(_v, rawExpr=u'$text103')) # from line 161, col 58.
        write(u'''" IDYES IeCheck\r
      LogEx::Write "User chose to abort installation"\r
      Abort  \r
    ${EndIf}\r
    \r
IeCheck:\r
    ;check for IE version 7 or higher\r
    Call GetIEVersion\r
    Pop $0\r
    LogEx::Write "IE version $0"\r
    ${If} $0 == 6.00\r
        LogEx::Write "Warning user about IE6"\r
\t\tIfSilent End\r
        MessageBox MB_OK "''')
        _v = VFFSL(SL,"text104",True) # u'$text104' on line 174, col 27
        if _v is not None: write(_filter(_v, rawExpr=u'$text104')) # from line 174, col 27.
        write(u'''"\r
    ${ElseIf} $0 < 6\r
        LogEx::Write "Warning user about IE version $0"\r
        IfSilent End\r
        MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "''')
        _v = VFFSL(SL,"text105",True) # u'$text105' on line 178, col 60
        if _v is not None: write(_filter(_v, rawExpr=u'$text105')) # from line 178, col 60.
        write(u'''" IDYES End\r
        LogEx::Write "User chose to abort (wrong IE version)"\r
        Abort\r
    ${EndIf}\r
End:\r
FunctionEnd\r
\r
;******\r
; copy all files, register DLLs, etc\r
;**\r
Section "MainSection" SEC01\r
\t;the settings dir will live here\r
    Var /GLOBAL SETTINGS_DIR\r
\t; the MSVC Redist temporary directory\r
\tVar /GLOBAL AMIS_TEMP\r
\t\r
    ;figure out the user\'s application data directore\r
    ;look for the "all users" context\r
    SetShellVarContext all\r
    StrCpy $SETTINGS_DIR $APPDATA\\AMIS\\settings\r
\r
\t; create a temp directory that\'s different than the default\r
\t; many windows machines put the default temp directory under the user\'s own path (including their username)\r
\t; and -- many users have non-ascii names, which can be problematic for some 3rd party installers\r
\t; get the drive letter for the windows drive\r
\tStrCpy $R0 $WINDIR 1\r
\tStrCpy $AMIS_TEMP "$R0:\\amistemp"\r
\tCreateDirectory $AMIS_TEMP\r
\r
    LogEx::Write "Installing AMIS in $INSTDIR"\r
    LogEx::Write "Installing AMIS settings in $SETTINGS_DIR"\r
    \r
    SetOutPath "$INSTDIR"\r
    SetOverwrite try\r
    File "${BIN_DIR}\\AMIS.exe"\r
    CreateDirectory "$SMPROGRAMS\\AMIS"\r
    CreateShortCut "$SMPROGRAMS\\AMIS\\AMIS.lnk" "$INSTDIR\\AMIS.exe"\r
    CreateShortCut "$DESKTOP\\AMIS.lnk" "$INSTDIR\\AMIS.exe"\r
  \r
    ;this creates a subdir in the start menu that will contain our modified shortcuts for compatibility/debug modes\r
    CreateDirectory "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text114",True) # u'$text114' on line 218, col 48
        if _v is not None: write(_filter(_v, rawExpr=u'$text114')) # from line 218, col 48.
        write(u'''"\r
    CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text114",True) # u'$text114' on line 219, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$text114')) # from line 219, col 47.
        write(_filter("\\"))
        _v = VFFSL(SL,"text115",True) # u'$text115' on line 219, col 64
        if _v is not None: write(_filter(_v, rawExpr=u'$text115')) # from line 219, col 64.
        write(_filter(".lnk"))
        write(u'''" "$INSTDIR\\AMIS.exe" "-prefs amisPrefsDebug.xml"\r
    CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text114",True) # u'$text114' on line 220, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$text114')) # from line 220, col 47.
        write(_filter("\\"))
        _v = VFFSL(SL,"text116",True) # u'$text116' on line 220, col 64
        if _v is not None: write(_filter(_v, rawExpr=u'$text116')) # from line 220, col 64.
        write(_filter(".lnk"))
        write(u'''" "$INSTDIR\\AMIS.exe" "-prefs amisPrefsCompatibilityMode.xml"\r
    CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text114",True) # u'$text114' on line 221, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$text114')) # from line 221, col 47.
        write(_filter("\\"))
        _v = VFFSL(SL,"text117",True) # u'$text117' on line 221, col 64
        if _v is not None: write(_filter(_v, rawExpr=u'$text117')) # from line 221, col 64.
        write(_filter(".lnk"))
        write(u'''" "$INSTDIR\\AMIS.exe" "-prefs amisPrefsCompatibilityModeWithDX.xml"\r
    CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text114",True) # u'$text114' on line 222, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$text114')) # from line 222, col 47.
        write(_filter("\\"))
        _v = VFFSL(SL,"text118",True) # u'$text118' on line 222, col 64
        if _v is not None: write(_filter(_v, rawExpr=u'$text118')) # from line 222, col 64.
        write(_filter(".lnk"))
        write(u'''" "$INSTDIR\\AMIS.exe" "-prefs amisPrefsCompatibilityModeWithTTS.xml"\r
    \r
    ;copy the DLLs\r
    File "${BIN_DIR}\\libambulant_shwin32.dll"\r
    File "${BIN_DIR}\\xerces-c_3_0.dll"\r
    File "${BIN_DIR}\\TransformSample.ax"\r
    File "${BIN_DIR}\\libamplugin_ffmpeg.dll"\r
    File "${BIN_DIR}\\avformat-52.dll"\r
    File "${BIN_DIR}\\avcodec-51.dll"\r
    File "${BIN_DIR}\\avutil-49.dll"\r
    File "${BIN_DIR}\\SDL.dll"\r
    File "${BIN_DIR}\\libamplugin_pdtb.dll"\r
    File "${BIN_DIR}\\lzop.exe"\r
    File "${BIN_DIR}\\IeDtbPlugin.dll"\r
    \r
    ;copy the xslt and stylesheet jar files\r
    SetOutPath "$INSTDIR\\xslt"\r
    File "${BIN_DIR}\\xslt\\org.daisy.util.jar"\r
    File "${BIN_DIR}\\xslt\\saxon8.jar"\r
    File "${BIN_DIR}\\xslt\\stax-api-1.0.1.jar"\r
    File "${BIN_DIR}\\xslt\\wstx-lgpl-3.2.8.jar"\r
    \r
    SetOutPath "$INSTDIR\\xslt\\dtbook"\r
    File "${BIN_DIR}\\xslt\\dtbook\\dtbook2xhtml.xsl"\r
    \r
    SetOutPath "$INSTDIR\\xslt\\l10n"\r
    File "${BIN_DIR}\\xslt\\l10n\\l10n.xsl"\r
    \r
    ;register the timescale ocx component\r
    LogEx::Write "Registering TransformSample.ax"\r
    ExecWait \'regsvr32.exe /s "$INSTDIR\\TransformSample.ax"\'\r
    \r
    ;copy the bookmark readme file\r
    SetOutPath "$SETTINGS_DIR\\bmk"\r
    File "${BIN_DIR}\\settings\\bmk\\readme.txt"\r
  \r
    ;copy the default settings\r
    SetOutPath "$SETTINGS_DIR"\r
    ;the prefs files were generated by the setup_prefs script (called before this install script was called)\r
    File "${BIN_DIR}\\settings\\clean_settings_for_the_installer\\amisPrefs.xml"\r
    File "${BIN_DIR}\\settings\\clean_settings_for_the_installer\\amisPrefsCompatibilityMode.xml"\r
    File "${BIN_DIR}\\settings\\clean_settings_for_the_installer\\amisPrefsCompatibilityModeWithDX.xml"\r
    File "${BIN_DIR}\\settings\\clean_settings_for_the_installer\\amisPrefsCompatibilityModeWithTTS.xml"\r
    File "${BIN_DIR}\\settings\\clean_settings_for_the_installer\\amisPrefsDebug.xml"\r
    \r
    ;preserve the history file if exists\r
    ${IfNot} ${FileExists} "$SETTINGS_DIR\\amisHistory.xml"\r
        File "${BIN_DIR}\\settings\\clean_settings_for_the_installer\\amisHistory.xml"\r
    ${EndIf}\r
\r
    File "${BIN_DIR}\\settings\\defaultToolbar.xml"\r
    File "${BIN_DIR}\\settings\\basicToolbar.xml"\r
    File "${BIN_DIR}\\settings\\amisHistory.xml.default"\r
    File "${BIN_DIR}\\settings\\clearHistory.bat"\r
    File "${BIN_DIR}\\settings\\clearCache.bat"\r
  \r
    ;update file permissions so that any user can run AMIS\r
    AccessControl::GrantOnFile "$SETTINGS_DIR\\bmk" "(BU)" "FullAccess"\r
    AccessControl::GrantOnFile "$SETTINGS_DIR" "(BU)" "FullAccess"\r
    \r
    File "${LOCAL_APP_DATA}\\AMIS\\settings\\resource.h.ini"\r
  \r
    ;copy the css files\r
    SetOutPath "$SETTINGS_DIR\\css"\r
    File "${BIN_DIR}\\settings\\css\\*.css"\r
    SetOutPath "$SETTINGS_DIR\\css\\customStyles"\r
    File "${BIN_DIR}\\settings\\clean_settings_for_the_installer\\customStyles\\*.css"\r
    SetOutPath "$SETTINGS_DIR\\css\\font"\r
    File "${BIN_DIR}\\settings\\css\\font\\*.css"\r
    SetOutPath "$SETTINGS_DIR\\css\\font\\ie8"\r
    File "${BIN_DIR}\\settings\\css\\font\\ie8\\*.css"\r
    \r
    ;copy the images\r
    SetOutPath "$SETTINGS_DIR\\img"\r
    File "${BIN_DIR}\\settings\\img\\*.ico"\r
    SetOutPath "$SETTINGS_DIR\\img\\defaultToolbar"\r
    File "${BIN_DIR}\\settings\\img\\defaultToolbar\\*.ico"\r
    SetOutPath "$SETTINGS_DIR\\img\\basicToolbar"\r
    File "${BIN_DIR}\\settings\\img\\basicToolbar\\*.ico"\r
  \r
    ;copy the lang directory readme file\r
    SetOutPath "$SETTINGS_DIR\\lang"\r
    File "${BIN_DIR}\\settings\\lang\\readme.txt"\r
\r
    ;copy the MSVC redistributables installer\r
    SetOutPath $AMIS_TEMP\r
    File "${VS_DIR}\\vcredist_x86.exe"\r
  \r
    ;copy the jaws scripts installer\r
    SetOutPath $AMIS_TEMP\r
    File "${BIN_DIR}\\amis3_jfw_scripts.exe"\r
  \r
    ;to support Thai encoding, add this key in HKLM\r
    ;Software\\Classes\\MIME\\Database\\Charset\\TIS-620 and set AliasForCharset to windows-874\r
    WriteRegStr HKLM "Software\\Classes\\MIME\\Database\\Charset\\TIS-620" "AliasForCharset" "Windows-874"\r
    LogEx::Write "Registered charset alias Windows-874 for TIS-620"\r
    \r
\t;remove keys - the formatting has changed between this version and the last one\r
\tDeleteRegKey HKCU "Software\\Amis\\AMIS\\UAKs"\r
\t\r
SectionEnd\r
\r
;******\r
; copy the default (eng-US) and custom (if different) language packs\r
;*\r
Section -CopyLangpacks\r
  \r
    LogEx::Write "Copying default language pack files: ${DEFAULT_LANG_ID}"\r
    \r
    ;***\r
    ;copy the default langpack\r
    ;***\r
    ;copy the langpack root files\r
    SetOutPath "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}"\r
    File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${DEFAULT_LANG_ID}\\*"\r
\r
    ;copy the langpack audio\r
    SetOutPath "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\audio"\r
    File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${DEFAULT_LANG_ID}\\audio\\*"\r
\r
    ;copy the langpack help book files (and images)\r
    SetOutPath "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\help"\r
    File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${DEFAULT_LANG_ID}\\help\\*"\r
    SetOutPath "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\help\\img"\r
    File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${DEFAULT_LANG_ID}\\help\\img\\*"\r
\r
    ;copy the langpack shortcut book files\r
    SetOutPath "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\shortcuts"\r
    File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${DEFAULT_LANG_ID}\\shortcuts\\*"\r
\r
    ;***\r
    ; copy the custom langpack\r
    ;***\r
    ${If} ${CUSTOM_LANG_ID} != "eng-US"\r
        LogEx::Write "Copying custom language pack files ${CUSTOM_LANG_ID}"\r
        \r
        ;copy the langpack root files\r
        SetOutPath "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}"\r
        File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${CUSTOM_LANG_ID}\\*"\r
\r
        ;copy the langpack audio\r
        SetOutPath "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\audio"\r
        File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${CUSTOM_LANG_ID}\\audio\\*"\r
\r
        ;copy the langpack help book files (and images)\r
        SetOutPath "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\help"\r
        File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${CUSTOM_LANG_ID}\\help\\*"\r
        SetOutPath "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\help\\img"\r
        File /nonfatal "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${CUSTOM_LANG_ID}\\help\\img\\*"  \r
        ;copy the langpack shortcut book files\r
        SetOutPath "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\shortcuts"\r
        File "${LOCAL_APP_DATA}\\AMIS\\settings\\lang\\${CUSTOM_LANG_ID}\\shortcuts\\*"\r
    ${EndIf}\r
    \r
End:\r
SectionEnd\r
\r
;******\r
; Install MSVC runtime\r
;*\r
Section -MSVCRuntime\r
  \r
    Var /GLOBAL MSVC_RUNTIME_INSTALLER\r
\t\r
    StrCpy $MSVC_RUNTIME_INSTALLER "$AMIS_TEMP\\vcredist_x86.exe"\r
    LogEx::Write "MSVC Runtime Installer copied to temp dir $AMIS_TEMP"\r
    \r
    ;check and see if the user needs these files\r
    ${registry::KeyExists} "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{7299052B-02A4-4627-81F2-1818DA5D550D}" $0\r
    \r
    ${If} $0 == 0\r
        LogEx::Write "MSVC Runtime already installed on this machine"\r
    ${Else}\r
        LogEx::Write "Attempting to install MSVC Runtime"\r
        ExecWait "$MSVC_RUNTIME_INSTALLER" $0\r
        \r
        ${If} $0 != "0"\r
            LogEx::Write "Error installing MSVC Runtime"\r
\t\t\tIfSilent End\r
            MessageBox MB_ICONEXCLAMATION "''')
        _v = VFFSL(SL,"text106",True) # u'$text106' on line 401, col 44
        if _v is not None: write(_filter(_v, rawExpr=u'$text106')) # from line 401, col 44.
        write(u'''"\r
        ${Else}\r
            LogEx::Write "MSVC Runtime installed successfully"\r
        ${EndIf}\r
    ${EndIf}\r
    \r
End:\r
    Delete "$MSVC_RUNTIME_INSTALLER"\r
SectionEnd\r
\r
''')
        if VFFSL(SL,"include_jaws_scripts",True) == "yes": # generated from line 411, col 1
            write(u'''\r
;******\r
; Install Jaws scripts\r
;*\r
Section -JawsScripts\r
  \r
    Var /GLOBAL JFW_SCRIPTS_INSTALLER\r
    StrCpy $JFW_SCRIPTS_INSTALLER "$AMIS_TEMP\\amis3_jfw_scripts.exe"\r
    LogEx::Write "Jaws Scripts Installer copied to temp dir $AMIS_TEMP"\r
    \r
    ; check if the user has jaws installed, then ask if they want to install the scripts\r
    ${registry::KeyExists} "HKEY_CURRENT_USER\\SOFTWARE\\Freedom Scientific\\JAWS" $0\r
    \r
    ${If} $0 == 0\r
        LogEx::Write "JAWS found on this machine"\r
        \r
\t\t; default for silent installation is "yes" for jaws scripts installation\r
\t\tIfSilent InstallScripts\r
        MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON1 "''')
            _v = VFFSL(SL,"text107",True) # u'$text107' on line 430, col 60
            if _v is not None: write(_filter(_v, rawExpr=u'$text107')) # from line 430, col 60.
            write(u'''" IDYES InstallScripts IDNO DoNotInstallScripts\r
\r
    InstallScripts:\r
        LogEx::Write "Attempting to install JAWS scripts"\r
        ExecWait "$JFW_SCRIPTS_INSTALLER" $0\r
        \r
        ${If} $0 != "0"\r
            LogEx::Write "Error installing JAWS scripts"\r
\t\t\tIfSilent End\r
            MessageBox MB_ICONEXCLAMATION "''')
            _v = VFFSL(SL,"text108",True) # u'$text108' on line 439, col 44
            if _v is not None: write(_filter(_v, rawExpr=u'$text108')) # from line 439, col 44.
            write(u'''"\r
        ${EndIf}\r
        Goto End\r
    \r
    DoNotInstallScripts:\r
        LogEx::Write "User declined JAWS scripts installation"\r
        Goto End\r
    \r
    ${Else}\r
        LogEx::Write "JAWS not found on this machine."\r
\t\tGoto End\r
    ${EndIf}\r
\r
End:\r
    Delete "$JFW_SCRIPTS_INSTALLER"\r
SectionEnd\r
''')
        else: # generated from line 455, col 1
            write(u'''Section -JawsScripts\r
 \t;don\'t install jaws scripts, just delete the exe\r
\tVar /GLOBAL JFW_SCRIPTS_INSTALLER\r
\tStrCpy $JFW_SCRIPTS_INSTALLER "$AMIS_TEMP\\amis3_jfw_scripts.exe"\r
\tDelete "$JFW_SCRIPTS_INSTALLER"\r
SectionEnd\r
''')
        write(u'''\r
;******\r
; Check if Java is installed\r
;*\r
Section -JavaCheck\r
\r
    ${registry::KeyExists} "HKEY_LOCAL_MACHINE\\SOFTWARE\\JavaSoft\\Java Runtime Environment" $0\r
    \r
    ${If} $0 == 0\r
        ${registry::Read} "HKEY_LOCAL_MACHINE\\SOFTWARE\\JavaSoft\\Java Runtime Environment" "CurrentVersion" $R0 $R1\r
    \r
        StrCmp $R0 "1.6" CorrectVersion Check17\r
        \r
        Check17:\r
            StrCmp $R0 "1.7" CorrectVersion IncorrectVersion\r
\t\tCorrectVersion:\r
            LogEx::Write "Correct Java version installed ($R0)"\r
\t\t\tGoto End\r
\t\tIncorrectVersion:\r
\t\t\tLogEx::Write "Incorrect Java version ($R0)"\r
\t\t\tIfSilent End\r
        \tMessageBox MB_OK "''')
        _v = VFFSL(SL,"text109",True) # u'$text109' on line 484, col 28
        if _v is not None: write(_filter(_v, rawExpr=u'$text109')) # from line 484, col 28.
        write(u'''"\r
        \tGoto End\r
    ${Else}\r
        LogEx::Write "Java not found"\r
\t\tIfSilent End\r
        MessageBox MB_OK "''')
        _v = VFFSL(SL,"text110",True) # u'$text110' on line 489, col 27
        if _v is not None: write(_filter(_v, rawExpr=u'$text110')) # from line 489, col 27.
        write(u'''"\r
\t\tGoto End\r
    ${EndIf}\r
End:\r
SectionEnd\r
\r
;******\r
; Create shortcuts and icons\r
;*\r
Section -AdditionalIcons\r
    WriteIniStr "$INSTDIR\\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"\r
    CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text119",True) # u'$text119' on line 500, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$text119')) # from line 500, col 47.
        write(_filter(".lnk"))
        write(u'''" "$INSTDIR\\${PRODUCT_NAME}.url"\r
    CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text120",True) # u'$text120' on line 501, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$text120')) # from line 501, col 47.
        write(_filter(".lnk"))
        write(u'''" "$INSTDIR\\Uninstall-AMIS.exe"\r
    ${If} ${CUSTOM_LANG_ID} != "eng-US"\r
        CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text121",True) # u'$text121' on line 503, col 51
        if _v is not None: write(_filter(_v, rawExpr=u'$text121')) # from line 503, col 51.
        write(u''' (${CUSTOM_LANG_NAME}).lnk" "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\help\\${CUSTOM_HELP}"\r
        CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text122",True) # u'$text122' on line 504, col 51
        if _v is not None: write(_filter(_v, rawExpr=u'$text122')) # from line 504, col 51.
        write(u''' (${CUSTOM_LANG_NAME}).lnk" "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\shortcuts\\amiskeys.html"\r
    ${EndIf}\r
    CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text121",True) # u'$text121' on line 506, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$text121')) # from line 506, col 47.
        write(u''' (${DEFAULT_LANG_NAME}).lnk" "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\help\\amishelp.html"\r
    CreateShortCut "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text122",True) # u'$text122' on line 507, col 47
        if _v is not None: write(_filter(_v, rawExpr=u'$text122')) # from line 507, col 47.
        write(u''' (${DEFAULT_LANG_NAME}).lnk" "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\shortcuts\\amiskeys.html"\r
SectionEnd\r
\r
;******\r
; write unintaller and registry strings\r
; check if we need to install the msvc runtimes\r
;**\r
Section -Post\r
\r
    ;register the pdtb-ie plugin\r
    LogEx::Write "Installing IeDtbPlugin"\r
    ExecWait \'regsvr32.exe /s "$INSTDIR\\IeDtbPlugin.dll"\'    \r
    \r
\r
    WriteUninstaller "$INSTDIR\\Uninstall-AMIS.exe"\r
    WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\\AMIS.exe"\r
    WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"\r
    WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\\Uninstall-AMIS.exe"\r
    WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\\AMIS.exe"\r
    WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"\r
    WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"\r
    WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"\r
    \r
    LogEx::Write "Summary of files:"\r
    LogEx::Write ""\r
    ExecDos::exec \'cmd /C dir "$INSTDIR" /b/s/l/a\' "" "$INSTDIR\\output.log"\r
    LogEx::AddFile "   >" "$INSTDIR\\output.log"\r
\r
    LogEx::Write ""\r
    ExecDos::exec \'cmd /C dir "$SETTINGS_DIR" /b/s/l/a\' "" "$INSTDIR\\output.log"\r
    LogEx::AddFile "   >" "$INSTDIR\\output.log"\r
    \r
    LogEx::Close\r
    \r
    Delete $INSTDIR\\output.log\r
\tRMDir "$AMIS_TEMP"\r
SectionEnd\r
\r
\r
;******\r
; uninstall init\r
;**\r
Function un.onInit\r
\tIfSilent End\r
    MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "''')
        _v = VFFSL(SL,"text111",True) # u'$text111' on line 551, col 56
        if _v is not None: write(_filter(_v, rawExpr=u'$text111')) # from line 551, col 56.
        write(u'''" IDYES End\r
    Abort\r
End:\r
FunctionEnd\r
\r
;******\r
; uninstall complete\r
;**\r
Function un.onUninstSuccess\r
    HideWindow\r
\tIfSilent End\r
    MessageBox MB_ICONINFORMATION|MB_OK "''')
        _v = VFFSL(SL,"text112",True) # u'$text112' on line 562, col 42
        if _v is not None: write(_filter(_v, rawExpr=u'$text112')) # from line 562, col 42.
        write(u'''"\r
End:\r
FunctionEnd\r
\r
\r
;******\r
;uninstall process\r
;**\r
Section Uninstall\r
\r
\t;figure out the user\'s application data directory\r
\t;look for the "all users" context\r
\tSetShellVarContext all \r
\tStrCpy $SETTINGS_DIR $APPDATA\\AMIS\\settings\r
\t\r
\t; unregister the timescale ocx component\r
\t; this works on both XP and Vista\r
    ExecWait \'regsvr32.exe /u /s "$INSTDIR\\TransformSample.ax"\'\r
    ; unregister the pdtb dll\r
    !insertmacro UnInstallLib REGDLLTLB NOTSHARED NOREBOOT_NOTPROTECTED "$INSTDIR\\IeDtbPlugin.dll"\r
  \r
\tDelete "$SETTINGS_DIR\\css\\*"\r
\tDelete "$SETTINGS_DIR\\css\\font\\*"\r
    Delete "$SETTINGS_DIR\\css\\font\\ie8\\*"\r
\tDelete "$SETTINGS_DIR\\css\\customStyles\\*"\r
    RMDir "$SETTINGS_DIR\\css\\font\\ie8\\"\r
    RMDir "$SETTINGS_DIR\\css\\font"\r
\tRMDir "$SETTINGS_DIR\\css\\customStyles"\r
\tRMDir "$SETTINGS_DIR\\css"\r
\t\r
\tDelete "$SETTINGS_DIR\\img\\*"\r
\tDelete "$SETTINGS_DIR\\img\\basicToolbar\\*"\r
\tDelete "$SETTINGS_DIR\\img\\defaultToolbar\\*"\r
\tRMDir "$SETTINGS_DIR\\img\\defaultToolbar"\r
\tRMDir "$SETTINGS_DIR\\img\\basicToolbar"\r
\tRMDir "$SETTINGS_DIR\\img"\r
\t\r
\tDelete "$SETTINGS_DIR\\amisPrefs.xml"\r
    Delete "$SETTINGS_DIR\\amisPrefsDebug.xml"\r
    Delete "$SETTINGS_DIR\\amisPrefsCompatibilityMode.xml"\r
    Delete "$SETTINGS_DIR\\amisPrefsCompatibilityModeWithDX.xml"\r
    Delete "$SETTINGS_DIR\\amisPrefsCompatibilityModeWithTTS.xml"\r
    Delete "$SETTINGS_DIR\\clearCache.bat"\r
    Delete "$SETTINGS_DIR\\defaultToolbar.xml"\r
    Delete "$SETTINGS_DIR\\basicToolbar.xml"\r
    Delete "$SETTINGS_DIR\\amisHistory.xml.default"\r
    Delete "$SETTINGS_DIR\\clearHistory.bat"\r
    Delete "$SETTINGS_DIR\\resource.h.ini"\r
    Delete "$SETTINGS_DIR\\amisLog.txt"\r
\r
    Delete "$INSTDIR\\xslt\\l10n\\*"\r
    RMDir "$INSTDIR\\xslt\\l10n\\"\r
    Delete "$INSTDIR\\xslt\\dtbook\\*"\r
    RMDir "$INSTDIR\\xslt\\dtbook\\"\r
    Delete "$INSTDIR\\xslt\\*"\r
    RMDir "$INSTDIR\\xslt"    \r
    Delete "$INSTDIR\\*"\r
    RMDir "$INSTDIR"\r
    ; this deletes all the registry keys used by NSIS\r
    DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"\r
    DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"\r
\r
    Delete "$DESKTOP\\AMIS.lnk" \r
    \r
\tDelete "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text114",True) # u'$text114' on line 626, col 36
        if _v is not None: write(_filter(_v, rawExpr=u'$text114')) # from line 626, col 36.
        write(u'''\\*"\r
\tDelete "$SMPROGRAMS\\AMIS\\*"\r
\t\r
    RMDir "''')
        write(_filter("$SMPROGRAMS\\AMIS\\"))
        _v = VFFSL(SL,"text114",True) # u'$text114' on line 629, col 38
        if _v is not None: write(_filter(_v, rawExpr=u'$text114')) # from line 629, col 38.
        write(u'''\\"\r
    RMDir "$SMPROGRAMS\\AMIS\\"\r
    \r
    SetAutoClose true\r
SectionEnd\r
\r
;******\r
;uninstall the langpacks\r
;**\r
Section -un.CopyLangpack\r
\t\r
\tDelete "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\help\\*"\r
    Delete "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\help\\img\\*"\r
    Delete "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\audio\\*"\r
  \r
    RMDir "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\help\\img"\r
    RMDir "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\help"\r
    RMDir "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\audio"\r
\r
    Delete "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\shortcuts\\*"\r
    RMDir "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\shortcuts"\r
\r
    Delete "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}\\*"\r
    RMDir "$SETTINGS_DIR\\lang\\${DEFAULT_LANG_ID}"\r
\r
    ${If} ${CUSTOM_LANG_ID} != ""\r
        Delete "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\help\\*"\r
        Delete "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\help\\img\\*"\r
        Delete "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\audio\\*"\r
\r
        RMDir "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\help\\img"\r
        RMDir "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\help"\r
        RMDir "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\audio"\r
\r
        Delete "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\shortcuts\\*"\r
        RMDir "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\shortcuts"\r
\r
        Delete "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}\\*"\r
        RMDir "$SETTINGS_DIR\\lang\\${CUSTOM_LANG_ID}"\r
    ${EndIf}\r
\r
    Delete "$SETTINGS_DIR\\lang\\readme.txt"\r
    RMDir "$SETTINGS_DIR\\lang"\r
SectionEnd\r
\r
Section -un.RemoveHistoryBookmarks\r
\tIfSilent Remove\r
    MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "''')
        _v = VFFSL(SL,"text113",True) # u'$text113' on line 676, col 56
        if _v is not None: write(_filter(_v, rawExpr=u'$text113')) # from line 676, col 56.
        write(u'''" IDYES Remove IDNO End\r
Remove:\r
    Delete "$SETTINGS_DIR\\amisHistory.xml"\r
    Delete "$SETTINGS_DIR\\bmk\\*"\r
    RMDir "$SETTINGS_DIR\\bmk"\r
    ; the settings dir should now be empty\r
    RMDir "$SETTINGS_DIR"\r
    RMDir "$APPDATA\\AMIS\\"\r
End:\r
SectionEnd\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_SetupAmis3NsiTemplate= 'respond'

## END CLASS DEFINITION

if not hasattr(SetupAmis3NsiTemplate, '_initCheetahAttributes'):
    templateAPIClass = getattr(SetupAmis3NsiTemplate, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(SetupAmis3NsiTemplate)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=SetupAmis3NsiTemplate()).run()


