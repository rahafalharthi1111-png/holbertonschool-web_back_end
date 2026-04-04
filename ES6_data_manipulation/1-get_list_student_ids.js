export default function getListStudentIds(List) {
    if (!Array.isArray(List)) {
      return [];
    }
    return List.map((student) => student.id);
}
