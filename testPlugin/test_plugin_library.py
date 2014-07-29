from qgis.core import *

def circumCenter(self, pointA, pointB, pointC):
    xA=pointA.x()
    yA=pointA.y()

    xB=pointB.x()
    yB=pointB.y()

    xC=pointC.x()
    yC=pointC.y()

    a2 = xA^2+yA^2
    b2 = xB^2+yB^2
    c2 = xC^2+yC^2

    const = 2*(xA*(yB-yC)+xB*(yC-yA)+xC*(yA-yB))
    xO = (a2*(yB-yC)+b2*(yC-yA)+c2*(yA-yB))/const
    yO = (a2*(xC-xB)+b2*(xA-xC)+c2*(xB-xA))/const
    pointO = QgsPoint(xO,yO)
    return pointO

def lineToPoint(lineLayer):                                       # STATUS : working      OUTPUT : memory layer
    #from PyQt4.QtCore import QVariant
    # function to convert line feature to point feature
    # PS: add function to add Attribute of A and B layer, to differentiate in processing later
    pointLayer = QgsVectorLayer("Point", "Point Result", "memory")
    prPoint = pointLayer.dataProvider()
    # add attribute collumns
    prPoint.addAttributes([QgsField("Id_feature", QVariant.Int)])
    feats = []
    for line in lineLayer.getFeatures():
        #get coordinate list from asPolyline function
        lineGeom = line.geometry()
        listCoord = lineGeom.asPolyline()
        inc = 0
        #convert to point
        for c in listCoord:
            increase = inc
            point = QgsPoint(c[0],c[1])
            geomPoint = QgsGeometry.fromPoint(point)
            #feat = QgsFeature(fields_)
            feat = QgsFeature()
            feat.setGeometry(geomPoint)
            # add atributes
            feat.setAttributes([increase])
            inc = increase + 1
            feats.append(feat)
        #add to defined point layer
        prPoint.addFeatures(feats)
        QgsMapLayerRegistry.instance().addMapLayer(pointLayer)


def pointToLine(pointLayer):                                    # STATUS : working      OUTPUT : memory layer
    # function to convert point features to line feature
    canvas = iface.mapCanvas()
    lineLayer = QgsVectorLayer("LineString", "Line Result", "memory")              # line Layer saved in memory
    prLine = lineLayer.dataProvider()
    pointList = []
    for point in pointLayer.getFeatures():
        p = point.geometry().asPoint()
        pointList.append(p)
    feat = QgsFeature()
    lineGeom = QgsGeometry.fromPolyline(pointList)
    feat.setGeometry(lineGeom)
    prLine.addFeatures([feat])
    QgsMapLayerRegistry.instance().addMapLayer(lineLayer)

def midPoint(point1,point2):        # working fine
    #this function returns midpoint from two input point as result.
    x1=point1.x()
    y1=point1.y()
    x2=point2.x()
    y2=point2.y()
    xMid=x1+(x2-x1)/2.0
    yMid=y1+(y2-y1)/2.0
    mid=(xMid,yMid)
    return mid


def perpendicularLine(pointA,pointB):
    # this function is to find a line that is perpendicular to line AB at its midpoint
    import math
    x1 = pointA.x()
    y1 = pointA.y()
    x2 = pointB.x()
    y2 = pointB.y()
    #-------------------------------------
    middleCoord = midPoint(pointA,pointB)
    middlePoint = QgsPoint(middleCoord[0],middleCoord[1])
    xm = middlePoint.x()
    ym = middlePoint.y()
    #-------------------------------------
    # get max extent value from both point layer
    extA = pointLayerA.extent()     #global variable
    extB = pointLayerB.extent()     #global variable
    if extA.xMaximum() > extB.xMaximum():
        xmax = extA.xMaximum()
    else:
        xmax = extB.xMaximum()
    if extA.yMaximum() > extB.yMaximum():
        ymax = extA.yMaximum()
    else:
        ymax = extB.yMaximum()
    # in order to shorten the equation
    P = x2 - x1
    Q = y2 - y1
    R = xm - x1
    S = ym - y1
    # line gradien, for determining max distance of perpendicular line
    gradien1 = Q / P
    gradien2 = -1/gradien1
    #-------------------------------------
    u = R / P
    u_ = S / Q                                                      # optional value, only for checking
    d2 = pointA.sqrDist(pointB)                                     # d is the distance. d2 is square of d
    #-------------------------------------
    # here comes the equation
    # y3*Q = (-P)*x3 + P*x1 + Q*y1 + u*d2
    # x3*P = (-Q)*y3 + P*x1 + Q*y1 + u*d2
    #-------------------------------------
    # we want the perpendicular line goes until the maximum value of pointA and B, just to make sure it works
    # in any shape of topography,,,,,,,,,, or maybe minimum value of pointA and B. need more consideration later.
    if math.pow(gradien2,2) > 1:
        y3 = ymax
        x3 = ((-Q)*y3 + P*x1 + Q*y1 + u*d2) / P
    else:
        x3 = xmax
        y3 = ((-P)*x3 + P*x1 + Q*y1 + u*d2) / Q
    #-------------------------------------
    ppdPoint = QgsPoint(x3,y3)
    pointList = []
    pointList.append(middlePoint)
    pointList.append(ppdPoint)
    #-------------------------------------
    p3Line = QgsGeometry.fromPolyline(pointList)
    return p3Line                                               # type QgsGeometry
