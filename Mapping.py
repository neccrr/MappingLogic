import json
import time

# global variables
classMappingCounts = 0
fieldMappingCounts = 0
methodMappingCounts = 0


# mappings.txt content (mappings/1.8.9_mappings.txt)
# "CL: ave net/minecraft/client/Minecraft"
#
# Map the classes
def classMapping(saveToJson: bool):
    # Read the raw field mapping files
    with open('mappings/raw/1.8.9_mappings.txt', 'r') as rawClassMappingFile:
        rawClassMappings = rawClassMappingFile.readlines()

    global classMappingCounts  # Declare global variable

    classMappingsJson = []

    # for each mapping elements in the raw mappings
    for mappingLines in rawClassMappings:
        # if the mapping elements starts with "FD:" (field)
        if mappingLines.startswith("CL:"):
            classMappingCounts += 1

            # splits the mapping elements into multiple sentences based on the space
            classMappingElements = mappingLines.split()

            # Obfuscated class name | ex: ave (net.minecraft.client.Minecraft)
            obfuscatedClassName = classMappingElements[1]

            # Mapped (original) class name | ex: net.minecraft.client.Minecraft (ave)
            mappedClassName = classMappingElements[2]

            # print the results
            print(f"[CL:] Mapping class {obfuscatedClassName} to {mappedClassName}")

            # Create a dictionary for the field mapping
            classMappingData = {
                "obfuscatedClassName": obfuscatedClassName,
                "mappedClassName": mappedClassName
            }

            # Add the field mapping to the list
            classMappingsJson.append(classMappingData)

    # Convert the list of field mappings to JSON
    json_data = json.dumps(classMappingsJson, indent=4)

    if saveToJson:
        # Save the JSON data to a file
        with open('mappings/processed/class_mappings.json', 'w') as processedMapping:
            processedMapping.write(json_data)

    print(f"Mapped {classMappingCounts} class")


# mappings.txt content (mappings/1.8.9_mappings.txt)
# "FD: ave/h Lbew; net/minecraft/client/Minecraft/thePlayer Lnet/minecraft/client/entity/EntityPlayerSP;"
#
# Map the field
def fieldMapping(saveToJson: bool):
    # Read the raw field mapping files
    with open('mappings/raw/1.8.9_mappings.txt', 'r') as rawFieldMappingFile:
        rawFieldMappings = rawFieldMappingFile.readlines()

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
            obfuscatedFieldName = fieldMappingElements[1].split("/")[1]
            # Obfuscated owner name | ex: ave (net.minecraft.client.Minecraft)
            obfuscatedFieldOwnerName = fieldMappingElements[1].split("/")[0]
            # Obfuscated full path name | ex: ave/h (net.minecraft.client.Minecraft.thePlayer)
            obfuscatedFieldFullPathName = fieldMappingElements[1]

            # Obfuscated object type | ex: Lwn; (Lnet/minecraft/entity/player/EntityPlayer;)
            obfuscatedFieldObjectType = fieldMappingElements[2]

            # Mapped (original) field name | ex: thePlayer (h)
            # Get the very last part of it
            mappedFieldName = fieldMappingElements[3].split("/")[-1]
            # Mapped (original) owner name | ex: net.minecraft.client.Minecraft (ave)
            # Get the rest of the part except the very last one
            mappedOwnerFieldName = "/".join(fieldMappingElements[3].split("/")[:-1])
            # Mapped (original) full path name | ex: net.minecraft.client.Minecraft.thePlayer (ave/h)
            mappedFieldFullPathName = fieldMappingElements[3]

            # Mapped (original) object type ex: Lnet/minecraft/entity/player/EntityPlayer; (Lwn;)
            mappedFieldObjectType = fieldMappingElements[4]

            # print the results
            print(f"[FD:] Mapping field {obfuscatedFieldOwnerName}/{obfuscatedFieldName} to {mappedFieldFullPathName}, obfObjectType: {obfuscatedFieldObjectType}, objectType: {mappedFieldObjectType}")

            # Create a dictionary for the field mapping
            fieldMappingData = {
                "obfuscatedFieldName": obfuscatedFieldName,
                "obfuscatedFieldOwnerName": obfuscatedFieldOwnerName,
                "obfuscatedFieldFullPathName": obfuscatedFieldFullPathName,
                "obfuscatedFieldObjectType": obfuscatedFieldObjectType,
                "mappedFieldName": mappedFieldName,
                "mappedOwnerFieldName": mappedOwnerFieldName,
                "mappedFieldFullPathName": mappedFieldFullPathName,
                "mappedFieldObjectType": mappedFieldObjectType
            }

            # Add the field mapping to the list
            fieldMappingsJson.append(fieldMappingData)

    # Convert the list of field mappings to JSON
    json_data = json.dumps(fieldMappingsJson, indent=4)

    if saveToJson:
        # Save the JSON data to a file
        with open('mappings/processed/field_mappings.json', 'w') as processedMapping:
            processedMapping.write(json_data)

    print(f"Mapped {fieldMappingCounts} fields")


