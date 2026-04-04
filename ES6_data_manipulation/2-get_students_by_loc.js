export default function getStudentsByLocation(List, city) {
    const new_array = List.filter((student) => student.location === city)
    return new_array
}
