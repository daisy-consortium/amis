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

#ifndef NAVMODEL_H
#define NAVMODEL_H

#include "dtb/nav/NavMap.h"
#include "dtb/nav/NavList.h"
#include "dtb/nav/PageList.h"

#include "Media.h"
#include "dtb/CustomTest.h"
#include "Error.h"
#include "dtb/nav/NavVisitor.h"
#include "AmisCore.h"

namespace amis
{
namespace dtb
{
namespace nav
{
class NavModel
{
public:
	NavModel();
	~NavModel();

	unsigned int getNumberOfNavLists();
	NavList* getNavList(unsigned int);
	NavList* getNavList(string);
	NavListList* getNavLists();
	int addNavList(string);
	bool hasPages();
	PageList* getPageList();
	NavMap* getNavMap();
	void acceptDepthFirst(NavVisitor*);
	NavNode* getNodeForSmilId(string, NavContainer*);
	void setSmilIdNodeMap(NodeRefMap*);
	void testMap();
	NavPoint* previousSection(int);
	NavPoint* nextSection(int);
	PageTarget* previousPage(int);
	PageTarget* nextPage(int);
	//add a node to the big ordered list.  the node will not necessarily be next in sequence.
	void addToPlayOrderList(NavNode*);
	NavNodeList* getPlayOrderList();
private:
	NavMap* mpNavMap;
	PageList* mpPageList;
	NodeRefMap* mpSmilIdNodeMap;
	NavListList mNavLists;
	NavNodeList mPlayOrderList;
};
}
}
}

#endif
