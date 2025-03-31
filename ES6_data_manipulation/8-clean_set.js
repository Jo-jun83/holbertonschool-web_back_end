const cleanSet = (set, startString) => {
  if (!startString) return '';

  return [...set]
    .filter((word) => word.startsWith(startString))
    .map((word) => word.slice(startString.length))
    .join('-');
};

export default cleanSet;
