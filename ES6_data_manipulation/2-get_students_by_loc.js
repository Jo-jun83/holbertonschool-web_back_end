const getStudentsByLocation = (ListStudents, city) => {
  const filteredStudents = ListStudents.filter((student) => student.location === city);
  return filteredStudents;
};

export default getStudentsByLocation;
