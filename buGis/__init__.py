# -*- coding: utf-8 -*-
"""
/***************************************************************************
 buGis
                                 A QGIS plugin
 a plugin to create boundary lines
                             -------------------
        begin                : 2014-01-30
        copyright            : (C) 2014 by Ivan Busthomi
        email                : ivanbusthomi@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load buGis class from file buGis
    from bugis import buGis
    return buGis(iface)
