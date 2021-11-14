// All Inclusive?
package kata

func ContainAllRots(strng string, arr []string) bool {
    if strng == "" {
        return true
    }
    var rotation string = string(strng[1:]) + string(strng[0])
    for rotation != strng {
        if !rotationInArray(rotation, arr) {
            return false
        }
        rotation = string(rotation[1:]) + string(rotation[0])
    }
    if !rotationInArray(strng, arr) {
        return false
    }
    return true
}

func rotationInArray(rotation string, arr[]string) bool {
    for _, elem := range arr {
        if elem == rotation {
            return true
        }
    }
    return false
}
