const getStudentIdsSum = (ListStudents) => {
  const sum = ListStudents.reduce((acc, curr) => acc + curr.id, 0);
  return sum;
};
export default getStudentIdsSum;
