import json
import time


classMappingCounts = 0
fieldMappingCounts = 0
methodMappingCounts = 0


# Read the raw field mapping files
with open('./mappings/1.8.9_mappings.txt', 'r') as file:
    rawClassMappings = file.readlines()


# ex mappings.txt content (mappings/1.8.9_mappings.txt)
classRef = "CL: ave net/minecraft/client/Minecraft"


# Map the field (FD:)
def classMapping(saveToJson: bool):
    global classMappingCounts  # Declare global variable

    classMappingsJson = []

    # for each mapping elements in the raw mappings
    for mappingLines in rawClassMappings:
        # if the mapping elements starts with "FD:" (field)
        if mappingLines.startswith("CL:"):
            classMappingCounts += 1

            # splits the mapping elements into multiple sentences based on the space
            fieldMappingElements = mappingLines.split()

            # Obfuscated class name | ex: ave (net.minecraft.client.Minecraft)
            fieldMappingElements_1 = fieldMappingElements[1]
            # Sets the results to variables to be used later
            obfuscatedClassName = fieldMappingElements_1

            # Mapped (original) class name | ex: net.minecraft.client.Minecraft (ave)
            fieldMappingElements_2 = fieldMappingElements[2]
            # Sets the results to variables to be used later
            mappedClassName = fieldMappingElements_2

            # print the results
            print(f"[CL:] Mapping class {obfuscatedClassName} to {mappedClassName}")

            # Create a dictionary for the field mapping
            fieldMappingJson = {
                "obfuscatedClassName": obfuscatedClassName,
                "mappedClassName": mappedClassName
            }

            # Add the field mapping to the list
            classMappingsJson.append(fieldMappingJson)

    # Convert the list of field mappings to JSON
    json_data = json.dumps(classMappingsJson, indent=4)

    if saveToJson:
        # Save the JSON data to a file
        with open('class_mappings.json', 'w') as processedMapping:
            processedMapping.write(json_data)

    print(f"Mapped {classMappingCounts} class")


# Read the raw field mapping files
with open('./mappings/1.8.9_mappings.txt', 'r') as file:
    rawFieldMappings = file.readlines()

# ex mappings.txt content (mappings/1.8.9_mappings.txt)
fieldRef = "FD: ave/h Lbew; net/minecraft/client/Minecraft/thePlayer Lnet/minecraft/client/entity/EntityPlayerSP;"


# Map the field (FD:)
def fieldMapping(saveToJson: bool):
    global fieldMappingCounts  # Declare global variable

    fieldMappingsJson = []

    # for each mapping elements in the raw mappings
    for mappingLines in rawFieldMappings:
        # if the mapping elements starts with "FD:" (field)
        if mappingLines.startswith("FD:"):
            fieldMappingCounts += 1

            # splits the mapping elements into multiple sentences based on the space
            fieldMappingElements = mappingLines.split()

            # Obfuscated field name | ex: h (thePlayer)
            # Obfuscated owner name | ex: ave (net.minecraft.client.Minecraft)
            # Obfuscated full path name | ex: ave/h (net.minecraft.client.Minecraft.thePlayer)
            fieldMappingElements_1 = fieldMappingElements[1]
            # Splits the second sentence by "/"
            # Sets the results to variables to be used later
            obfuscatedOwnerName = fieldMappingElements_1.split("/")[0]
            obfuscatedFieldName = fieldMappingElements_1.split("/")[1]
            obfuscatedFullPathName = fieldMappingElements_1

            # Obfuscated object type | ex: Lwn; (Lnet/minecraft/entity/player/EntityPlayer;)
            fieldMappingElements_2 = fieldMappingElements[2]
            # Sets the results to variables to be used later
            obfuscatedObjectType = fieldMappingElements_2

            # Mapped (original) field name | ex: thePlayer (h)
            # Mapped (original) owner name | ex: net.minecraft.client.Minecraft (ave)
            # Mapped (original) full path name | ex: net.minecraft.client.Minecraft.thePlayer (ave/h)
            fieldMappingElements_3 = fieldMappingElements[3]
            # Splits the second sentence by "/"
            # Sets the results to variables to be used later
            mappedFullPathName = fieldMappingElements_3

            # Mapped (original) object type ex: Lnet/minecraft/entity/player/EntityPlayer; (Lwn;)
            fieldMappingElements_4 = fieldMappingElements[4]
            # Sets the results to variables to be used later
            mappedObjectType = fieldMappingElements_4

            # print the results
            print(f"[FD:] Mapping field {obfuscatedOwnerName}/{obfuscatedFieldName} to {mappedFullPathName}, obfObjectType: {obfuscatedObjectType}, objectType: {mappedObjectType}")

            # Create a dictionary for the field mapping
            fieldMappingJson = {
                "obfuscatedFieldName": obfuscatedFieldName,
                "obfuscatedOwnerName": obfuscatedOwnerName,
                "obfuscatedFullPathName": obfuscatedFullPathName,
                "obfuscatedObjectType": obfuscatedObjectType,
                "mappedFullPathName": mappedFullPathName,
                "mappedObjectType": mappedObjectType
            }

            # Add the field mapping to the list
            fieldMappingsJson.append(fieldMappingJson)

    # Convert the list of field mappings to JSON
    json_data = json.dumps(fieldMappingsJson, indent=4)

    if saveToJson:
        # Save the JSON data to a file
        with open('field_mappings.json', 'w') as processedMapping:
            processedMapping.write(json_data)

    print(f"Mapped {fieldMappingCounts} fields")


