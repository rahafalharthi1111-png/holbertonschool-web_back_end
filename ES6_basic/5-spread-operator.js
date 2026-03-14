export default function concatArrays(array1, array2, string) {
  const concatenate = [...array1, ...array2, ...string];
  return concatenate;
}
