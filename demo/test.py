import mimetypes
ob = Objecttype.objects.get(title="Document")
a  = "/home/dhiru/Desktop/ncert2/ncert_nroer/demo/static/img/"
l2 =ob.member_objects.all()
list_of = [ [ mimetypes.guess_type(a+each.altnames)[0],each]  for each in l2]
for each in list_of:
    b = each[1]
    print b
    if not each[0] == None:
	    if "audio" in each[0]:
        	b.objecttypes.remove(Objecttype.objects.get(title="Document"))
        	b.objecttypes.add(Objecttype.objects.get(title="Audio"))
	    if "image" in each[0]:                              
		b.objecttypes.remove(Objecttype.objects.get(title="Document"))
        	b.objecttypes.add(Objecttype.objects.get(title="Graphics"))
	    if "video" in each[0] or "flash" in each[0]:                              
		b.objecttypes.remove(Objecttype.objects.get(title="Document"))
        	b.objecttypes.add(Objecttype.objects.get(title="Multimedia"))
	    if "pdf"  in each[0]:                              
		b.objecttypes.remove(Objecttype.objects.get(title="Document"))
        	b.objecttypes.add(Objecttype.objects.get(title="Presentation"))

    