# ex mappings.txt content (mappings/1.8.9_mappings.txt)
methodRef = "MD: pk/F ()I net/minecraft/entity/Entity/getEntityId ()I"


# Read the raw method mapping files
with open('./mappings/1.8.9_mappings.txt', 'r') as file:
    rawMethodMappings = file.readlines()


# Map the field (FD:)
def methodMapping(saveToJson: bool):
    global methodMappingCounts  # Declare global variable

    methodMappingsJson = []

    # for each mapping elements in the raw mappings
    for mappingLines in rawMethodMappings:
        # if the mapping elements starts with "FD:" (field)
        if mappingLines.startswith("MD:"):
            methodMappingCounts += 1

            # splits the mapping elements into multiple sentences based on the space
            fieldMappingElements = mappingLines.split()

            # Obfuscated field name | ex: h (thePlayer)
            # Obfuscated owner name | ex: ave (net.minecraft.client.Minecraft)
            # Obfuscated full path name | ex: ave/h (net.minecraft.client.Minecraft.thePlayer)
            fieldMappingElements_1 = fieldMappingElements[1]
            # Splits the second sentence by "/"
            # Sets the results to variables to be used later
            obfuscatedOwnerName = fieldMappingElements_1.split("/")[0]
            obfuscatedMethodName = fieldMappingElements_1.split("/")[1]
            obfuscatedFullPathName = fieldMappingElements_1

            # Obfuscated object type | ex: Lwn; (Lnet/minecraft/entity/player/EntityPlayer;)
            fieldMappingElements_2 = fieldMappingElements[2]
            # Sets the results to variables to be used later
            obfuscatedObjectType = fieldMappingElements_2

            # Mapped (original) field name | ex: thePlayer (h)
            # Mapped (original) owner name | ex: net.minecraft.client.Minecraft (ave)
            # Mapped (original) full path name | ex: net.minecraft.client.Minecraft.thePlayer (ave/h)
            fieldMappingElements_3 = fieldMappingElements[3]
            # Splits the second sentence by "/"
            # Sets the results to variables to be used later
            mappedFullPathName = fieldMappingElements_3

            # Mapped (original) object type ex: Lnet/minecraft/entity/player/EntityPlayer; (Lwn;)
            fieldMappingElements_4 = fieldMappingElements[4]
            # Sets the results to variables to be used later
            mappedObjectType = fieldMappingElements_4

            # print the results
            print(f"[MD:] Mapping method {obfuscatedOwnerName}/{obfuscatedMethodName} to {mappedFullPathName}, obfObjectType: {obfuscatedObjectType}, objectType: {mappedObjectType}")

            # Create a dictionary for the field mapping
            methodMappingJson = {
                "obfuscatedMethodName": obfuscatedMethodName,
                "obfuscatedOwnerName": obfuscatedOwnerName,
                "obfuscatedFullPathName": obfuscatedFullPathName,
                "obfuscatedObjectType": obfuscatedObjectType,
                "mappedFullPathName": mappedFullPathName,
                "mappedObjectType": mappedObjectType
            }

            # Add the field mapping to the list
            methodMappingsJson.append(methodMappingJson)

    # Convert the list of field mappings to JSON
    json_data = json.dumps(methodMappingsJson, indent=4)

    if saveToJson:
        # Save the JSON data to a file
        with open('method_mappings.json', 'w') as processedMapping:
            processedMapping.write(json_data)

    print(f"Mapped {fieldMappingCounts} methods")


# Main processes
if __name__ == '__main__':
    # Capture the start time
    startTime = time.perf_counter()

    # Starting mapping process
    print("Starting mapping process...")

    # Starts the class mapping process (CL:)
    classMapping(saveToJson=True)

    # Starts the field mapping process (FD:)
    fieldMapping(saveToJson=True)

    # Starts the method mapping process (MD:)
    methodMapping(saveToJson=True)

    # Capture the end time
    endTime = time.perf_counter()

    print(f"Mapped {classMappingCounts} class, {fieldMappingCounts} fields, and {methodMappingCounts} methods.")

    # Calculate the elapsed time
    elapsedTime = endTime - startTime
    print(f"Elapsed time: {elapsedTime} seconds ({elapsedTime * 1000} ms)")
