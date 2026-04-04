export default function updateStudentGradeByCity(students, city, newGrades) {
  const gradesIndex = new Map(newGrades.map((g) => [g.studentId, g.grade]));

  const inCity = students.filter((student) => student.location === city);

  return inCity.map((s) => {
  const found = gradesIndex.get(s.id);
  const finalGrade = (found !== undefined) ? found : 'N/A';
  return { ...s, grade: finalGrade };
});
}
