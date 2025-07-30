
def tag_attributes(description):
    tags = []
    if "cotton" in description.lower():
        tags.append("Material: Cotton")
    if "red" in description.lower():
        tags.append("Color: Red")
    if "t-shirt" in description.lower() or "shirt" in description.lower():
        tags.append("Category: T-Shirt")
    return tags