# mappings.txt content (mappings/1.8.9_mappings.txt)
# "MD: pk/F ()I net/minecraft/entity/Entity/getEntityId ()I"
#
# Map the method
def methodMapping(saveToJson: bool):
    # Read the raw method mapping files
    with open('mappings/raw/1.8.9_mappings.txt', 'r') as rawMethodMappingFile:
        rawMethodMappings = rawMethodMappingFile.readlines()

    global methodMappingCounts  # Declare global variable

    methodMappingsJson = []

    # for each mapping elements in the raw mappings
    for mappingLines in rawMethodMappings:
        # if the mapping elements starts with "FD:" (field)
        if mappingLines.startswith("MD:"):
            methodMappingCounts += 1

            # splits the mapping elements into multiple sentences based on the space
            methodMappingElements = mappingLines.split()

            # Splits the second sentence by "/"
            # Obfuscated method name | ex: h (thePlayer)
            obfuscatedMethodName = methodMappingElements[1].split("/")[1]
            # Obfuscated owner name | ex: ave (net.minecraft.client.Minecraft)
            obfuscatedMethodOwnerName = methodMappingElements[1].split("/")[0]
            # Obfuscated full path name | ex: ave/h (net.minecraft.client.Minecraft.thePlayer)
            obfuscatedMethodFullPathName = methodMappingElements[1]

            # Obfuscated object type | ex: Lwn; (Lnet/minecraft/entity/player/EntityPlayer;)
            obfuscatedMethodObjectType = methodMappingElements[2]

            # Splits the second sentence by "/"
            # Mapped (original) method name | ex: thePlayer (h)
            mappedMethodName = methodMappingElements[3].split("/")[-1]
            # Mapped (original) owner name | ex: net.minecraft.client.Minecraft (ave)
            mappedMethodOwnerName = "/".join(methodMappingElements[3].split("/")[:-1])
            # Mapped (original) full path name | ex: net.minecraft.client.Minecraft.thePlayer (ave/h)
            mappedMethodFullPathName = methodMappingElements[3]

            # Mapped (original) object type ex: Lnet/minecraft/entity/player/EntityPlayer; (Lwn;)
            mappedMethodObjectType = methodMappingElements[4]

            # print the results
            print(f"[MD:] Mapping method {obfuscatedMethodOwnerName}/{obfuscatedMethodName} to {mappedMethodFullPathName}, obfObjectType: {obfuscatedMethodObjectType}, objectType: {mappedMethodObjectType}")

            # Create a dictionary for the field mapping
            methodMappingData = {
                "obfuscatedMethodName": obfuscatedMethodName,
                "obfuscatedMethodOwnerName": obfuscatedMethodOwnerName,
                "obfuscatedMethodFullPathName": obfuscatedMethodFullPathName,
                "obfuscatedMethodObjectType": obfuscatedMethodObjectType,
                "mappedMethodName": mappedMethodName,
                "mappedMethodOwnerName": mappedMethodOwnerName,
                "mappedMethodFullPathName": mappedMethodFullPathName,
                "mappedMethodObjectType": mappedMethodObjectType
            }

            # Add the field mapping to the list
            methodMappingsJson.append(methodMappingData)

    # Convert the list of field mappings to JSON
    json_data = json.dumps(methodMappingsJson, indent=4)

    if saveToJson:
        # Save the JSON data to a file
        with open('mappings/processed/method_mappings.json', 'w') as processedMapping:
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

    # Format the elapsed time
    hours, a = divmod(elapsedTime, 3600)
    minutes, seconds = divmod(a, 60)
    formattedTime = ""
    if hours > 0:
        formattedTime += f"{int(hours)} hours "
    if minutes > 0:
        formattedTime += f"{int(minutes)} minutes "
    formattedTime += f"{seconds:.2f} seconds"

    print(f"Elapsed time: {elapsedTime} seconds ({elapsedTime * 1000} ms)")
    print(f"{formattedTime}")
