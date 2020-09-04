function GetImageList1(HSetConds) {
	var ImageList1 = []
		for (var i=0; i<HSetConds.length; i++) { 
		    ImageList1[i] = Obj1[HSetConds[i]-1];	
		}
return ImageList1
}

function GetImageList2(HSetConds) {
	var ImageList2 = [];	
					for (var i=0; i<HSetConds.length; i++) { 
            ImageList2[i] = Obj2[HSetConds[i]-1];						    
				}
return ImageList2
}

function GetImageListsrc1(ImageList1) {
	var ImageListsrc1 = [];
	for (var i=0; i<HSetConds.length; i++) { 
    	ImageListsrc1[i] = "../StimuliSets/ExploringObjects72-squared-3-luminance/"+ImageList1[i];
	}	
	return ImageListsrc1;
}

function GetImageListsrc2(ImageList2) {
    var ImageListsrc2 = [];
	for (var i=0; i<HSetConds.length; i++) { 
    	ImageListsrc2[i] = "../StimuliSets/ExploringObjects72-squared-3-luminance/"+ImageList2[i];
	}	
	return ImageListsrc2;
}

var Obj1 = ["apple.png", "axe.png", "backpack.png", "bed.png", "bicycle.png", "binoculars.png", "blender.png", "bookshelf.png", "broom.png", "cake.png", "canoe.png", "axe.png", "backpack.png", "bed.png", "bicycle.png", "binoculars.png", "blender.png", "bookshelf.png", "broom.png", "cake.png", "canoe.png", "backpack.png", "bed.png", "bicycle.png", "binoculars.png", "blender.png", "bookshelf.png", "broom.png", "cake.png", "canoe.png", "bed.png", "bicycle.png", "binoculars.png", "blender.png", "bookshelf.png", "broom.png", "cake.png", "canoe.png", "bicycle.png", "binoculars.png", "blender.png", "bookshelf.png", "broom.png", "cake.png", "canoe.png", "binoculars.png", "blender.png", "bookshelf.png", "broom.png", "cake.png", "canoe.png", "blender.png", "bookshelf.png", "broom.png", "cake.png", "canoe.png", "bookshelf.png", "broom.png", "cake.png", "canoe.png", "broom.png", "cake.png", "canoe.png", "cake.png", "canoe.png", "canoe.png"]
var Obj2 = ["alarmclock.png", "alarmclock.png", "alarmclock.png", "alarmclock.png", "alarmclock.png", "alarmclock.png", "alarmclock.png", "alarmclock.png", "alarmclock.png", "alarmclock.png", "alarmclock.png", "apple.png", "apple.png", "apple.png", "apple.png", "apple.png", "apple.png", "apple.png", "apple.png", "apple.png", "apple.png", "axe.png", "axe.png", "axe.png", "axe.png", "axe.png", "axe.png", "axe.png", "axe.png", "axe.png", "backpack.png", "backpack.png", "backpack.png", "backpack.png", "backpack.png", "backpack.png", "backpack.png", "backpack.png", "bed.png", "bed.png", "bed.png", "bed.png", "bed.png", "bed.png", "bed.png", "bicycle.png", "bicycle.png", "bicycle.png", "bicycle.png", "bicycle.png", "bicycle.png", "binoculars.png", "binoculars.png", "binoculars.png", "binoculars.png", "binoculars.png", "blender.png", "blender.png", "blender.png", "blender.png", "bookshelf.png", "bookshelf.png", "bookshelf.png", "broom.png", "broom.png", "cake.png"]