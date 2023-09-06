#!/usr/bin/env python3
import sys
import yaml

action = sys.argv[1]

actionYaml = yaml.safe_load(open(f"{action}/action.yaml").read())

start = "# Inputs"


def get_inputs():
    doc_string = ""

    if "inputs" in actionYaml:
        doc_string += "|Input Name|Description|Required|Default|Type|\n"
        doc_string += "|---|---|---|---|---|\n"

        for inputName, input in actionYaml["inputs"].items():
            if "description" in input:
                description = input["description"]
            else:
                description = " "

            if "required" in input:
                required = input["required"]
            else:
                required = " "

            if "type" in input:
                type = input["type"]
            else:
                type = " "

            if "default" in input:
                default = input["default"]
            else:
                default = " "

            doc_string += f"|{inputName}|{description}|{required}|{default}|{type}|\n"
    return doc_string


def get_outputs():
    doc_string = ""
    if "outputs" in actionYaml:
        doc_string = "\n# Outputs\n"
        doc_string += "|Output Name|Value|\n"
        doc_string += "|---|---|\n"
        for outputName, output in actionYaml["outputs"].items():
            doc_string += f"|{outputName}|{output['value']}|\n"
    return doc_string


def get_readme():
    return open(f"{action}/README.md").read()


if __name__ == '__main__':
    readme = get_readme()

    foundMaker = False
    preMarker = ""
    for line in readme.split("\n"):
        if start in line:
            break
        preMarker += line + "\n"

    preMarker += f"{start}\n"
    preMarker += get_inputs()
    preMarker += get_outputs()
    preMarker += "\n"

    f = open(f"{action}/README.md", "w")
    f.write(preMarker)
    f.close()
