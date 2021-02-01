MainWindow.clearData()
MainWindow.openPreWindow()
box = CAD.Box()
box.setName('Box_1')
box.setLocation(0,0,0)
box.setPara(10,10,10)
box.create()
cylinder = CAD.Cylinder()
cylinder.setName('Cylinder_2')
cylinder.setLocation(0,0,0)
cylinder.setRadius(5)
cylinder.setLength(10)
cylinder.setAxis(0,0,1)
cylinder.create()
booloperation = CAD.BooLOperation()
booloperation.setBoolType('Fause')
booloperation.setIndexOfSolid1InGeo(1,0)
booloperation.setIndexOfSolid2InGeo(2,0)
booloperation.create()
gmsher = Mesher.Gmsher()
gmsher.setDim(3)
gmsher.appendSolid(3,0)
gmsher.setElementType("Tet")
gmsher.setElementOrder(1)
gmsher.setMethod(1)
gmsher.setSizeFactor(1)
gmsher.setMinSize(0)
gmsher.setMaxSize(1.0)
gmsher.cleanGeo()
gmsher.startGenerationThread()
