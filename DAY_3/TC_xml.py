import xml.etree.ElementTree as Et

tree = Et.parse("student.xml")
root = tree.getroot()

for student in root.findall("Student"):
    id = student.find("Id").text
    name = student.find("Name").text
    age = student.find("Age").text
    print(id, name, age)

root = Et.Element("employee")
emp1 = Et.SubElement(root, "emp")
Et.SubElement(emp1, "id").text = "101"
Et.SubElement(emp1, "Name").text = "Uday"
Et.SubElement(emp1, "Salary").text = "100000"
emp2 = Et.SubElement(root, "emp")
Et.SubElement(emp2, "id").text = "102"
Et.SubElement(emp2, "Name").text = "Hari"
Et.SubElement(emp2, "Salary").text = "200000"

tree = Et.ElementTree(root)
tree.write("employee.xml")
print("xml file written successfully")

