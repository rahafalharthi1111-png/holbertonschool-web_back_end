export default function getStudentIdsSum(List) {
    const sum = List.reduce((acc, student) => {
      return acc + student.id;
    }, 0);
    return sum;
}
