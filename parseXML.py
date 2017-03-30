import xml.etree.ElementTree as ET

tree= ET.parse('esempio.xml')

root = tree.getroot()
ET.dump(root)
#print (root.tag)
#for child in root:
    #print(child.tag,child.attrib)

#root = ET.Element('articolo')
#paragrafo1 = ET.SubElement(root,'paragrafo')
#ET.dump(root)




