/*
AMIS: Adaptive Multimedia Information System
Software for playing DAISY books
Homepage: http://amis.sf.net

Copyright (C) 2004-2007  DAISY for All Project

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/

#include "stdafx.h"
#include "Preferences.h"
#include "gui/AmisApp.h"
#include "util/SearchForFilesMFC.h"
#include "util/FilePathTools.h"
#include "io/ModuleDescReader.h"
#include "util/Log.h"
using namespace amis;

Preferences* Preferences::pinstance = 0;

Preferences* Preferences::Instance()
{
	if (pinstance == 0) pinstance = new Preferences;
    return pinstance;
}


void Preferences::DestroyInstance()
{
	delete pinstance;
}

Preferences::Preferences()
{
	setUiLangId("eng-US");
	setPauseOnLostFocus(true);
	setIsSelfVoicing(false);
	setUseTTSNotAudio(false);
	setLoadLastBook(false);
	setStartInBasicView(false);
	setTTSVoiceIndex(0);
	setWasExitClean(true);
	setDisableScreensaver(true);
	mFontsizeCssFiles.clear();
	mCustomCssFiles.clear();
	//note that file paths here are hardcoded relative to the application directory
	//whereas in the prefs XML file, they are relative to the prefs XML file
	//they get overridden by reading in the preferences file; these defaults are just here as a safety measure
	mFontsizeCssDir = ambulant::net::url::from_filename("./settings/css/font/");
	mCustomCssDir = ambulant::net::url::from_filename("./settings/css/contrast/");
	mLangpacksDir = ambulant::net::url::from_filename("./settings/lang/");
	mUserBmkDir = ambulant::net::url::from_filename("./settings/bmk/");
	mAmisCssFile = ambulant::net::url::from_filename("./settings/css/amis.css");	
	mZed2005CssFile = ambulant::net::url::from_filename("./settings/css/dtbook.2005.basic.css");

	ambulant::net::url app_path = ambulant::net::url::from_filename(theApp.getAppPath());
	mFontsizeCssDir = mFontsizeCssDir.join_to_base(app_path);
	mCustomCssDir = mCustomCssDir.join_to_base(app_path);
	mLangpacksDir = mLangpacksDir.join_to_base(app_path);
	mUserBmkDir = mUserBmkDir.join_to_base(app_path);
	mAmisCssFile = mAmisCssFile.join_to_base(app_path);
	mZed2005CssFile = mZed2005CssFile.join_to_base(app_path);

	mHighlightFG.set("#000000");
	mHighlightBG.set("#FFFF00");
	mSidebarFontName = "Arial";
}

//this function should be called after the preferences XML file has been parsed
void Preferences::scanAll()
{
	scanDirectoriesForCssFiles();
	scanDirectoriesForLanguagePackFiles();
	
}
void Preferences::scanDirectoriesForCssFiles()
{
	amis::util::SearchForFilesMFC searcher;
	searcher.addSearchCriteria(".css");
	//these files will only bother developers
	searcher.addSearchExclusionCriteria(".svn");
	searcher.setRecursiveSearch(true);
	if (searcher.startSearch(mFontsizeCssDir.get_file()) > 0)
	{
		mFontsizeCssFiles = *searcher.getSearchResults();
	}
	else 
	{
		TRACE(_T("No fontsize css files found\n"));
		amis::util::Log::Instance()->writeWarning("No fontsize css files found in directory",
			&mFontsizeCssDir, "Preferences::scanDirectoriesForCssFiles", "AmisGuiMFC2");
	}
	
	searcher.clearSearchResults();
	if (searcher.startSearch(mCustomCssDir.get_file()) > 0)
	{
		mCustomCssFiles = *searcher.getSearchResults();
	}
	else 
	{
		TRACE(_T("No contrast css files found\n"));
		string log_msg = "No contrast css files found in " + mCustomCssDir.get_url();
	}
}

//search for "moduleDesc.xml" files that inside the root language pack directory
//save the ones that have type="langpack" enabled="yes" on the root moduleDesc element
//store the language id and media group of the language label
void Preferences::scanDirectoriesForLanguagePackFiles()
{
	amis::util::SearchForFilesMFC searcher;
	searcher.addSearchCriteria("moduleDesc.xml");
	//these files will only bother developers
	searcher.addSearchExclusionCriteria(".svn");
	searcher.setRecursiveSearch(true);
	if (searcher.startSearch(mLangpacksDir.get_file()) > 0)
	{
		amis::UrlList list = *searcher.getSearchResults();
		for (int i = 0; i<list.size(); i++)
		{
			amis::io::ModuleDescReader reader;
			if (reader.readFromFile(&list[i]))
			{
				amis::ModuleDescData* p_data = reader.getModuleDescData();
				if (p_data == NULL)
				{
					TRACE(_T("No data available for language pack\n"));
					string log_msg = "No data available for language pack " + list[i].get_url();
					amis::util::Log::Instance()->writeError("No data available for language pack", 
						&list[i], "Preferences::scanDirectoriesForLanguagePackFiles", "AmisGuiMFC2");
				}
				else
				{
					if (p_data->isEnabled() && p_data->getModuleType() == amis::ModuleDescData::LANGPACK)
					{
						string id = p_data->getId();
						mInstalledLanguages[id] = p_data;
						string log_msg = "Added language pack for " + id;
						amis::util::Log::Instance()->writeMessage(log_msg, 
							"Preferences::scanDirectoriesForLanguagePackFile", "AmisGuiMFC2");
					}
				}
			}
			else
			{
				TRACE(_T("Could not read language pack file\n"));
				amis::util::Log::Instance()->writeError("Could not read language pack file: ", &list[i], 
					"Preferences::scanDirectoriesForLanguagePackFiles", "AmisGuiMFC2");
			}
		}
	}
	else
	{
		TRACE(_T("No language pack files found\n"));
		amis::util::Log::Instance()->writeError("No language pack files found", 
			"Preferences::scanDirectoriesForLanguagePackFiles", "AmisGuiMFC2");
	}
}

Preferences::~Preferences()
{
	amis::StringModuleMap::iterator it = mInstalledLanguages.begin();
	while (mInstalledLanguages.size() > 0)
	{
		amis::ModuleDescData* p_module = it->second;
		if (p_module != NULL) delete p_module;
		mInstalledLanguages.erase(it);
		it = mInstalledLanguages.begin();
	}
}

//************************************
//ACCESSORS
void Preferences::setUiLangId(string value)
{
	mUiLangId = value;
}
string Preferences::getUiLangId()
{
	return mUiLangId;
}

void Preferences::setStartInBasicView(bool value)
{
	mbStartInBasicView = value;
}

bool Preferences::getStartInBasicView()
{
	return mbStartInBasicView;
}

void Preferences::setLoadLastBook(bool value)
{
	mbLoadLastBook = value;
}

bool Preferences::getLoadLastBook()
{
	return mbLoadLastBook;
}

void Preferences::setPauseOnLostFocus(bool value)
{
	mbPauseOnLostFocus = value;
}

bool Preferences::getPauseOnLostFocus()
{
	return mbPauseOnLostFocus;
}

void Preferences::setIsSelfVoicing(bool value)
{
	mbIsSelfVoicing = value;
}

bool Preferences::getIsSelfVoicing()
{
	return mbIsSelfVoicing;
}

void Preferences::setTTSVoiceIndex(int value)
{
	mTTSVoiceIndex = value;
}

int Preferences::getTTSVoiceIndex()
{
	return mTTSVoiceIndex;
}

void Preferences::setUseTTSNotAudio(bool value)
{
	mbUseTTSNotAudio = value;
}

bool Preferences::getUseTTSNotAudio()
{
	return mbUseTTSNotAudio;
}

void Preferences::setWasExitClean(bool value)
{
	mbWasExitClean = value;
}

bool Preferences::getWasExitClean()
{
	return mbWasExitClean;
}
void Preferences::setHighlightText(bool value)
{
	mbHighlightText = value;
}
bool Preferences::getHighlightText()
{
	return mbHighlightText;
}
void Preferences::setDisableScreensaver(bool value)
{
	mbDisableScreensaver = value;
}
bool Preferences::getDisableScreensaver()
{
	return mbDisableScreensaver;
}
void Preferences::setUserBmkDir(const ambulant::net::url* value)
{
	mUserBmkDir = *value;
}

const ambulant::net::url* Preferences::getUserBmkDir()
{
	return &mUserBmkDir; 
}

void Preferences::setLangpacksDir(const ambulant::net::url* value)
{
	mLangpacksDir = *value;
}

const ambulant::net::url* Preferences::getLangpacksDir()
{
	return &mLangpacksDir;
}

void Preferences::setFontsizeCssDir(const ambulant::net::url* value)
{
	mFontsizeCssDir = *value;
}

const ambulant::net::url* Preferences::getFontsizeCssDir()
{
	return &mFontsizeCssDir;
}

void Preferences::setCustomCssDir(const ambulant::net::url* value)
{
	mCustomCssDir = *value;
}

const ambulant::net::url* Preferences::getCustomCssDir()
{
	return &mCustomCssDir;
}

void Preferences::setAmisCssFile(const ambulant::net::url* value)
{
	mAmisCssFile = *value;
}

const ambulant::net::url* Preferences::getAmisCssFile()
{
	return &mAmisCssFile;
}

void Preferences::setZed2005CssFile(const ambulant::net::url* value)
{
	mZed2005CssFile = *value;
}

const ambulant::net::url* Preferences::getZed2005CssFile()
{
	return &mZed2005CssFile;
}

void Preferences::setSourceUrl(const ambulant::net::url* value)
{
	mSourceUrl = *value;
}

const ambulant::net::url* Preferences::getSourceUrl()
{
	return &mSourceUrl;
}

amis::UrlList* Preferences::getFontsizeCssFiles()
{
	return &mFontsizeCssFiles;
}

amis::UrlList* Preferences::getCustomCssFiles()
{
	return &mCustomCssFiles;
}
amis::StringModuleMap* Preferences::getInstalledLanguages()
{
	return &mInstalledLanguages;
}

amis::ModuleDescData* Preferences::getCurrentLanguageData()
{
	amis::ModuleDescData* p_data = mInstalledLanguages[mUiLangId];
	return p_data;
}
void Preferences::setHighlightBGColor(amis::util::Color value)
{
	mHighlightBG = value;
}
amis::util::Color Preferences::getHighlightBGColor()
{
	return mHighlightBG;
}
void Preferences::setHighlightFGColor(amis::util::Color value)
{
	mHighlightFG = value;
}
amis::util::Color Preferences::getHighlightFGColor()
{
	return mHighlightFG;
}
void Preferences::setSidebarFontName(std::string value)
{
	mSidebarFontName = value;
}
std::string Preferences::getSidebarFontName()
{
	return mSidebarFontName;
}
void Preferences::logAllPreferences()
{
	amis::util::Log* p_log = amis::util::Log::Instance();
	p_log->writeMessage("__Preferences (all)__");
	
	p_log->writeMessage("\tPreferences XML File: ", getSourceUrl());
	
	string log_msg = "\tLanguage pack = " + getUiLangId();
	p_log->writeMessage(log_msg);

	log_msg = "\tStartup view = ";
	if (getStartInBasicView()) log_msg += "Basic";
	else log_msg += "Default";
	p_log->writeMessage(log_msg);

	log_msg = "\tWill load last book on startup? ";
	if (getLoadLastBook()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);
	
	log_msg = "\tWill pause when AMIS loses application focus? ";
	if (getPauseOnLostFocus()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);

	log_msg = "\tIs self-voicing? ";
	if (getIsSelfVoicing()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);
	
	//TODO: log tts voice index as something meaningful

	log_msg = "\tUsing TTS or pre-recorded audio? ";
	if (getUseTTSNotAudio()) log_msg += "TTS";
	else log_msg += "Audio";
	p_log->writeMessage(log_msg);

	log_msg = "\tDid AMIS exit cleanly last time? ";
	if (getWasExitClean()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);

	log_msg = "\tHighlight text? ";
	if (getHighlightText()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);

	log_msg = "\tDisable screensaver? ";
	if (getDisableScreensaver()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);

	p_log->writeMessage("\tBookmark dir = ", &mUserBmkDir);
	p_log->writeMessage("\tLangpacks dir = ", &mLangpacksDir);
	p_log->writeMessage("\tFontsize css dir = ", &mFontsizeCssDir);
	p_log->writeMessage("\tContrast css dir = ", &mCustomCssDir);
	p_log->writeMessage("\tAmis css file = ", &mAmisCssFile);
	p_log->writeMessage("\tZed2005 css file = ", &mZed2005CssFile);

	p_log->writeMessage("\tInstalled language packs:");
	amis::StringModuleMap::iterator it;
	it = mInstalledLanguages.begin();
	while (it != mInstalledLanguages.end())
	{
		string lang_id = it->first;
		log_msg = "\t\t" + lang_id;
		p_log->writeMessage(log_msg);
		it++;
	}

	p_log->writeMessage("\tFontsize CSS files:");
	for (int i = 0; i<mFontsizeCssFiles.size(); i++)
		p_log->writeMessage("\t\t", &mFontsizeCssFiles[i]);


	p_log->writeMessage("\tCustom CSS files:");
	for (int i = 0; i<mCustomCssFiles.size(); i++)
		p_log->writeMessage("\t\t", &mCustomCssFiles[i]);
}

void Preferences::logUserControllablePreferences()
{
	amis::util::Log* p_log = amis::util::Log::Instance();
	p_log->writeMessage("__Preferences (user-controllable only)__");

	string log_msg = "\tLanguage pack = " + getUiLangId();
	p_log->writeMessage(log_msg);

	log_msg = "\tStartup view = ";
	if (getStartInBasicView()) log_msg += "Basic";
	else log_msg += "Default";
	p_log->writeMessage(log_msg);

	log_msg = "\tWill load last book on startup? ";
	if (getLoadLastBook()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);
	
	log_msg = "\tWill pause when AMIS loses application focus? ";
	if (getPauseOnLostFocus()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);

	log_msg = "\tIs self-voicing? ";
	if (getIsSelfVoicing()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);

	log_msg = "\tHighlight text? ";
	if (getHighlightText()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);

	log_msg = "\tDisable screensaver? ";
	if (getDisableScreensaver()) log_msg += "Yes";
	else log_msg += "No";
	p_log->writeMessage(log_msg);
}