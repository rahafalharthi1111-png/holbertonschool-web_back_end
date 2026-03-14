export default function appendToEachArrayValue(array, appendString) {
  const tableau = [];
  for (const value of array) {
    tableau.push(appendString + value);
  }

  return tableau;
}
