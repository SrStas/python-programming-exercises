class MyClass:
    def countingValleys(steps, path):
        # convert string to list
        pathList = list(path)
        elivationCounter = 0
        valleysCounter = 0
        valleyTrigger = False
        for step in pathList:
            if step == "U":
                elivationCounter += 1
            elif step == "D":
                elivationCounter -= 1

            # check if we are entering valley
            if elivationCounter < 0 and not valleyTrigger:
                valleyTrigger = True
            # check if leaving valley
            if elivationCounter == 0 and valleyTrigger:
                valleysCounter += 1
                valleyTrigger = False

        return valleysCounter


steps = 8
path = "DDUUUUDDUDDDUU"


if __name__ == "__main__":
    # steps = int(input().strip())
    # path = input()
    result = MyClass.countingValleys(steps, path)
    print(str(result) + "\n")
